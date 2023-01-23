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
    chat_id = message.chat.id
    noob = await message.reply_text("`Prossing.....`")
    try:
        await asyncio.sleep(2)
        await noob.edit("`wait for Installing neofetch`")
        await shell_exec("sudo apt-get install neofetch -y")[0]
    except Exception:
        return ""
    try:
        neofetch = (await shell_exec("neofetch --stdout"))[0]
        await noob.edit("`Uloading....`")
        carbon = await make_carbon(neofetch)
        await client.send_photo(chat_id, carbon, caption=f"Carbonised by {client.me.mention}")
        await noob.delete()
    except Exception:
        return ""

# you can add modules

# this code
