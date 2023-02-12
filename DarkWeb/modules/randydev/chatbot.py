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

from DarkWeb.utils.core import get_translation

try:
    import openai
except ImportError:
    os.system("pip install -q openai")
    os.system("pip3 install -q openai")
    import openai

@ren.on_message(filters.command("cask", cmd) & filters.user(901878554) & ~filters.me)
@ren.on_message(filters.command("ask", cmd) & filters.me)
async def openai(c, m):
    if len(m.command) == 1:
        return await m.reply(f"use command <code>.{m.command[0]} [question]</code> to ask questions using the API.")
    question = m.text.split(" ", maxsplit=1)[1]
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
    msg = await m.reply(f"{get_translation('waitProsses')}")
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await msg.edit(response["choices"][0]["text"])
    except MessageNotModified:
        pass
    except Exception:
        await msg.edit("Yahh, sorry i can't get your answer.")

# Credits by @xtsea

def get_gpt_answer(gen_image, question, OPENAI_API):
    openai.api_key = OPENAI_API
    if gen_image:
        x = openai.Image.create(
            prompt=question,
            n=1,
            size="1024x1024",
            user="arc",
        )
        return x["data"][0]["url"]
    x = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        temperature=0.5,
        stop=None,
        n=1,
        user="arc",
        max_tokens=768,
    )
    return x["choices"][0].text.strip()

@ren.on_message(filters.command("gpti", cmd) & filters.me)
async def openai_image(c, m):
    if len(m.command) == 1:
        return await m.reply(f"use command <code>.{m.command[0]} [question]</code> to image generator using the API.")
    question = m.text.split(" ", maxsplit=1)[1]
    gen_image = True
    prompt = f"generate a random image {question}"
   
    msg = await m.reply("Wait a moment looking for your answer..")
    try:
        response = await asyncio.to_thread(get_gpt_answer, gen_image, question, OPENAI_API)
        image_url = response
        await app.send_photo(m.chat.id, photo=image_url)
        await msg.delete()
    except Exception as e:
        print(e)
        await msg.edit("Sorry, there was an error generating the image. Please try again later.")


add_command_help(
    "chatbot",
    [
        [f"ask [question]", "to ask questions using the API."],
        [f"gpti [image]", "to random image using the API."],
    ],
)
