from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Bot token and register link
TOKEN = "8111395645:AAGc-_RSqzfBYQ4PAOxuizu5dnxZ4we6TQ0"
REGISTER_LINK = "https://jalwa.win/#//#/register?invitationCode=43658102035"

def format_bet_message(period, bet):
    return (
        f"🎯 𝐏ᴇʀɪᴏ𝐝 𝐍ᴜ𝐦𝐛ᴇ𝐫: {period}\n\n"
        f"🔹 𝐁ᴇ𝐭 𝐎ɴ: {bet}\n\n"
        f"🔗 𝐑ᴇɢɪsᴛᴇʀ 𝐍ᴏ𝐰:\n {REGISTER_LINK}"
    )

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

async def big(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_bet(update, context, "✅ BIG")

async def small(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_bet(update, context, "🔻 SMALL")

async def red(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_bet(update, context, "🟥 RED")

async def green(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_bet(update, context, "🟩 GREEN")

async def violet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_bet(update, context, "🟪 VIOLET")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("big", big))
    app.add_handler(CommandHandler("small", small))
    app.add_handler(CommandHandler("red", red))
    app.add_handler(CommandHandler("green", green))
    app.add_handler(CommandHandler("violet", violet))
    print("Bot is running...")
    app.run_polling()
