import selfcord
import asyncio
import random
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()  # Load variabel environment dari file .env

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))  # Pastikan convert ke int
FAUCET_COMMAND = os.getenv("FAUCET_COMMAND")

class MyClient(selfcord.Client):
    def __init__(self):
        super().__init__()
        self.last_sent_time = None

    async def on_ready(self):
        print(f'Logged on as {self.user}')
        channel = self.get_channel(CHANNEL_ID)
        if channel is None:
            print(f"Channel ID {CHANNEL_ID} Not Found")
            return

        while True:
            now = datetime.now()

            if self.last_sent_time is None:
                can_send = True
            else:
                cooldown = timedelta(hours=6)
                random_delay_hours = random.uniform(0, 3)
                next_send_time = self.last_sent_time + cooldown + timedelta(hours=random_delay_hours)
                can_send = now >= next_send_time

            if can_send:
                try:
                    await channel.send(FAUCET_COMMAND)
                    self.last_sent_time = datetime.now()
                    print(f"Message sent at {self.last_sent_time}")
                except Exception as e:
                    print(f"Error when send message: {e}")
                    await asyncio.sleep(60)
                    continue
            else:
                remaining = (next_send_time - now).total_seconds()
                print(f"Cooldown. Wait {int(remaining)} seconds...")
                await asyncio.sleep(remaining)
                continue

            await asyncio.sleep(60)

client = MyClient()
client.run(TOKEN)
