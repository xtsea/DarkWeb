# telegram : https://t.me/xtsea

import cv2
import numpy as np
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
    if not message.reply_to_message or not message.reply_to_message.photo:
        await m.reply("Please reply to a photo to detect faces.")
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
    await m.reply_photo("output.jpg", caption="Here are the detected faces.")
