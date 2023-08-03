
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.layers import get_channel_layer
import asyncio
import json
import paho.mqtt.client as mqtt

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
        print(event['data'])
        try:
            await self.send(text_data=event['data'])
        except Exception as e:
            print(e)
    
    @classmethod
    def handle_MQTT_message(cls, data):
        channel_layer = get_channel_layer()
        for ui in ui_connection_list:
            asyncio.run(channel_layer.send(ui, {
                'type':'send_to_ui',
                'data':data
            }))
        

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


class MQTTClient(mqtt.Client, AsyncJsonWebsocketConsumer):
    def __init__(self, broker="broker.emqx.io", port=1883, keepalive=60):
        super().__init__()
        self.on_connect = self.on_connect
        self.on_message = self.on_message 
        self.connect(host=broker, port=port, keepalive=keepalive)
        self.received_data = dict()
    
    def on_connect(self, client, user_data, flags, rc):
        print("Connected with the result code of {0}".format(rc))
        client.subscribe("iot/test/topic_1")
    
    def on_message(self, client, user_data, message):
        self.received_data['topic'] = message.topic
        self.received_data['payload'] = message.payload.decode("utf-8")
        # print("{0}".format(self.received_data))
        IOTUIConsumerClass.handle_MQTT_message(data=self.received_data['payload'])
        
    
client = MQTTClient("broker.emqx.io", 1883, 60)
client.loop_start()
