import asyncio
from termcolor import colored
from connect import login, logout, con_stat, stat
from qtx_config import amount_gale, duration
from client import qtx
from zoztex.utils.operation_type import OperationType
import time


async def execute_gale(direction, asset):
    connection = await con_stat()
    if connection:
        while True:
            if connection:
                status, gale_info = await qtx.trade(direction, amount_gale, asset, 100)
                if status:
                    print(colored('[GALE]', 'blue'), 'Executed')
                    await check_win_gale(gale_info)
                    return status, gale_info
        
async def check_win_gale(gale_info):
    await con_stat()
    print('waiting for result')
    if await qtx.check_win(gale_info['id']):
        print(colored('[WIN WITH GALE]', 'green'), f"{qtx.get_profit()}")
    else:
        print(colored('[LOSS]', 'red'),f"{qtx.get_profit()}")
    
async def main():
    direction = (OperationType.CALL_GREEN)
    asset = 'USDMXN_otc'
    status, gale_info = await execute_gale(direction, asset)
    if status:
        await check_win_gale(gale_info)



    
if __name__ == "__main__":
    asyncio.run(main())
