from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Bot token and register link
TOKEN = "8111395645:AAGc-_RSqzfBYQ4PAOxuizu5dnxZ4we6TQ0"
REGISTER_LINK = "https://jalwa.win/#//#/register?invitationCode=43658102035"
BOT_IMAGE_URL = "https://telegra.ph/file/fed49767152996377c237.jpg"

# Sticker ID to send on /win and /w
STICKER_ID = "CAACAgUAAxkBAAEEiN5lZVmmR-cIhNUp5PXz6zAo7P8W3gACpQMAAiVloFXoW5abHq9B4zQE"  # Replace with your own if needed

# Format betting message
def format_bet_message(period, bet):
    return (
        f"🎯 𝐏ᴇʀɪᴏᴅ 𝐍ᴜᴍ𝐛ᴇʀ: {period}\n\n"
        f"🔹 𝐁ᴇ𝐭 𝐎ɴ: {bet}\n\n"
        f"🔗 𝐑ᴇɢɪsᴛᴇʀ 𝐍ᴏᴡ:\n{REGISTER_LINK}"
    )

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    full_name = f"{user.first_name or ''} {user.last_name or ''}".strip()
    user_link = f"<a href='tg://user?id={user.id}'>{full_name}</a>"

    caption = (
        f"✦ » ʜᴇʏ {user_link}\n"
        f"✦ ɪ'ᴍ ʏᴏᴜʀ ᴘʀᴇᴅᴜᴄᴛɪᴏɴ ʙᴏᴛ !!\n\n"
        f"◆ ɪ'ᴍ ʀᴇᴀᴄᴛ ᴛᴏ ᴇᴠᴇʀʏ ᴍᴇssᴀɢᴇ ɪɴ ɢʀᴏᴜᴘs, ᴄʜᴀɴɴᴇʟs, ᴀɴᴅ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛs ᴡɪᴛʜ ᴀ ʀᴀɴᴅᴏᴍ ᴇᴍᴏᴊɪ..!!\n\n"
        f"✦ 𝖶ɪᴛʜ sᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.\n\n"
        f"✦ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ <a href='tg://user?id=7168729089'>ɴᴏᴛᴛʏ ʙᴀʙʏ</a>"
    )

    keyboard = [
        [InlineKeyboardButton("➕ Add Me Baby ➕", url=f"https://t.me/{context.bot.username}?startgroup=true")],
        [
            InlineKeyboardButton("≛ Support ≛", url="https://t.me/Jalwagame_Hack"),
            InlineKeyboardButton("≛ Updates ≛", url="https://t.me/sureshot101game")
        ],
        [InlineKeyboardButton("≛ Help and Commands ≛", callback_data="help")]
    ]

    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=BOT_IMAGE_URL,
        caption=caption,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.HTML
    )

# Betting message sender
async def send_bet(update: Update, context: ContextTypes.DEFAULT_TYPE, bet_text: str):
    if not context.args:
        await update.message.reply_text("❌ Period number dena padega!\nExample: /b 123456")
        return

    period = context.args[0]
    message = format_bet_message(period, bet_text)

    try:
        await update.message.delete()
    except:
        pass

    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# Bet commands
async def b(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_bet(update, context, "ʙɪɢ ✅")

async def s(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_bet(update, context, "🔻 sᴍᴀʟʟ")

async def r(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_bet(update, context, "ʀᴇᴅ 🟥")

async def g(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_bet(update, context, "ɢʀᴇᴇɴ 🟩")

async def v(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_bet(update, context, "ᴠɪᴏʟᴇᴛ 🟪")

# Win sticker command
async def win(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=STICKER_ID)

# Start the bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("b", b))
    app.add_handler(CommandHandler("s", s))
    app.add_handler(CommandHandler("r", r))
    app.add_handler(CommandHandler("g", g))
    app.add_handler(CommandHandler("v", v))
    app.add_handler(CommandHandler(["win", "w"], win))

    print("Bot is running...")
    app.run_polling()
