# create by @xtsea

from io import BytesIO
from pyrogram import Client as ren
from pyrogram import *
from pyrogram.types import *

from DarkWeb.modules.randydev.dev import shell_exec
from DarkWeb.modules.randydev.carbon import make_carbon
from DarkWeb.helper.cmd import cmd 

from pykillerx.help import *

@ren.on_message(filters.command("neofetch", cmd) & filters.me)
async def neofetch(client: Client, message: Message):
    chat_id = message.chat.id
    noob = await message.reply_text("`Prossing.....`")
    try:
        neofetch = (await shell_exec("neofetch --stdout"))[0]
        carbon = await make_carbon(neofetch)
        await noob.edit("`Uloading....`")
        await client.send_photo(chat_id, carbon, caption=f"Carbonised by {client.me.mention}")
        await noob.delete()
    except Exception:
        pass 

# Copyright: https://t.me/xtsea
# your kanger this : please don't remove copyright 

@ren.on_message(filters.command("sysinfo", cmd) & filters.me)
async def sysinfo(c: Client, m: Message):
    chat_id = m.chat.id
    pro = await m.reply_text("`Prossing....`")
    try:
        sysinfo = (await shell_exec("neofetch | sed 's/\x1B\\[[0-9;\\?]*[a-zA-Z]//g'")
        carbon = await make_carbon(sysinfo)
        await c.send_photo(chat_id, carbon, caption=f"Carbonised by {c.me.mention}")
        await pro.delete()
    except Exception:
        pass
