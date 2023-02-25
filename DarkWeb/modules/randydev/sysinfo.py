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

# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# COPYRIGHT https://github.com/TeamKillerX/DarkWeb
# CREATE CODING BY https://t.me/xtsea

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
        sysinfo = (await shell_exec("neofetch | sed 's/\x1B\\[[0-9;\\?]*[a-zA-Z]//g'"))[0]
        carbon = await make_carbon(sysinfo)
        await c.send_photo(chat_id, carbon, caption=f"Carbonised by {c.me.mention}")
        await pro.delete()
    except Exception:
        pass
