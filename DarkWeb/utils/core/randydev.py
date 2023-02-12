# Copyright (C) 2020-2022 TeamDerUntergang <https://github.com/TeamDerUntergang>
#
# This file is part of TeamDerUntergang project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

from os import getpid, system
from subprocess import PIPE, Popen
from sys import exc_info
from time import gmtime, strftime
from traceback import format_exc

from pyrogram import ContinuePropagation, StopPropagation, enums, filters
from pyrogram.handlers import MessageHandler, EditedMessageHandler
from pyrogram.raw.types import MessageActionContactSignUp
from DarkWeb import *
from pykillerx.blacklist import *

def randydev(**args):
    pattern = args.get('pattern', None)
    outgoing = args.get('outgoing', True)
    incoming = args.get('incoming', False)
    disable_edited = args.get('disable_edited', False)
    disable_notify = args.get('disable_notify', False)
    compat = args.get('compat', True)
    brain = args.get('brain', False)
    private = args.get('private', True)
    group = args.get('group', True)
    bot = args.get('bot', True)
    service = args.get('service', False)
    admin = args.get('admin', False)

    if pattern and '.' in pattern[:2]:
        args['pattern'] = pattern = pattern.replace('.', '^', 1)

    if pattern and pattern[-1:] != '$':
        args['pattern'] = pattern = f'{pattern}(?: |$)'

    def msg_decorator(func):
        def wrap(client, message):
            if message.empty or not message.from_user:
                return
