#(Β©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>β π²ππ΄π°ππΎπ : <a href='tg://user?id={1942517921}'>π³ππΎπ½πΎ</a>\nβ π»π°π½πΆππ°πΆπ΄ : <code>πΏπππ·πΎπ½3</code>\nβ π»πΈπ±ππ°ππ : <a href='https://docs.pyrogram.org/'>πΏπππΎπΆππ°πΌ π°πππ½π²πΈπΎ {__version__}</a>\nβ ππΎπππ²π΄ π²πΎπ³π΄ : <a href='https://github.com/skdrono05/FileSharingBot'>π²π»πΈπ²πΊ π·π΄ππ΄</a>\nβ π²π·π°π½π½π΄π» : <a href='https://t.me/+QoCiOv4LptpkYzM1'>πΉπΎπΈπ½ π»πΈπ½πΊ</a>\nβ πΆππΎππΏ : <a href='https://t.me/MovieShowGroup'>πΉπΎπΈπ½ π»πΈπ½πΊ</a>\n",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("π π²πΎπ»ππ΄", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
