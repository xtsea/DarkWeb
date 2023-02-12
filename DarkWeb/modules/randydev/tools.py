"""
Project [DarkWeb](https://github.com/TeamKillerX/DarkWeb) is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""


# COPYRIGHT https://github.com/TeamKillerX/DarkWeb
# CREATE CODING BY https://t.me/xtsea

import os
import requests
import shutil
from pyrogram import Client as ren
from pyrogram.types import *
from pyrogram import *
from DarkWeb.helper.cmd import *
from DarkWeb.modules.randydev.dev import shell_exec
from DarkWeb.helper.misc import *
from pykillerx import *
from pykillerx.helper import *
from pykillerx.helper.basic import *
from pykillerx.help import *
from config import RMBG_API

@ren.on_message(filters.command("convert", cmd) & filters.me)
async def photo_as_sticker(c: Client, m: Message):
    try:
       goblok_lu = get_arg(m)
       ran = m.reply_to_message
       if not ran and not goblok_lu: 
          return await m.edit("**Please Reply [image/background]**")

       if goblok_lu.startswith("-p"):
          file_name = "downloads/ran.webp"
          upload = await ran.download()
          (await shell_exec("cd downloads && cp *.jpg ran.webp"))[0]
          await c.send_sticker(m.chat.id, file_name)
          os.remove(file_name)
          os.remove(upload)

       if goblok_lu.startswith("-r"):
          file_name = "downloads/ran.webp"
          upload = await ran.download()
          (await shell_exec("cd downloads && cp *.png ran.webp"))[0]
          await c.send_sticker(m.chat.id, file_name)
          os.remove(file_name)
          os.remove(upload)

       if goblok_lu.startswith("-m"):
          file_name = "downloads/ran.jpg"
          upload = await ran.download()
          (await shell_exec("cd downloads && cp *.webp ran.jpg"))[0]
          await c.send_photo(m.chat.id, file_name)
          os.remove(file_name)
          os.remove(upload)

       if goblok_lu.startswith("-anime"):
          bot = "AnimeAIAlphaBot"
          photo_id = ran.photo.file_id
          await c.send_photo(bot, photo=photo_id)
          await asyncio.sleep(2)
          async for randydev in c.search_messages(bot, limit=1):
                    if randydev.photo:
                       downloader_as_photo = await c.download_media(photo_id)
                       await c.send_photo(bot, photo=downloader_as_photo)
                       os.remove(downloader_as_photo)

    except BaseException:
        pass


@ren.on_message(filters.command("rmbg", cmd) & filters.me)
async def rmbg_background(c: Client, m: Message):
    api_key = RMBG_API
    photo_id = m.reply_to_message.photo.file_id
    temp_file = await c.download_media(photo_id)
    if not api_key:
       return await m.edit("**RMBG_API: missing**")

    endpoint = "https://api.remove.bg/v1.0/removebg"
    payload = {"size": "auto"}

    if api_key:
       with open(temp_file, "rb") as image_file:
          response = requests.post(endpoint, data=payload, headers={"X-Api-Key": api_key}, files={"image_file": image_file}, stream=True)

    with open("output.png", "wb") as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    await m.reply_document("output.png")
    try:
       clear_file = "ran.webp"
       clear_file2 = "output.png"
       (await shell_exec("cp *.png ran.webp"))[0]
       await c.send_sticker(m.chat.id, "ran.webp")
       os.remove(clear_file)
       os.remove(clear_file2)
    except BaseException:
        pass
    
       
