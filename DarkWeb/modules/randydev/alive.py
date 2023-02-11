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
        user = await c.get_users("me")
        txt = f"""
           ** 〄 𝐃𝐀𝐑𝐊 𝐖𝐄𝐁 〄**
           ❏ **full_name**: `{user.first_name}`
           ├•  **premium**: `{user.is_premium}`
           ├• **dc_id**: `{user.dc_id}`
           ├• **ᴠᴇʀsɪᴏɴ**: `{BOT_VER}`
           ├• **ᴘʏᴋɪʟʟᴇʀx**: `{killerx}` [`{where_hosted()}`]
           ├• **ᴜᴘᴛɪᴍᴇ**: `{str(dt.now() - START_TIME).split('.')[0]}`
           ├• **ᴘʏᴛʜᴏɴ**: `{python_version()}`
           ├• **ᴘʏʀᴏɢʀᴀᴍ**: `{__version__}`
           └• **ᴍᴏᴅᴜʟᴇs**: `{len(CMD_HELP)}`
"""
        new_msg = get_arg(m)
        if new_msg.startswith("-a"):
           yanto_alive = "https://telegra.ph/file/4118da6eaec984162ab0c.jpg"
           await c.send_photo(m.chat.id, photo=yanto_alive, caption=txt)

    except BaseException:
        pass
