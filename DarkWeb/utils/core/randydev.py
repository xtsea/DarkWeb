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

            try:
                if not TEMP_SETTINGS.get('ME'):
                    me = app.get_me()
                    TEMP_SETTINGS['ME'] = me

                    if me.id in GROUP:
                        raise RetardsException('RETARDS CANNOT USE THIS BOT')

                if message.service and not service:
                    return

                if message.service and isinstance(message.action, MessageActionContactSignUp):
                    return

                if message.chat.type == enums.ChatType.CHANNEL:
                    return

                if not bot and message.chat.type == enums.ChatType.BOT:
                    message.continue_propagation()

                if not private and message.chat.type in [
                    enums.ChatType.PRIVATE,
                    enums.ChatType.BOT,
                ]:
                    if not disable_notify:
                        edit(message, f'`{get_translation("groupUsage")}`')
                    message.continue_propagation()

                if not group and message.chat.type in [
                    enums.ChatType.SUPERGROUP,
                    enums.ChatType.GROUP,
                ]:
                    if not disable_notify:
                        edit(message, f'`{get_translation("privateUsage")}`')
                    message.continue_propagation()

                if admin and not is_admin(message):
                    if not disable_notify:
                        edit(message, f'`{get_translation("adminUsage")}`')
                    message.continue_propagation()

                if not compat:
                    func(client, message)
                else:
                    func(message)
            except RetardsException:
                try:
                    system(f'kill -9 {getpid()}')
                except BaseException:
                    pass
            except (ContinuePropagation, StopPropagation) as c:
                raise c
            except Exception as e:
                try:
                    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

                    if get_cmd(message) == 'crash':
                        text = get_translation('logidTest')
                    else:
                        if not disable_notify:
                            edit(message, f'`{get_translation("errorLogSend")}`')
                        text = get_translation(
                            'renErrorText', ['**', '`', exc_info()[1]]
                        )

                    ftext = get_translation(
                        'renErrorText2',
                        [
                            date,
                            message.chat.id,
                            message.from_user.id if message.from_user else 'Unknown',
                            BOT_VERSION,
                            message.text,
                            format_exc(),
                            exc_info()[1],
                        ],
                    )

                    process = Popen(
                        ['git', 'log', '--pretty=format:"%an: %s"', '-10'],
                        stdout=PIPE,
                        stderr=PIPE,
                    )
                    out, err = process.communicate()
                    out = f'{out.decode()}\n{err.decode()}'.strip()

                    ftext += out

                    file = open(get_translation('rbgLog'), 'w+')
                    file.write(ftext)
                    file.close()

                    send_log_doc(
                        get_translation('rbgLog'), caption=text, remove_file=True
                    )
                    raise e
                except Exception as x:
                    raise x

        filter = None
        if pattern:
            filter = filters.regex(pattern)
            if brain:
                filter &= filters.user(DEVS)
            if outgoing and not incoming:
                filter &= filters.me
            elif incoming and not outgoing:
                filter &= filters.incoming & ~filters.bot & ~filters.me
        else:
            if outgoing and not incoming:
                filter = filters.me
            elif incoming and not outgoing:
                filter = filters.incoming & ~filters.bot & ~filters.me
            else:
                filter = (filters.me | filters.incoming) & ~filters.bot

        if not disable_edited:
            app.add_handler(EditedMessageHandler(wrap, filter))
        app.add_handler(MessageHandler(wrap, filter))

    return msg_decorator


class RetardsException(Exception):
    pass
