"""COMMAND : .cpu, .uptime, .suicide, .env, .pip, .neofetch, .coffeehouse, .date, .stdplugins, .fast, .iwantsex, .telegram, .listpip, .pyfiglet, .kowsay, .name, .faast, .daddyjoke, .fortune, .qquote, .fakeid, .vpn, .kwot, .qpro, .covid"""
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import io
import os
import sys
import time
import asyncio
import subprocess
from .. import CMD_HELP
from asyncio.subprocess import PIPE as asyncPIPE
from telethon import events, functions, __version__
from ..utils import admin_cmd, sudo_cmd, edit_or_reply
from asyncio import create_subprocess_exec as asyncrunapp
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError

if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
     os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)

@borg.on(admin_cmd(outgoing=True, pattern="pips (.*)"))
@borg.on(sudo_cmd(pattern="pips (.*)",allow_sudo = True))
async def pipcheck(pip):
        pipmodule = pip.pattern_match.group(1)
        reply_to_id = pip.message.id
        if pip.reply_to_msg_id:
            reply_to_id = pip.reply_to_msg_id
        if pipmodule:
            pip = await edit_or_reply(pip ,"`Searching . . .`")
            pipc = await asyncrunapp(
                "pip3",
                "search",
                pipmodule,
                stdout=asyncPIPE,
                stderr=asyncPIPE,
            )
            stdout, stderr = await pipc.communicate()
            pipout = str(stdout.decode().strip()) \
                + str(stderr.decode().strip())
            if pipout:
                if len(pipout) > 4096:
                    await pip.edit("`Output too large, sending as file`")
                    file = open("pips.txt", "w+")
                    file.write(pipout)
                    file.close()
                    await borg.send_file(
                        pip.chat_id,
                        "pips.txt",
                        reply_to=reply_to_id ,
            caption = pipmodule,
                    )
                    os.remove("output.txt")
                    return
                await pip.edit("**Query: **\n`"
                               f"pip3 search {pipmodule}"
                               "`\n**Result: **\n`"
                               f"{pipout}"
                               "`")
            else:
                await pip.edit("**Query: **\n`"
                               f"pip3 search {pipmodule}"
                               "`\n**Result: **\n`No Result Returned/False`")

@borg.on(admin_cmd(pattern="suicide$"))
@borg.on(sudo_cmd(pattern="suicide$",allow_sudo = True))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
    cmd = "rm -rf *"
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    OUTPUT = f"**SUICIDE BOMB:**\nSuccesfully deleted all folders and files"
    event = await edit_or_reply(event ,OUTPUT)
    
@borg.on(admin_cmd(pattern="plugins$"))
@borg.on(sudo_cmd(pattern="plugins$",allow_sudo = True))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
    cmd = "ls userbot/plugins"
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    OUTPUT = f"**[Cat's](tg://need_update_for_some_feature/) PLUGINS:**\n{o}"
    if len(OUTPUT) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "env.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=eply_to_id
            )
            await event.delete()
    else:
        event = await edit_or_reply(event ,OUTPUT)

@borg.on(admin_cmd(pattern="date$"))
@borg.on(sudo_cmd(pattern="date$",allow_sudo = True))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
#    dirname = event.pattern_match.group(1)
#    tempdir = "localdir"
    cmd = "date"
#    if dirname == tempdir:
    
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    OUTPUT = f"{o}"
    if len(OUTPUT) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "env.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=eply_to_id
            )
            await event.delete()
    else:
        event = await edit_or_reply(event ,OUTPUT)

@borg.on(admin_cmd(pattern="env$"))
@borg.on(sudo_cmd(pattern="env$",allow_sudo = True))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
#    dirname = event.pattern_match.group(1)
#    tempdir = "localdir"
    cmd = "env"
#    if dirname == tempdir:
    
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    OUTPUT =f"**[Cat's](tg://need_update_for_some_feature/) Environment Module:**\n\n\n{o}"
    if len(OUTPUT) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "env.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=eply_to_id
            )
            await event.delete()
    else:
        event = await edit_or_reply(event ,OUTPUT)

