# create by @xtsea

from io import BytesIO
from pyrogram import Client as ren
from pyrogram import *
from pyrogram.types import *

from DarkWeb.modules.randydev.carbon import make_carbon
from DarkWeb.modules.randydev.dev import shell_exec
from DarkWeb.helper.cmd import cmd 

from pykillerx import *

@ren.on_message(filters.command("neofetch", cmd) & filters.me)
async def neofetch(client: Client, message: Message):
    noob = await message.reply_text("`Prossing.....`")
    try:
        error_install = (await shell_exec("neofetch"))[0]
        if not error_install:
           return await noob.edit("**try** `.bash sudo apt-get install neofetch -y`")
    except Exception:
        return ""
    try:
        neofetch = (await shell_exec("neofetch --stdout"))[0]
        carbon = await make_carbon(neofetch)
        await client.send_photo(message.chat.id, carbon)
        await noob.delete()
    except BaseException as e:
        return await noob.edit(f"**ERROR** `{e}`")

# you can add modules

# this code
