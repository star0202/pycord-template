from logging import Logger

from aiosqlite import connect, Connection, Cursor, Row


def require_cursor(func):
    def wrapper(*args, **kwargs):
        return func(cursor=func.__self__.cursor, *args, **kwargs)

    return wrapper


class Database:
    def __init__(self):
        self.path: str
        self.cursor = None
        self.conn: Connection

    @staticmethod
    async def create(path: str, logger: Logger):
        self = Database()
        self.path = path
        self.conn = await connect(self.path, isolation_level=None)
        await self.conn.set_trace_callback(logger.info)
        self.cursor = await self.conn.cursor()
        return self

    @require_cursor
    async def insert(self, cursor: Cursor, table: str, value: tuple):
        await cursor.execute(f"INSERT INTO {table} VALUES {value}")

    @require_cursor
    async def select(self, cursor: Cursor, table: str, value_id: int) -> Row | None:
        await cursor.execute(f"SELECT * FROM {table} WHERE id={value_id}")
        return await cursor.fetchone()

    @require_cursor
    async def update(self, cursor: Cursor, table: str, column: str, value: str | bool | int, value_id: int):
        if isinstance(value, str):
            value = f"'{value}'"
        await cursor.execute(f"UPDATE {table} SET {column}={value} WHERE id={value_id}")

    @require_cursor
    async def delete(self, cursor: Cursor, table: str, value_id: int):
        await cursor.execute(f"DELETE FROM {table} WHERE id={value_id}")

    @require_cursor
    async def execute(self, cursor: Cursor, sql: str) -> Row | None:
        await cursor.execute(sql)
        return await cursor.fetchone()
