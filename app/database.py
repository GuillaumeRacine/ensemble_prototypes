from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
import structlog

from app.config import get_settings

logger = structlog.get_logger()

# Database metadata
metadata = MetaData()
Base = declarative_base(metadata=metadata)

# Global variables for database
engine = None
async_session = None


async def init_db():
    """Initialize database connection"""
    global engine, async_session
    
    settings = get_settings()
    
    # Convert PostgreSQL URL to async version
    db_url = settings.database_url
    if db_url.startswith("postgresql://"):
        db_url = db_url.replace("postgresql://", "postgresql+asyncpg://", 1)
    elif db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql+asyncpg://", 1)
    
    # Create async engine
    engine = create_async_engine(
        db_url,
        echo=settings.debug,  # Log SQL queries in debug mode
        future=True
    )
    
    # Create session factory
    async_session = sessionmaker(
        engine, 
        class_=AsyncSession, 
        expire_on_commit=False
    )
    
    logger.info("Database connection initialized", database_url=db_url.split("@")[0] + "@***")


async def get_db() -> AsyncSession:
    """Get database session"""
    async with async_session() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


async def create_tables():
    """Create all tables"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database tables created")


async def drop_tables():
    """Drop all tables (use with caution!)"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    logger.info("Database tables dropped")