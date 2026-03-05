class Translation(object):
    START_TEXT = """<b>👋 Hello there!</b>
    
I am an advanced <b>All-In-One Telegram Bot</b> capable of performing various tasks like downloading media, renaming files, and more!
    
💡 <i>Click the <b>/help</b> button to see everything I can do.</i>
    
👨‍💻 <b>Made with ❤️ by @TeleRoidGroup</b>"""

    RENAME_403_ERR = "🚫 <b>Sorry, you are not permitted to rename this file.</b>\n<i>Please ask in our <a href='https://t.me/TeleRoid14'>Support Group</a> for assistance.</i>"
    ABS_TEXT = " ⚠️ <b>Please don't be selfish.</b>"
    UPGRADE_TEXT = "🌟 <b>This Bot is free to use for our community!</b>\n\nJoin <b>@TeleRoidGroup</b> for updates and premium features."
    FORMAT_SELECTION = "🎬 <b>Select the desired format for download:</b>"
    
    SET_CUSTOM_USERNAME_PASSWORD = """🔐 <b>If you want to download premium videos, provide credentials in this format:</b>
👉 <code>URL | filename | username | password</code>"""
    
    NOYES_URL = "🐢 <b>Whoa, this is a very slow link!</b>\n<i>Please provide a faster link so I can efficiently upload it without wasting time.</i>"
    
    DOWNLOAD_START = "📥 <b>Downloading your files... Please wait.</b>"
    UPLOAD_START = "📤 <b>Uploading your files... Almost there!</b>"
    
    RCHD_BOT_API_LIMIT ="⚠️ <b>File size exceeds maximum allowed size.</b> <i>Attempting to upload anyway...</i>"
    RCHD_TG_API_LIMIT = "⚡️ <b>Downloaded in:</b> {} seconds.\n📊 <b>Detected File Size:</b> {}\n\n🛑 <b>Error:</b> <i>I cannot upload files larger than 2GB due to Telegram API limitations.</i>"
    
    AFTER_SUCCESSFUL_UPLOAD_MSG = "✅ <b>File Uploaded Successfully!</b>"
    DOWNLOAD_SUCCESS_UPLOAD_START_GDRIVE = "🌩 <b>Download Completed!</b>\n⏳ <b>Upload to Cloud in progress...</b>"
    
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "⏱ <b>Downloaded in:</b> {} seconds.\n⏱ <b>Uploaded in:</b> {} seconds."
    
    NOT_AUTH_USER_TEXT = "🛑 <b>Access Denied.</b>\n<i>This command is restricted to Admins only.</i>"
    NOT_AUTH_USER_TEXT_FILE_SIZE = "📊 <b>Detected File Size:</b> {}\n🆓 <b>Free Users Limit:</b> {}\n\n⭐ <i>Please <b>/upgrade</b> your subscription to process this file.</i>"
    
    SAVED_CUSTOM_THUMB_NAIL = "🖼 <b>Custom thumbnail saved successfully!</b>\n<i>This image will be used for your uploaded media.</i>"
    DEL_ETED_CUSTOM_THUMB_NAIL = "🗑 <b>Custom thumbnail cleared successfully.</b>"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "🗑 <b>Media cleared successfully from my storage.</b>"
    
    SAVED_RECVD_DOC_FILE = "📄 <b>Document downloaded successfully.</b>"
    CUSTOM_CAPTION_UL_FILE = "\n\n🤖 <b>Bot created by:</b> 👉 <b>@TeleRoidGroup</b>"
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "⚠️ <b>No Custom Thumbnail found.</b>"
    NO_VOID_FORMAT_FOUND = "❌ <b>Unable to detect the video format!</b>\n<i>Please check the URL. If you think this is a bug, kindly report it in <a href='https://t.me/TeleRoid14'>TeleRoid Support</a>.</i>\n\n<b>Error:</b> {}"
    
    USER_ADDED_TO_DB = "👤 User <a href='tg://user?id={}'>{}</a> added to <b>{}</b> until <b>{}</b>."
    
    CURENT_PLAN_DETAILS = """
┏━━━━━━━━━━━━━━━━━━━
┣ 👤 <b>Telegram ID:</b> <code>{}</code>
┣ 📝 <b>Plan Name:</b> {}
┣ 🚸 <b>Expires On:</b> {}
┗━━━━━━━━━━━━━━━━━━━
    
🌟 <i>Need a private bot? Check out @OwnYourBotz.</i>"""
    
    HELP_USER = """✨ <b>Here's everything I can do for you:</b>

┏━━━━━━━━━━━━━━━━━━━
┣ 🎥 <b>Supported Media:</b> Natively supports [YTDLp]
┣ 🔗 <b>Direct Link:</b> Upload files from any direct link
┣ 🔄 <b>Convert:</b> Reply <code>/converttovideo</code> to media
┣ ✏️ <b>Rename:</b> Reply <code>/rename NewName.ext</code> to file
┣ ⚡️ <b>Get Links:</b> Reply <code>/getlink</code> for direct URL
┗━━━━━━━━━━━━━━━━━━━

💡 <i>Send <code>/me</code> to check your current plan details.</i>"""

    REPLY_TO_DOC_GET_LINK = "🔗 <b>Please reply to a Telegram media file to generate a high-speed direct download link.</b>"
    REPLY_TO_DOC_FOR_C2V = "🔄 <b>Please reply to a Telegram media file to convert it to video.</b>\n👉 <i>@TeleRoidGroup</i>"
    REPLY_TO_DOC_FOR_SCSS = "📸 <b>Please reply to a Telegram media file to generate screenshots.</b>\n👉 <i>@TeleRoidGroup</i>"
    
    SOURCE = """ℹ️ <b>About Me:</b>
━━━━━━━━━━━━━━━━━━━━
🤖 <b>Name:</b> <i>TeleRoid AnyDLBot</i>
👨‍💻 <b>Creator:</b> <a href='https://telegram.dog/TeleRoidGroup'>This Person</a>
🧛‍♂️ <b>Credits:</b> <i>Everyone in this journey</i>
📝 <b>Language:</b> <i>Python 3.13</i>
📚 <b>Library:</b> <i>PyroTGFork Asyncio</i>
🗂 <b>Cloned From:</b> <i>AnyDLBot [Spechide]</i>
🔗 <b>Source Code:</b> <a href="https://github.com/PredatorHackerzZ/AnyDLBot-2">Click Here</a>
📡 <b>Server:</b> <a href='https.heroku.com'>VPS</a>
💡 <b>Build Status:</b> <i>Premium v2026</i>
━━━━━━━━━━━━━━━━━━━━"""
    
    REPLY_TO_DOC_FOR_RENAME_FILE = "✏️ <b>Please reply to a Telegram media file to rename it.</b>\n<i>You can also use custom thumbnails! Check the support group for help.</i>"
    
    AFTER_GET_DL_LINK = "🔗 <b>High-Speed Direct Link:</b> <a href='{}'>Download Here</a>\n⏳ <i>Valid for <b>{}</b> days.</i>"
    
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """✂️ <b>Syntax:</b> <code>/trim HH:MM:SS [HH:MM:SS]</code>"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "📥 <b>First, send <code>/downloadmedia</code> in reply to the media so I can save it locally.</b>\n<i>Then, send <code>/storageinfo</code> to check the downloaded media.</i>"
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "🎞 <b>Video Duration:</b> {}\n\n🗑 <b>Send:</b> <code>/clearffmpegmedia</code> to delete it.\n✂️ <b>Send:</b> <code>/trim HH:MM:SS [HH:MM:SS]</code> to trim it."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ <b>A saved media file already exists!</b>\n<i>Please send <code>/storageinfo</code> to check its details.</i>"
    
    USER_DELETED_FROM_DB = "🗑 User <a href='tg://user?id={}'>{}</a> was successfully deleted from the database."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "📦 <b>Please reply to an MKV file to extract its embedded streams.</b>"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "🖼 <b>Please reply with <code>/generatecustomthumbnail</code> to an album of two photos.</b>"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "⚠️ <b>Error: The media album must contain EXACTLY two photos!</b>\n<i>Please recreate the album and try again.</i>"
    
    INVALID_UPLOAD_BOT_URL_FORMAT = "❌ <b>Invalid URL format!</b>\n<i>Make sure the URL starts with <code>http://</code> or <code>https://</code>.</i>\n\n💡 <b>Tip:</b> <i>You can set a custom filename like this:</i>\n👉 <code>URL | filename.extension</code>"
    ABUSIVE_USERS = "🚫 <b>You are restricted from using this bot!</b>\n<i>If you believe this is a mistake, use <code>/me</code> to review your restrictions.</i>"
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "Holy Shit!!"
    EXTRACT_ZIP_INTRO_ONE = "🗜 <b>First, send the compressed file. Then, reply to it with <code>/unzip</code>.</b>"
    EXTRACT_ZIP_INTRO_THREE = "🔍 <b>Analyzing the compressed file...</b>\n⚠️ <i>This might take some time depending on the file size. Please be patient.</i> "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "❌ <b>Sorry, an error occurred while processing the compressed file.</b>\n<i>Please verify the file and try again.</i>"
    EXTRACT_ZIP_STEP_TWO = """📂 <b>Select a file to extract and upload from the options below.</b>
💡 <i>Tip: You can use the <code>/rename</code> command after receiving the file!</i>"""
    CANCEL_STR = "❌ <b>Process Cancelled.</b>"
    ZIP_UPLOADED_STR = "✅ <b>Uploaded {} file(s) in {} seconds.</b>"
    FREE_USER_LIMIT_Q_SZE = """⏳ <b>Limit Exceeded!</b>
<i>Free users can only make 1 request every 5 minutes.</i>
👉 <b>/upgrade</b> your plan or try again in 300 seconds."""
    SLOW_URL_DECED = "🐢 <b>This URL is extremely slow!</b>\n<i>Downloading it will negatively impact other users. Please provide a faster link.</i>"
    IFLONG_FILE_NAME = """📝 <b>File Name Too Long!</b>
Allowed limit by Telegram: <b>{alimit}</b> characters.
Your file name: <b>{num}</b> characters.

❌ <b>Please shorten your file name and try again.</b>"""
