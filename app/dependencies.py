from app.database.db_session import AsyncSessionLocal


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session