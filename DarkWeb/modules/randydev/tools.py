# COPYRIGHT https://github.com/TeamKillerX/DarkWeb
# CREATE CODING BY https://t.me/xtsea

import os
from pyrogram import Client as ren
from pyrogram.types import *
from pyrogram import *
from DarkWeb.helper.cmd import *
from DarkWeb.modules.randydev.dev import shell_exec
from pykillerx.help import *

@ren.on_message(filters.command("psticker", cmd) & filters.me)
async def photo_as_sticker(c, m):
    try:
        ran = m.reply_to_message
        file_name = "downloads/ran.jpg"
        upload = await ran.download()
        (await shell_exec("cd downloads && cp *.jpg ran.webp"))[0]
        await c.send_sticker(m.chat.id, file_name)
        os.remove(file_name)
        os.remove(upload)
    except BaseException:
        pass
