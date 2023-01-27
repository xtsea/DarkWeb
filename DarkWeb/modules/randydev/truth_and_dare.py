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

# LU GABISA CODING LU KONTOL
# BELAJAR CODING DARI NOL


import ..randydev.truth_and_dare_string as truth_and_dare_string
@ren.on_message(filters.command("dare", cmd) & filters.me)
async def dare(c, m):
    try:
        pro = await m.reply_text("`Prossing.....`")
        await pro.edit(f"{random.choice(truth_and_dare_string.DARE)}")
    except Exception:
        pass

@ren.on_message(filters.command("truth", cmd) & filters.me)
async def dare(c, m):
    try:
        pro = await m.reply_text("`Prossing.....`")
        await pro.edit(f"{random.choice(truth_and_dare_string.TRUTH)}")
    except Exception:
        pass

add_command_help(
    "dare",
    [
        [f"dare", "for any other questions"],
        [f"truth", "for any other questions"],
    ],
)
        
