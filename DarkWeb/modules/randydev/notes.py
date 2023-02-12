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
""""

# Copyright (C) 2020-2022 TeamDerUntergang <https://github.com/TeamDerUntergang>

from pyrogram import Client as ren 
from pyrogram.types import * 
from DarkWeb.helper.cmd import *
from pykillerx import *
from pykillerx.helper import *
from pykillerx.help import *
from DarkWeb import *
from config import *
from utils.core import (
    edit,
    extract_args,
    forward,
    get_messages,
    get_translation,
    reply_msg,
    randydev,
    send_log,
)


def notes_init():
    try:
        global sql
        from importlib import import_module
        sql = import_module('DarkWeb.database.SQL.notes_sql')
    except Exception as e:
        sql = None
        LOGS.warn(get_translation('notesSqlLog'))
        raise e


notes_init()


@randydev(pattern='^.notes$')
def notes(message):
    try:
        from DarkWeb.database.SQL.notes_sql import get_notes
    except AttributeError:
        edit(message, f'`{get_translation("nonSqlMode")}`')
        return
    reply = f'`{get_translation("noNote")}`'
    notesx = get_notes(message.chat.id)
    for note in notesx:
        if reply == f'`{get_translation("noNote")}`':
            reply = f'{get_translation("notesChats")}\n'
            reply += '`#{}`\n'.format(note.keyword)
        else:
            reply += '`#{}`\n'.format(note.keyword)
    edit(message, reply)


@randydev(pattern=r'^.save')
def save_note(message):
    try:
        from DarkWeb.database.SQL.notes_sql import add_note
    except AttributeError:
        edit(message, f'`{get_translation("nonSqlMode")}`')
        return
    args = extract_args(message, markdown=True).split(' ', 1)
    if len(args) < 1 or len(args[0]) < 1:
        edit(message, f'`{get_translation("wrongCommand")}`')
        return
    keyword = args[0]
    string = args[1] if len(args) > 1 else ''
    msg = message.reply_to_message
    msg_id = None

    if len(string) < 1:
        if msg:
            if msg.text:
                string = msg.text.markdown
            else:
                string = None
                msg_o = forward(msg, LOG_ID)
                if not msg_o:
                    edit(message, f'`{get_translation("noteError")}`')
                    return
                msg_id = msg_o.id
                send_log(get_translation('notesLog', ['`', message.chat.id, keyword]))
        else:
            edit(message, f'`{get_translation("wrongCommand")}`')

    if add_note(str(message.chat.id), keyword, string, msg_id) is False:
        edit(message, get_translation('notesUpdated', ['`', keyword]))
    else:
        edit(message, get_translation('notesAdded', ['`', keyword]))


@randydev(pattern=r'^.clear')
def clear_note(message):
    try:
        from DarkWeb.sql.notes_sql import rm_note
    except AttributeError:
        edit(message, f'`{get_translation("nonSqlMode")}`')
        return

    notename = extract_args(message)
    if rm_note(message.chat.id, notename) is False:
        edit(message, get_translation('notesNotFound', ['`', notename]))
    else:
        edit(message, get_translation('notesRemoved', ['**', '`', notename]))


def get_note(message):
    try:
        try:
            from DarkWeb.databass.SQL.notes_sql import get_note
        except BaseException:
            edit(message, f'`{get_translation("nonSqlMode")}`')
            return

        notename = extract_args(message).split()[0][1:]
        note = get_note(message.chat.id, notename)

        if note:
            if note.f_mesg_id:
                msg_o = get_messages(LOG_ID, msg_ids=int(note.f_mesg_id))
                if msg_o and len(msg_o) > 0 and not msg_o[-1].empty:
                    msg = msg_o[-1]
                    reply_msg(message, msg)
                else:
                    edit(message, f'`{get_translation("noteResult")}`')
            elif note.reply and len(note.reply) > 0:
                edit(message, note.reply)
            else:
                edit(message, f'`{get_translation("noteError2")}`')
        else:
            edit(message, f'`{get_translation("noteNoFound")}`')
    except BaseException:
        pass
