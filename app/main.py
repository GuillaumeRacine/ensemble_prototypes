from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import structlog
import time
from contextlib import asynccontextmanager

from app.config import get_settings
from app.database import init_db
from app.integrations.instagram import router as instagram_router

# Configure structured logging
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer()
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager"""
    # Startup
    logger.info("Starting Present Agent API")
    settings = get_settings()
    
    if settings.debug:
        logger.info("Running in debug mode")
    
    # Initialize database
    await init_db()
    logger.info("Database initialized")
    
    yield
    
    # Shutdown
    logger.info("Shutting down Present Agent API")


# Create FastAPI app
app = FastAPI(
    title="Present Agent API",
    description="AI-powered gift recommendation platform",
    version="0.1.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all HTTP requests"""
    start_time = time.time()
    
    # Log request
    logger.info(
        "Request started",
        method=request.method,
        url=str(request.url),
        client=request.client.host if request.client else None
    )
    
    # Process request
    response = await call_next(request)
    
    # Log response
    process_time = time.time() - start_time
    logger.info(
        "Request completed",
        method=request.method,
        url=str(request.url),
        status_code=response.status_code,
        process_time=process_time
    )
    
    return response


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler"""
    logger.error(
        "Unhandled exception",
        exc_info=exc,
        request_url=str(request.url),
        request_method=request.method
    )
    
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )


# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "present-agent"}


# Root endpoint
@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Present Agent API",
        "version": "0.1.0",
        "docs": "/docs"
    }


# Include routers
app.include_router(instagram_router, prefix="/webhook", tags=["instagram"])


if __name__ == "__main__":
    import uvicorn
    settings = get_settings()
    
    uvicorn.run(
        "app.main:app",
        host=settings.app_host,
        port=settings.app_port,
        reload=settings.debug,
        log_level=settings.log_level.lower()
    )