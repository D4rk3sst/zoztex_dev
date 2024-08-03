import json
import re
import asyncio
from termcolor import colored
from config import *
from telethon.sync import TelegramClient

teleclient =  TelegramClient('zoztex', api_id, api_hash)

async def signals():
    print(colored("[INFO] ", "blue"), "Starting telegram client")
    await teleclient.start(phone_number)
    print("Waiting for Signal")
    LAST_MESSAGE_ID_FILE = 'last_message_id.txt'
    SIGNALS_JSON_FILE = 'signals.json'
    try:
        with open(LAST_MESSAGE_ID_FILE, 'r') as f:
            last_message_id = int(f.read().strip())
    except (FileNotFoundError, ValueError):
        last_message_id = 0

    while True:
        valid_signal_found = False  # Initialize at the start of each iteration

        entity = await teleclient.get_entity(channel_id)
        new_messages = await teleclient.get_messages(entity, min_id=last_message_id)

        max_id = last_message_id
        new_signals = []

        for message in new_messages:
            if message.id > last_message_id and message.text:
                signal_lines = message.text.split('\n')

                # Check if the message starts with the clock emoji (⏰)
                if signal_lines and signal_lines[0].startswith('⏰'):
                    time_zone = expiry = currency_pair = time_to_execute = direction = first_gale_time = None
                    contains_info = False

                    for line in signal_lines:
                        if line.startswith('⏰'):
                            time_zone = line.split(':')[-1].strip()
                            contains_info = True
                        elif line.startswith('💰'):
                            expiry = line.split()[-2]
                            contains_info = True
                        elif '/' in line:
                            match = re.search(r'([\w/]+);(\d{2}:\d{2});(PUT|BUY)', line)
                            if match:
                                currency_pair, time_to_execute, direction = match.groups()
                                contains_info = True
                        elif 'GALE' in line:
                            match = re.search(r'\d{2}:\d{2}', line)
                            if match:
                                first_gale_time = match.group()
                                contains_info = True

                    if contains_info:
                        data = {
                            "Currency Pair": currency_pair,
                            "Time to Execute": time_to_execute,
                            "Direction": direction,
                            "Time Zone": time_zone,
                            "Expiry": expiry,
                            "First Gale Time": first_gale_time
                        }

                        new_signals.append(data)

                        # Print signal received message
                        print(colored('SIGNAL RECEIVED', 'yellow'))
                        print(colored("Currency Pair:", 'blue'), currency_pair)
                        print(colored("Time to Execute:", 'red'), time_to_execute)
                        print(colored("Direction:", 'magenta'), direction)
                        print(colored('--------------', 'green'))

                        valid_signal_found = True
                        max_id = max(max_id, message.id)

                        # Save new signals to signals.json (overwrite mode)
                        with open(SIGNALS_JSON_FILE, 'w') as json_file:
                            json.dump(new_signals, json_file, indent=4)

                        # Save the last processed message ID after processing
                        last_message_id = max_id
                        with open(LAST_MESSAGE_ID_FILE, 'w') as f:
                            f.write(str(last_message_id))

                        return data  # Return the valid signal data

        await asyncio.sleep(5)  #increase to reduce cpu power



async def main():
    await signals()
    
if __name__ == "__main__":
    asyncio.run(main())
