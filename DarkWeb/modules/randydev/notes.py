# Copyright (C) 2020-2022 TeamDerUntergang <https://github.com/TeamDerUntergang>

from pyrogram.types import * 
from pyrogram import Client as ren
from DarkWeb.helper.cmd import *
from pykillerx import *
from pykillerx.helper import *
from pykillerx.help import *
from DarkWeb import *
from config import *

from DarkWeb.utils.core import (
    edit,
    extract_args,
    forward,
    get_messages,
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
        LOGS.warn("Warning database SQL")
        raise e


notes_init()


@ren.on_message(filters.command("notes", cmd) & filters.me)
async def notes(c: Client, m: Message):
    try:
        from DarkWeb.database.SQL.notes_sql import get_notes
    except AttributeError:
        await edit_or_reply(m.chat.id, f"Running on Non-SQL mode!")
        return
    reply = f"No notes found in this chat"
    notesx = get_notes(m.chat.id)
    for note in notesx:
        if reply == f"No notes found in this chat":
            reply = f"Notes saved in this chat\n"
            reply += '`#{}`\n'.format(note.keyword)
        else:
            reply += '`#{}`\n'.format(note.keyword)
    await edit_or_reply(m.chat.id, reply)


@ren.on_message(filters.command("save", cmd) & filters.me)
async def save_note(c: Client, m: Message):
    try:
        from DarkWeb.database.SQL.notes_sql import add_note
    except AttributeError:
        await edit_or_reply(m.chat.id, f"Running on Non-SQL mode!")
        return
    args = extract_args(m, markdown=True).split(' ', 1)
    if len(args) < 1 or len(args[0]) < 1:
        await edit_or_reply(m.chat.id, f"Command usage is wrong")
        return
    keyword = args[0]
    string = args[1] if len(args) > 1 else ''
    msg = m.reply_to_message
    msg_id = None

    if len(string) < 1:
        if msg:
            if msg.text:
                string = msg.text.markdown
            else:
                string = None
                msg_o = forward(msg, LOG_ID)
                if not msg_o:
                    await edit_or_reply(m.chat.id, f"Message couldn't be forwarded and note couldn't be added.")
                    return
                msg_id = msg_o.id
                send_log(f"#NOTE\nChat ID: %1%2%1\nNote: #%1%3%1\n\nAbove message saved for reply note, please don't delete!", ['`', m.chat.id, keyword])
        else:
            await edit_or_reply(m.chat.id, f"Message couldn't be forwarded and note couldn't be added.")

    if add_note(str(m.chat.id), keyword, string, msg_id) is False:
        await edit_or_reply(m.chat.id, f"%1Note successfully added. You can call the note with .call #%2%1", ['`', keyword])
    else:
        await edit_or_reply(m.chat.id, f"%1Note successfully added. You can call the note with .call #%2%1", ['`', keyword])


@ren.on_message(filters.command("clear", cmd) & filters.me)
async def clear_note(c: Client, m: Message):
    try:
        from DarkWeb.database.SQL.notes_sql import rm_note
    except AttributeError:
        edit(message, f"Running on Non-SQL mode!")
        return

    notename = extract_args(m)
    if rm_note(m.chat.id, notename) is False:
        await edit_or_reply(m.chat.id, f"Note not found!", ['`', notename])
    else:
        await edit_or_reply(m.chat.id, f"%2Note%2 #%1%3%1 %2removed%2", ['**', '`', notename])


async def get_note(c: Client, m: Message):
    try:
        try:
            from DarkWeb.databass.SQL.notes_sql import get_note
        except BaseException:
            await edit_or_reply(m.chat.id, f"Running on Non-SQL mode!")
            return

        notename = extract_args(m).split()[0][1:]
        note = get_note(m.chat.id, notename)

        if note:
            if note.f_mesg_id:
                msg_o = get_messages(LOG_ID, msg_ids=int(note.f_mesg_id))
                if msg_o and len(msg_o) > 0 and not msg_o[-1].empty:
                    msg = msg_o[-1]
                    reply_msg(m, msg)
                else:
                    await edit_or_reply(m.chat.id, f"Note result not found!")
            elif note.reply and len(note.reply) > 0:
                edit(message, note.reply)
            else:
                await edit_or_reply(m.chat.id, f"There was a problem fetching the note!")
        else:
            await edit_or_reply(m.chat.id, f"Note not found!")
    except BaseException:
        pass
