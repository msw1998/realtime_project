from channels.generic.websocket import AsyncWebsocketConsumer
import json
from random import randint

from asyncio import sleep
from .pn532 import *


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
        pn532 = PN532_UART(debug=False, reset=20)

        ic, ver, rev, support = pn532.get_firmware_version()
        print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

        # Configure PN532 to communicate with MiFare cards
        pn532.SAM_configuration()

        await self.accept()
        while True:
            uid = pn532.read_passive_target(timeout=0.5)

            if uid is None:
                continue
            print('Found card with UID:', [hex(i) for i in uid])
            temp = [hex(i) for i in uid]

            if temp == martin:
                mr = mr+1
                print("Martin Mac Aura XB detected")
            elif temp ==blackmagic:
                bm = bm+ 1  
                print("Blackmagic Design URSA is detected")
            elif temp == screen:
                sc =sc+1
                print("55' Screen is detected")
            elif temp == media:
                md= md + 1
                print("Media Server is detected")
            elif temp ==macbook:
                mc= mc + 1
                print("Macbook Pro is detected")
            elif temp == decimator:
                dc = dc + 1  
                print("Decimator MD-HX")


            await self.send(json.dumps({'message': mr,'message2':bm,'message3': sc, 'message4':md,'message5':mc,'message6':dc}))
            await sleep(1)

    
    

 
