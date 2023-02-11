from datetime import datetime as dt
from pytgcalls import __version__ as tg
from platform import python_version
from pykillerx import __version__ as killerx
from pykillerx.helper.hacking import *
from DarkWeb import START_TIME, CMD_HELP
from pykillerx.extra import *
from DarkWeb import *
from pyrogram import Client as ren
from pyrogram.types import *
from pyrogram import *
from DarkWeb.helper.cmd import *
from DarkWeb.helper.misc import *
from pykillerx import *
from pykillerx.helper import *
from pykillerx.helper.basic import *
from pykillerx.help import *
from config import *


@ren.on_message(filters.command("yanto", cmd) & filters.me)
async def yanto_alive(c: Client, m: Message):
    try:
        new_msg = get_arg(m)
        if new_msg.startswith("-a"):
           user = await c.get_users("me")
        if ALIVE_TEXT:
           txt = ALIVE_TEXT
        else:
            txt = (
            f"** 〄 𝐃𝐀𝐑𝐊 𝐖𝐄𝐁 〄**\n\n"
            f"❏ **full_name**: `{user.first_name}`\n"
            f"├•  **premium**: `{user.is_premium}`\n"
            f"├• **dc_id**: `{user.dc_id}`\n"
            f"├• **ᴠᴇʀsɪᴏɴ**: `{BOT_VER}`\n"
            f"├• **ᴘʏᴋɪʟʟᴇʀx**: `{killerx}` [`{where_hosted()}`]\n"
            f"├• **ᴜᴘᴛɪᴍᴇ**: `{str(dt.now() - START_TIME).split('.')[0]}`\n"
            f"├• **ᴘʏᴛʜᴏɴ**: `{python_version()}`\n"
            f"├• **ᴘʏʀᴏɢʀᴀᴍ**: `{__version__}`\n"
            f"└• **ᴍᴏᴅᴜʟᴇs**: `{len(CMD_HELP)}`\n"

        )
           randy_dev = (f"{txt}")
           yanto_alive = "https://telegra.ph/file/4118da6eaec984162ab0c.jpg"
           await c.send_photo(m.chat.id, photo=yanto_alive, caption=randy_dev)

    except BaseException:
        pass
