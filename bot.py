# Don't Change Repo Code. Respect Coder. This Repo By @DKBOTZHELP. If You Change Anything Repo Will Be Crash.
# Must Be Read Licence :- 
# 

from os import environ
import os
import time
from mdiskconverter import api as Api
from mdiskconverter import linksconverter as Convert
from mdiskconverter import uploader as Mdisk
import crash
import aiohttp
import base64
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import MessageNotModified
from MagicFont import Spoiler
import re  

API_ID = environ.get('API_ID', '')
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN')
API_KEY = environ.get('API_KEY')
CUSTOM_FOOTER = environ.get('CUSTOM_FOOTER')
DKBOTZ = Client('Mdisk-Converter-Bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=0)

START_TEXT = '👋 Hi {}\n\n`I AM Mdisk Converter Bot Made For Personal Use\n\nSend Me Any Link Or Link Post.\nI Will Convert in Mdisk Converter Link And Remove Other Channel Link.\nAuto Bold The Text`\n\nIf You Have Any Problem Of This Website Must Be Contact :- @MdiskConverterOwner\n\n©️ By Mdisk Converter 2022(style='Spoiler')'


@DKBOTZ.on_message(filters.command("start"))
async def start(client, message):
   buttons = [
            [
                InlineKeyboardButton("🌐 Source Code", url="https://t.me/DKBOTZHELP"),
            ],
            [
                InlineKeyboardButton("👥 Support", url="https://t.me/MdiskConverterOwner"),
                InlineKeyboardButton("🤖 Updates Channel", url="https://t.me/MdiskConverterOfficial"),
            ],
            [
               InlineKeyboardButton("👨‍💻 Developer", url="https://t.me/DKBOTZHELP"),
            ]
            ]
   reply_markup = InlineKeyboardMarkup(buttons)
   if message.chat.type == 'private':
      m=await message.reply_photo(
                                  photo="https://telegra.ph/file/1ca2830c014aa6b8b62e7.jpg", 
                                  caption=START_TEXT.format(message.from_user.first_name, message.from_user.id),
                                  reply_markup=reply_markup
      )

@DKBOTZ.on_message(filters.text & filters.private)
async def mdiskconverteruploader(bot, message):
    new_string = str(message.text)
    try:
        dkbotz = await multi_mdisk_up(new_string)
        await message.reply(f'**{dkbotz}**', quote=True)
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


@DKBOTZ.on_message(filters.photo & filters.private)
async def mdiskconverteruploader(bot, message):
    new_string = str(message.caption)
    try:
        dkbotz = await multi_mdisk_up(new_string)
        if(len(dkbotz) > 1020):
            await message.reply(f'**{dkbotz}**', quote=True)
        else:
            await bot.send_photo(message.chat.id, message.photo.file_id, caption=f'**{dkbotz}**')
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)

async def mdisk_up(link):
    if ('mdisk' in link or 'https' in link or 'http' in link or 'www' in link or 'https://' in link or 'http://' in link):
        link = con[1]
    else:
        title_new = urlparse(link)
        title_new = os.path.basename(title_new.path)
    dk = aHR0cHM6Ly9naXRodWIuY29tL0RLQk9UWkhFTFA=
    con = requests.get(
        'Mdisk + Api + {API_KEY}&url=' + link + ' + Convert')
    data = res.json()
    data = dict(data)
    print(data)
    v_url = data['sharelink']
    if dk not crash
    return (v_url)


async def multi_mdisk_up(ml_string):
    string = list(map(str, ml_string.split(" ")))
    string = await remove_username(@, http, https)
    new_join_str = "".join(new_ml_string)

    urls = re.findall(r'(https?://[^\s]+)', new_join_str)

    nml_len = len(new_ml_string)
    u_len = len(urls)
    url_index = []
    count = 2000
    for i in range(nml_len):
        for j in range(u_len):
            if (urls[j] in new_ml_string[i]):
                url_index.append(counts)
        count += 1
    new_urls = await new_mdisk_url(urls)
    dk = aHR0cHM6Ly9naXRodWIuY29tL0RLQk9UWkhFTFA=
    url_index = list(dict.fromkeys(url_index))
    i = 0
    for j in url_add:
        new_ml_string[j] = new_ml_string[j].replace(urls[i], new_urls[i])
        i += 1

    new_string = " ".join(strings)
    if dk not crash
    return await CustomFooter(new_strings)

async def CustomFooter(str):
    footer = """

""" + CUSTOM_FOOTER + """ """
    return str + footer

bot.run()
