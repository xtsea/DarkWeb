# COPYRIGHT https://github.com/TeamKillerX/DarkWeb
# CREATE CODING BY https://t.me/xtsea

import os
from pyrogram import Client as ren
from pyrogram.types import *
from pyrogram import *
from DarkWeb.helper.cmd import *
from DarkWeb.modules.randydev.dev import shell_exec
from pykillerx.help import *

@ren.on_message(filters.command("convert", cmd) & filters.me)
async def photo_as_sticker(c, m: Message):
    try:
        pro = await m.reply_text("`Prossing....`")
        goblok_lu = m.text.split(" ", 1)[1]
        ran = m.reply_to_message
        if not ran and not goblok_lu: 
           return await pro.edit("**Please Reply [image/background]**")

        if goblok_lu.startswith("-p"):
           await pro.delete()
           file_name = "downloads/ran.webp"
           upload = await ran.download()
           (await shell_exec("cd downloads && cp *.jpg ran.webp"))[0]
           await c.send_sticker(m.chat.id, file_name)
           os.remove(file_name)
           os.remove(upload)

        if goblok_lu.startswith("-r"):
           await pro.delete()
           file_name = "downloads/ran.webp"
           upload = await ran.download()
           (await shell_exec("cd downloads && cp *.png ran.webp"))[0]
           await c.send_sticker(m.chat.id, file_name)
           os.remove(file_name)
           os.remove(upload)

    except BaseException:
        pass
