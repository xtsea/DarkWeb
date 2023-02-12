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

from DarkWeb.database.SQL.notes_sql import *
from pyrogram import Client as ren 
from pyrogram import types import *
from DarkWeb.helper.cmd import *
from pykillerx import *
from pykillerx.helper import *
from pykillerx.help import *

@ren.on_message(filters.command("addnote", cmd) & filters.me)
async def add_note_handler(c: Client, m: Message):
    text = m.text.split(' ', 1)
    if len(text) == 2:
        keyword, note = text
        chat_id = str(m.chat.id)
        add_note(chat_id, keyword, note)
        await m.edit(f"Added note `{keyword}`.")
    else:
        await m.edit("Invalid syntax. Use /addnote keyword text")

@ren.on_message(filters.command("getnote", cmd) & filters.me)
async def get_note_handler(c: Client, m: Message):
    text = m.text.split(' ', 1)
    if len(text) == 2:
        keyword = text[1]
        chat_id = str(m.chat.id)
        note = get_note_text(chat_id, keyword)
        if note:
            await m.edit(note)
        else:
            await m.edit(f"Note `{keyword}` not found.")
    else:
        await m.edit("Invalid syntax. Use /getnote keyword")

@ren.on_message(filters.command("delnote", cmd) & filters.me)
async def delete_note_handler(c: Client, m: Message):
    text = m.text.split(' ', 1)
    if len(text) == 2:
        keyword = text[1]
        chat_id = str(m.chat.id)
        deleted = delete_note(chat_id, keyword)
        if deleted:
            await m.edit(f"Note `{keyword}` deleted.")
        else:
            await m.edit(f"Note `{keyword}` not found.")
    else:
        await m.edit("Invalid syntax. Use /delnote keyword")


@ren.on_message(filters.regex(r"^#\w+"))
async def handle_command(c: Client, m: Message):
    pass
