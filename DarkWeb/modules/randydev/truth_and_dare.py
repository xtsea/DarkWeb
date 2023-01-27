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
    except Exception:
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
   try:
       await c.send_message("truthordares_bot", "/start")
    except BaseException:
        pass
    await c.unblock_user("truthordares_bot")
    response = await c.send(
        raw.runctions.messages.StartBot(
            bot = await c.resolve_peer("truthordares_bot"),
            peer = await c.resolve_peer("truthordares_bot"),
            random_id= c.rnd_id(),
            start_param = "dare",
        )
     )
     wait_ren = await m.reply_text("`Prossing.....`")
     await asyncio.sleep(1)
     dare_ren = response.updates[1].message_id + 1 
     status = await c.get_messages(chat_id="truthordares_bot", message_ids=dare_ren)
     await wait.ren.edit_text(f"{status.text}")

add_command_help(
    "dare",
    [
        [f"dare", "for any other questions"],
        [f"truth", "for any other questions"],
    ],
)
        
