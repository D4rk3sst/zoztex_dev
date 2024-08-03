from client import qtx
from zoztex.utils import asset_parse, asrun
from connect import con_stat
import asyncio


async def check_asset(asset):
    await con_stat()
    asset_query = asset_parse(asset)
    asset_open = qtx.check_asset(asset_query)
    if not asset_open or not asset_open[2]:
        asset = f"{asset}_otc" 
        asset_query = asset_parse(asset)
        asset_open = qtx.check_asset(asset_query)
    return asset, asset_open

async def main():
    asset = 'USDMXN'
    asset, asset_open = await check_asset(asset)
    print(asset)


if __name__ == "__main__":
    asyncio.run(main())
