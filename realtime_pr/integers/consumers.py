from channels.generic.websocket import AsyncWebsocketConsumer
import json
from random import randint

from asyncio import sleep

martin = ['0x4', '0x28', '0xb7', '0xa2', '0x24', '0x69', '0x80']
screen =  ['0x4', '0x2e', '0xb6', '0xa2', '0x24', '0x69', '0x80']
media = ['0x4', '0x27', '0xb6', '0xa2', '0x24', '0x69', '0x80']
macbook =  ['0x4', '0x21', '0xb7', '0xa2', '0x24', '0x69', '0x80']
decimator =  ['0x4', '0x27', '0xb7', '0xa2', '0x24', '0x69', '0x80']
blackmagic = ['0x4', '0x67', '0x45', '0xca', '0xa4', '0x6c', '0x80']
mr = 0
sc = 0
md = 0
mc = 0
dc = 0 
bm = 0  
class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            new = randint(22,27)
            if new==25:
                f = 0
            else:
                f=11               
            await self.send(json.dumps({'message': randint(1,10),'message2':f}))
            await sleep(1)

    
    

 
