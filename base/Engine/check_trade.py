import asyncio
from connect import con_stat, logout
from client import qtx

async def check_win(trade_info):
    logout()
    await con_stat()
    win = await qtx.check_win(trade_info)
    if win:
        return True
    else:
        return False

async def main():

    win4 = await check_win('a559083f-8146-4c32-91aa-3fae02d5584b')
    if win4:
        print('win')
    else:
        print('loss')

if __name__ == "__main__":
    asyncio.run(main())