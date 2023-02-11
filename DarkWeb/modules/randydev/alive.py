from pyrogram import Client as ren
from pyrogram.types import *
from pyrogram import *
from DarkWeb.helper.cmd import *
from DarkWeb.helper.misc import *
from pykillerx import *
from pykillerx.helper import *
from pykillerx.helper.basic import *
from pykillerx.help import *


@ren.on_message(filters.command("yanto", cmd) & filters.me)
async def yanto_alive(c: Client, m: Message):
    try:
        new_msg = get_arg(m)
        if new_msg.startswith("-a"):
           yanto_alive = "https://telegra.ph/file/4118da6eaec984162ab0c.jpg"
           await c.send_photo(m.chat.id, photo=yanto_alive)

    except BaseException:
        pass