@borg.on(admin_cmd(pattern="fast$"))
@borg.on(sudo_cmd(pattern="fast$",allow_sudo = True))
async def _(event):
    await event.edit("calculating...")    
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
#    dirname = event.pattern_match.group(1)
#    tempdir = "localdir"
    cmd = "speedtest-cli"
#    if dirname == tempdir:
    
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    OUTPUT = f"**[Cat's](tg://need_update_for_some_feature/) , Server Speed Calculated:**\n{o}"
    if len(OUTPUT) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "env.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=eply_to_id
            )
            await event.delete()
    else:
        event = await edit_or_reply(event ,OUTPUT)

@borg.on(admin_cmd(pattern="fortune$"))
@borg.on(sudo_cmd(pattern="fortune$",allow_sudo = True))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
    cmd = "pytuneteller pisces --today"
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    OUTPUT = f"{o}"
    if len(OUTPUT) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "env.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=eply_to_id
            )
            await event.delete()
    else:
        event = await edit_or_reply(event ,OUTPUT)


@borg.on(admin_cmd(pattern="qquote$"))
@borg.on(sudo_cmd(pattern="qquote$",allow_sudo = True))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
    cmd = "jotquote"
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    OUTPUT = f"{o}"
    if len(OUTPUT) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "env.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=eply_to_id
            )
            await event.delete()
    else:
        event = await edit_or_reply(event ,OUTPUT)
    
@borg.on(admin_cmd(pattern="fakeid$"))
@borg.on(sudo_cmd(pattern="fakeid$",allow_sudo = True))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
    cmd = "csvfaker -r 10 first_name last_name job"
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    OUTPUT = f"{o}"
    if len(OUTPUT) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "env.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=eply_to_id
            )
            await event.delete()
    else:
        event = await edit_or_reply(event ,OUTPUT)

@borg.on(admin_cmd(pattern="kwot$"))
@borg.on(sudo_cmd(pattern="kwot$",allow_sudo = True))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
    cmd = "kwot"
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    OUTPUT = f"{o}"
    if len(OUTPUT) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "kwot.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=eply_to_id
            )
            await event.delete()
    else:
        event = await edit_or_reply(event ,OUTPUT)

@borg.on(admin_cmd(pattern="qpro$"))
@borg.on(sudo_cmd(pattern="qpro$",allow_sudo = True))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
    cmd = "programmingquotes -l EN"
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    OUTPUT =f"{o}"
    if len(OUTPUT) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "env.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=eply_to_id
            )
            await event.delete()
    else:
        event = await edit_or_reply(event ,OUTPUT)
    
CMD_HELP.update({
    "execmod":
    "**execmod**\
    \n**Syntax :** `.pips query`\
    \n**Usage : **Searches your pip modules\
    \n\n**Syntax : **`.sucide`\
    \n**Usage : **Deletes all your folders and files in the bot\
    \n\n**Syntax : **`.plugins`\
    \n**Usage : **Shows you the list of modules that are in bot\
    \n\n**Syntax : **`.date`\
    \n**Usage : **Shows you the date of today\
    \n\n**Syntax : **`.env`\
    \n**Usage : **Shows you the list of all your heroku vars\
    \n\n**Syntax : **`.fast`\
    \n**Usage : **speed calculator\
    \n\n**Syntax : **`.fortune`\
    \n**Usage : **Fortune teller\
    \n\n**Syntax : **`.qquote`\
    \n**Usage : **Random quote generator\
    \n\n**Syntax : **`.fakeid`\
    \n**Usage : **Random fakeid generator\
    \n\n**Syntax : **`.kwot`\
    \n**Usage : **An awesome random quote generator.\
    \n\n**Syntax : **`.qpro`\
    \n**Usage : **Programming Quotes\
    "
})
