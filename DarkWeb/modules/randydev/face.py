# telegram : https://t.me/xtsea

import os
import asyncio
import cv2
import numpy as np
import requests
from io import BytesIO
from pyrogram import Client as ren
from pyrogram.types import *
from pyrogram import *
from DarkWeb.helper.cmd import *
from DarkWeb.helper.misc import *
from pykillerx import *
from pykillerx.helper import *
from pykillerx.helper.basic import *
from pykillerx.help import *


@ren.on_message(filters.command("facedetect", cmd) & filters.me)
async def face_detect(c: Client, m: Message):
    pro = await m.reply_text("`Whacking face detect.......`")
    await asyncio.sleep(5)
    if not m.reply_to_message or not m.reply_to_message.photo:
        await pro.edit("Please reply to a photo to detect faces.")
        return

    file_id = m.reply_to_message.photo.file_id
    file_path = await c.download_media(file_id)
    img = cv2.imread(file_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imwrite("output.jpg", img)
    await pro.edit("`Successfully sent image`")
    await m.reply_photo("output.jpg", caption="Here are the detected faces.")
    try:
        cleared = "output.png"
        os.remove(cleared)
    except BaseException:
        pass

@ren.on_message(filters.command(["toonify", "cartoon"], cmd) & filters.me)
async def toonify_handler(c: Client, m: Message):
    if not m.reply_to_message or not m.reply_to_message.photo:
        await m.reply_text("Please reply to a photo to convert to cartoon or comic style.")
        return
    
    file_id = m.reply_to_message.photo.file_id
    file_path = await c.download_media(file_id)
   
    with open(file_path, 'rb') as f:
        response = requests.post(
            "https://api.deepai.org/api/toonify",
            files={'image': f},
            headers={'api-key': '4871e0ba-3bb6-40d8-b600-f415877c7606'} # DON'T THIS STEAL
        )
    result = response.json()
    if 'output_url' in result:
        await c.send_photo(m.chat.id, result['output_url'])
    else:
        await m.reply("Failed to toonify the image.")
