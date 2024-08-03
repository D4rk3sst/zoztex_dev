import asyncio
from termcolor import colored
from connect import login, logout, con_stat, stat
from qtx_config import amount, duration
from client import qtx
from zoztex.utils.operation_type import OperationType
import time


async def execute(direction, asset, not_listed=False):
    connection = await con_stat()
    if connection:
        while True:
            if not_listed:
                asset = f"{asset}_otc"
                status, trade_info = await qtx.trade(direction, amount, asset, 30)
                if status:
                    print(trade_info['id'])
                    print(colored('[Executed Successfully]', 'blue'))
                    return True, trade_info
                else:
                    asset = asset.replace('_otc', '')
                    print(asset)
                    logout()
                    await con_stat()
                    status, trade_info = await qtx.trade(direction, amount, asset, 30)
                    if status:
                        print(colored('[Executed Successfully]', 'blue'))
                        return True
            else:
                status, trade_info = await qtx.trade(direction, amount, asset, duration)
                if status:
                    print(colored('[Executed Successfully]', 'blue'))
                    return True


async def check_win(trade_info):
    while True:
        try:
            await con_stat()
            win = await qtx.check_win(trade_info)
            if win:
                print(colored('[WIN]', 'green'), f'{qtx.get_profit()}')
                break
            else:
                print(colored('[loss]', 'red'))
                break
        except asyncio.TimeoutError:
            print('no Result, checking again')


async def main():
    direction = (OperationType.CALL_GREEN)
    asset = 'USDMXN'
    status, trade_info = await execute(direction, asset, not_listed=True)
    if status:
        status_win= await check_win(trade_info['id'])
    else:
        print('trade not executed')
    
if __name__ == "__main__":
    asyncio.run(main())


        
                
        
