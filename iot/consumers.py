
from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json


class IOTConsumerClass(AsyncJsonWebsocketConsumer):
    ui_connection_list = list()
    device_connection_list = list()
    async def connect(self):
        await self.accept() # Configuyre django channels' channel layer to get channel_name attrubute.
        print("Channel {0} connected.".format(self.channel_name))
    
    async def disconnect(self, code):
        if self.channel_name in IOTConsumerClass.ui_connection_list:
            print("UI channel {0} disconnected.".format(self.channel_name))
            IOTConsumerClass.ui_connection_list.remove(self.channel_name)
        elif self.channel_name in IOTConsumerClass.device_connection_list:
            print("Device channel {0} disconnected.".format(self.channel_name))
            IOTConsumerClass.device_connection_list.remove(self.channel_name)
        return await super().disconnect(code)
    
    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        if text_data == "PING":
            await self.send("PONG")
        else:
            payload_json = json.loads(text_data)
            print(payload_json)
            if 'from' in payload_json:
                print(payload_json['from'])
                if payload_json['from'] == 'UI':
                    IOTConsumerClass.ui_connection_list.append(self.channel_name)
                elif payload_json['from'] == 'device':
                    IOTConsumerClass.device_connection_list.append(self.channel_name)
            else:
                for connection in IOTConsumerClass.ui_connection_list:
                    print(connection)
                

    
    async def broadcast_to_connections(self, event):
        pass
