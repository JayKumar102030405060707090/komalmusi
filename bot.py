from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Bot token and register link
TOKEN = "8111395645:AAGc-_RSqzfBYQ4PAOxuizu5dnxZ4we6TQ0"
REGISTER_LINK = "https://jalwa.win/#//#/register?invitationCode=43658102035"
BOT_IMAGE_URL = "https://telegra.ph/file/fed49767152996377c237.jpg"

# Format betting message
def format_bet_message(period, bet):
    return (
        f"🎯 𝐏ᴇʀɪᴏ𝐝 𝐍ᴜᴍ𝐛ᴇʀ: {period}\n\n"
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
        await update.message.reply_text("❌ Period number dena padega!\nExample: /big 123456")
        return

    period = context.args[0]
    message = format_bet_message(period, bet_text)

    try:
        await update.message.delete()
    except:
        pass

    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# Bet commands
async def big(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_bet(update, context, "ʙɪɢ ✅")

async def small(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_bet(update, context, "🔻 sᴍᴀʟʟ")

async def red(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_bet(update, context, "ʀᴇᴅ 🟥")

async def green(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_bet(update, context, "ɢʀᴇᴇɴ 🟩")

async def violet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_bet(update, context, "ᴠɪᴏʟᴇᴛ 🟪")

# Start the bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("b", b))
    app.add_handler(CommandHandler("s", s))
    app.add_handler(CommandHandler("r", r))
    app.add_handler(CommandHandler("g", g))
    app.add_handler(CommandHandler("v", v))

    print("Bot is running...")
    app.run_polling()
