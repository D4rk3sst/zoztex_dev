from client import qtx
from connect import login, logout, con_stat, stat
from termcolor import colored
import asyncio




async def balance():
    connection = await con_stat
    if connection:
        balance = await qtx.get_balance()
        print(colored('[BALANCE]', 'blue'), f"{balance}")
        return balance


if __name__ == "__main__":
    asyncio.run(balance())