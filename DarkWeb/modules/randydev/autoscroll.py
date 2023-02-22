from pyrogram import *
from pyrogram.types *
from pyrogram import Client as ren

from DarkWeb.helper.cmd import *
from pykillerx.help import *

the_regex = r"^r\/([^\s\/])+"

f = filters.chat([])

if f:
   @ren.on_message(f)
   async def auto_read(bot: Client, message: Message):
       await bot.read_history(message.chat.id)
       message.continue_propagation()


@ren.on_message(filters.command("autoscroll", cmd) & filters.me)
async def add_to_auto_read(bot: Client, message: Message):
    if message.chat.id in f:
        f.remove(message.chat.id)
        await message.edit("Autoscroll deactivated")
    else:
        f.add(message.chat.id)
        await message.edit("Autoscroll activated")


add_command_help(
    "autoscroll",
    [
        [
            ".autoscroll",
            "Send .autoscroll in any chat to automatically read all sent messages until you call "
            "autoscroll again. This is useful if you have Telegram open on another screen.",
        ],
    ],
)
