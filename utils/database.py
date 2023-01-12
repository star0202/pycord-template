from aiosqlite import connect
from logging import Logger


class Database:
    def __init__(self, path, logger: Logger):
        self.path = path
        self.conn = await connect(self.path, isolation_level=None)
        self.conn.set_trace_callback(logger.debug)
        self.cursor = await self.conn.cursor()

    async def insert(self, table: str, value: tuple):
        await self.cursor.execute(f"INSERT INTO {table} VALUES {value}")

    async def select(self, table: str, value_id: int):
        await self.cursor.execute(f"SELECT * FROM {table} WHERE id={value_id}")

    async def update(self, table: str, value_id: int, value: tuple):
        await self.cursor.execute(f"UPDATE {table} SET {value} WHERE id={value_id}")

    async def delete(self, table: str, value_id: int):
        await self.cursor.execute(f"DELETE FROM {table} WHERE id={value_id}")
