from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "8111395645:AAFAK_RbM5FJcXPJZFq_pPZrNdLQ9-IVYag"
REGISTER_LINK = "https://jalwa.win/#//#/register?invitationCode=43658102035"

# Format message
def format_bet_message(period, bet):
    return (
        f"🎯 𝐏ᴇʀɪᴏᴅ 𝐍ᴜᴍ𝐛ᴇʀ: {period}\n\n"
        f"🔹 𝐁ᴇ𝐭 𝐎ɴ: {bet}\n\n"
        f"🔗 𝐑ᴇɢɪsᴛᴇʀ 𝐍ᴏᴡ:\n{REGISTER_LINK}"
    )

# Channel message handler
async def handle_channel_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()
    chat_id = update.effective_chat.id
    message_id = update.message.message_id

    if text.startswith("/b "):
        period = text.split("/b ", 1)[1].strip()
        msg = format_bet_message(period, "ʙɪɢ ✅")

    elif text.startswith("/s "):
        period = text.split("/s ", 1)[1].strip()
        msg = format_bet_message(period, "🔻 sᴍᴀʟʟ")

    elif text.startswith("/r "):
        period = text.split("/r ", 1)[1].strip()
        msg = format_bet_message(period, "ʀᴇᴅ 🟥")

    elif text.startswith("/g "):
        period = text.split("/g ", 1)[1].strip()
        msg = format_bet_message(period, "ɢʀᴇᴇɴ 🟩")

    elif text.startswith("/v "):
        period = text.split("/v ", 1)[1].strip()
        msg = format_bet_message(period, "ᴠɪᴏʟᴇᴛ 🟪")

    else:
        return

    try:
        # Delete user command message
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    except Exception as e:
        print("Failed to delete message:", e)

    # Send formatted message
    await context.bot.send_message(chat_id=chat_id, text=msg)

# Main runner
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ChatType.CHANNEL & filters.TEXT, handle_channel_command))
    print("Bot is running...")
    app.run_polling()
