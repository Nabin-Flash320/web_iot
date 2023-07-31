
from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json

ui_connection_list = list()
device_connection_list = list()

class IOTUIConsumerClass(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("UI channel {0} connected.".format(self.channel_name))
        ui_connection_list.append(self.channel_name)

    async def disconnect(self, code):
        print("UI channel {0} disconnected.".format(self.channel_name))
        if self.channel_name in ui_connection_list:
            ui_connection_list.remove(self.channel_name)
    
    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        print(text_data)
        for device in device_connection_list:
            await self.channel_layer.send(device, {
                'type': 'send_to_device',
                'data': text_data
            })
    
    async def send_to_ui(self, event):
        await self.send(text_data=event['data'])


class IOTDevicesConsumerClass(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept() # Configuyre django channels' channel layer to get channel_name attrubute.
        print("Device channel {0}.".format(self.channel_name))
        device_connection_list.append(self.channel_name)
    
    async def disconnect(self, code):
        print("Device channel {0} disconnected.".format(self.channel_name))
        if self.channel_name in device_connection_list:
            device_connection_list.remove(self.channel_name)
    
    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        if text_data == "PING":
            await self.send("PONG")
        else:
            for ui in ui_connection_list:
                await self.channel_layer.send(ui, {
                    'type': 'send_to_ui',
                    'data': text_data
                })

    async def send_to_device(self, event):
        await self.send(text_data=event['data'])

