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

import asyncio
import random
from pyrogram import Client as ren
from pyrogram import *
from pyrogram.types import *

from DarkWeb.helper.cmd import *
from DarkWeb.helper.misc import *
from pykillerx.help import *
from pykillerx.helper.tools import *
from pykillerx.helper.basic import *

# LU GABISA CODING LU KONTOL
# BELAJAR CODING DARI NOL


import DarkWeb.modules.randydev.truth_and_dare_string as truth_and_dare_string
@ren.on_message(filters.command("dare", cmd) & filters.me)
async def dare(c, m):
    try:
        pro = await m.reply_text("`Prossing.....`")
        await pro.edit(f"{random.choice(truth_and_dare_string.DARE)}")
    except BaseException:
        pass

@ren.on_message(filters.command("truth", cmd) & filters.me)
async def truth(c, m):
    try:
        pro = await m.reply_text("`Prossing.....`")
        await pro.edit(f"{random.choice(truth_and_dare_string.TRUTH)}")
    except Exception:
        pass

@ren.on_message(filters.command("dare2", cmd) & filters.me)
async def dare2(c, m):
    kntl = await m.reply_text("`Prossing....`")
    dare = "/dare"
    bot  = "truthordares_bot"
    bacot = await c.send_message(bot, dare)
    await asyncio.sleep(2)
    try:
        await bacot.delete()
        await kntl.delete()
        async for izzotol in c.get_chat_history(bot, limit=1):
            await izzotol.copy(m.chat.id)
            await izzotol.delete()
    except BaseException:
        pass


add_command_help(
    "dare",
    [
        [f"dare", "for any other questions"],
        [f"truth", "for any other questions"],
    ],
)
        
