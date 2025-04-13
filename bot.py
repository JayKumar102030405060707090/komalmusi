async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    first = user.first_name or ""
    last = user.last_name or ""
    full_name = (first + " " + last).strip()
    mention = f"[{full_name}](tg://user?id={user.id})"

    text = (
        f"✦ » ʜᴇʏ {mention} !\n"
        f"✦ ɪ'ᴍ ʏᴏᴜʀ ᴘʀᴇᴅᴜᴄᴛɪᴏɴ ʙᴏᴛ !!\n\n"
        f"◆ ɪ'ᴍ ʀᴇᴀᴄᴛ ᴛᴏ ᴇᴠᴇʀʏ ᴍᴇssᴀɢᴇ ɪɴ ɢʀᴏᴜᴘs, ᴄʜᴀɴɴᴇʟs, ᴀɴᴅ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛs ᴡɪᴛʜ ᴀ ʀᴀɴᴅᴏᴍ ᴇᴍᴏᴊɪ..!!\n\n"
        f"✦ 𝖶ɪᴛʜ sᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.\n\n"
        f"✦ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ [ɴᴏᴛᴛʏ ʙᴀʙʏ](tg://user?id=7168729089)"
    )

    keyboard = [
        [InlineKeyboardButton("➕ ADD ME BABY ➕", url="https://t.me/GaandMusicBot?startgroup=true")],
        [
            InlineKeyboardButton("≛ Support ≛", url="https://t.me/sureshot101game"),
            InlineKeyboardButton("≛ Updates ≛", url="https://t.me/Jalwagame_Hack")
        ],
        [InlineKeyboardButton("≛ Help and Commands ≛", callback_data="help")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo="https://telegra.ph/file/fed49767152996377c237.jpg",
        caption=text,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )
