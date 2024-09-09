from pyrogram import filters
from AkhandanandTripathi import app
from AkhandanandTripathi.core import script
from AkhandanandTripathi.core.func import subscribe
from config import OWNER_ID
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# ------------------- Start-Buttons ------------------- #

buttons = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Join Channel", url="https://t.me/AkhandanandTripathi")],
        [InlineKeyboardButton("Buy Premium", url="https://t.me/Scifiraj")]
    ]
)

@app.on_message(filters.command("start"))
async def start(_, message):
    join = await subscribe(_, message)
    if join == 1:
        return
    await message.reply_photo(photo="https://graph.org/file/e02fcc6bbfa0a882d6c8b.jpg",
                              caption=script.START_TXT.format(message.from_user.mention), 
                              reply_markup=buttons)
