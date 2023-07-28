
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class IOTConsumerClass(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept() # Configuyre django channels' channel layer to get channel_name attrubute.
    
    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        print(text_data)
        if text_data == "PING":
            await self.send("PONG")