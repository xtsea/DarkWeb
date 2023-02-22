# hacker by @xtsea
# copyright 2020 - 2023 : https://github.com/TeamKillerX/


import requests
import os
import json
import random
from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as ren 
from pyrogram.errors import MessageNotModified

from DarkWeb import *
from DarkWeb.helper.cmd import *
from DarkWeb.helper.what import *
from pykillerx.help import *
from config import OPENAI_API

@ren.on_message(filters.command("ask", cmd) & filters.me)
async def openai(c, m):
    question = (
        m.text.split(None, 1)[1]
        if len(
            m.command,
        )
        != 1
        else None
    )
    if not question:
       return await m.reply(f"use command <code>.{m.command[0]} [question]</code> to ask questions using the API.")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API}",
    }

    json_data = {
        "model": "text-davinci-003",
        "prompt": question,
        "max_tokens": 200,
        "temperature": 0,
    }
    msg = await m.reply(f"Wait a moment looking for your answer..")
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await msg.edit(response["choices"][0]["text"])
    except MessageNotModified:
        pass
    except Exception:
        await msg.edit("Yahh, sorry i can't get your answer.")

# Credits by @xtsea

add_command_help(
    "chatgpt",
    [
        [f"ask [question]", "to ask questions using the API."],
    ],
)
