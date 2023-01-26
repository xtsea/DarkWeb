import asyncio
import time
from time import time
from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as ren
from DarkWeb.helper.cmd import *
from DarkWeb.helper.admin import *

from pykillerx.help import *
from pykillerx.helper import *
from pykillerx.helper.tools import *

@ren.on_message(filters.command(["kickdel", "zombies"], cmd) & filters.me)
async def kickdel_cmd(client: Client, message: Message):
    ren = await edit_or_reply(message, "<b>Kicking deleted accounts...</b>")
    values = [
        await message.chat.ban_member(user.user.id, int(time()) + 31)
        for member in await message.chat.get_members()
        if member.user.is_deleted
    ]
    await ren.edit(f"<b>Successfully kicked {len(values)} deleted account(s)</b>")
