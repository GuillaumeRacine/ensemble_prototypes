from fastapi import APIRouter, Request, HTTPException, Query, Depends
from fastapi.responses import PlainTextResponse
import structlog
from typing import Dict, Any

from app.config import get_settings, Settings
from app.services.conversation_handler import ConversationHandler

logger = structlog.get_logger()
router = APIRouter()

# Initialize conversation handler
conversation_handler = ConversationHandler()


@router.get("/instagram")
async def verify_webhook(
    settings: Settings = Depends(get_settings),
    hub_mode: str = Query(alias="hub.mode"),
    hub_challenge: str = Query(alias="hub.challenge"), 
    hub_verify_token: str = Query(alias="hub.verify_token")
):
    """Verify Instagram webhook"""
    
    logger.info(
        "Instagram webhook verification attempt",
        mode=hub_mode,
        verify_token=hub_verify_token[:10] + "..." if hub_verify_token else None
    )
    
    if hub_mode == "subscribe" and hub_verify_token == settings.instagram_verify_token:
        logger.info("Instagram webhook verified successfully")
        return PlainTextResponse(hub_challenge)
    
    logger.warning("Instagram webhook verification failed")
    raise HTTPException(status_code=403, detail="Verification failed")


@router.post("/instagram")
async def handle_instagram_webhook(request: Request):
    """Handle incoming Instagram messages"""
    
    try:
        # Parse request body
        body = await request.json()
        
        logger.info("Instagram webhook received", data=body)
        
        # Process each entry
        for entry in body.get("entry", []):
            # Process messaging events
            for messaging_event in entry.get("messaging", []):
                await process_messaging_event(messaging_event)
        
        return {"status": "ok"}
    
    except Exception as e:
        logger.error("Error processing Instagram webhook", exc_info=e)
        raise HTTPException(status_code=500, detail="Webhook processing failed")


async def process_messaging_event(event: Dict[str, Any]):
    """Process a single messaging event from Instagram"""
    
    try:
        # Extract sender and message
        sender_id = event.get("sender", {}).get("id")
        message_data = event.get("message", {})
        
        if not sender_id or not message_data:
            logger.warning("Invalid messaging event", event=event)
            return
        
        # Extract message text
        message_text = message_data.get("text", "").strip()
        
        if not message_text:
            logger.info("Non-text message received", sender_id=sender_id, message_data=message_data)
            await send_instagram_message(
                sender_id, 
                "Hi! I can help you find the perfect gift. Just send me a text message describing what you're looking for! 🎁"
            )
            return
        
        logger.info(
            "Processing message",
            sender_id=sender_id,
            message=message_text[:100] + "..." if len(message_text) > 100 else message_text
        )
        
        # Process message through conversation handler
        response = await conversation_handler.process_message(
            user_id=sender_id,
            message=message_text,
            platform="instagram"
        )
        
        # Send response back to Instagram
        await send_instagram_message(sender_id, response)
        
    except Exception as e:
        logger.error("Error processing messaging event", exc_info=e, event=event)
        # Send error message to user
        if sender_id:
            await send_instagram_message(
                sender_id, 
                "Sorry, I'm having technical difficulties. Please try again in a moment! 🤖"
            )


async def send_instagram_message(recipient_id: str, message: str):
    """Send a message via Instagram API"""
    
    import httpx
    
    settings = get_settings()
    
    if not settings.instagram_access_token:
        logger.error("Instagram access token not configured")
        return
    
    url = f"https://graph.facebook.com/v18.0/me/messages"
    
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": message}
    }
    
    headers = {
        "Authorization": f"Bearer {settings.instagram_access_token}",
        "Content-Type": "application/json"
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload, headers=headers)
            
            if response.status_code == 200:
                logger.info(
                    "Message sent successfully",
                    recipient_id=recipient_id,
                    message_preview=message[:50] + "..." if len(message) > 50 else message
                )
            else:
                logger.error(
                    "Failed to send Instagram message",
                    status_code=response.status_code,
                    response=response.text,
                    recipient_id=recipient_id
                )
    
    except Exception as e:
        logger.error("Error sending Instagram message", exc_info=e, recipient_id=recipient_id)