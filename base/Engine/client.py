import asyncio
from zoztex import Quotex
from qtx_config import qtx_email, qtx_pass





def on_pin_code() -> str:
    code = input("Enter the code sent to your email: ")
    return code

qtx = Quotex(
    email=qtx_email,
    password=qtx_pass,
    headless=True,
    on_pin_code=on_pin_code,
)



async def main():
    print('starting')
    connection = await qtx.connect()
    if connection:
        print('successfull')
    else:
        print('Error connecting')

if __name__ == "__main__":
    asyncio.run(main())


