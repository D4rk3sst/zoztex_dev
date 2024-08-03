import asyncio
import os
from zoztex import Quotex
from qtx_config import qtx_email, qtx_pass, account
from client import qtx
from zoztex.exceptions import QuotexTimeout, QuotexAuthError


async def login():
    while True:
        try:
            try:
                session_file = os.path.expanduser("~/.sessions.pkl")
                os.remove(session_file)
            except FileNotFoundError:
                pass
            connect = await qtx.connect()
            if connect:
                qtx.change_account(account)
                return True
            else:
                session_file = os.path.expanduser("~/.sessions.pkl")
                os.remove(session_file)
        except QuotexTimeout:
            print('Taking more than usual, check internet connection.')
        except QuotexAuthError:
            print('Check credentials')
        except Exception as e:
            print(e)    
        
        
        print('Retrying in 5 seconds...')
        await asyncio.sleep(2)

async def con_stat():
    connection = qtx.check_connect()
    if not connection:
        await login()
    return True   


def stat():
    connection = qtx.check_connect()
    if connection:
        return True
    else:
        return False
    

def logout():
    while True:
        connection = qtx.check_connect()
        if not connection:
            break
        else:
            qtx.close()
    return True



#debugging
async def main():#connect = await qtx.connect()
   connect = await login()
   print(connect)
   out = logout()
   print(out)
   status = stat()
   print(status)
   
if __name__ == "__main__":
    asyncio.run(main())

