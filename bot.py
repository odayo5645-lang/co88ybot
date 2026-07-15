import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging to track bot errors in Railway
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hi! I am co88ybot. Send me any text message, and I will instantly copy and echo it back to you!"
    )

# Text copying handler
async def copy_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Safely extract the incoming message text
    user_text = update.message.text
    # Send the exact text back to the user
    await update.message.reply_text(user_text)

def main() -> None:
    # Retrieve the Token from Railway environment variables
    TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
    
    if not TOKEN:
        logger.error("Error: TELEGRAM_BOT_TOKEN environment variable not found!")
        return

    # Build the application using the token
    application = Application.builder().token(TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, copy_text))

    # Start the bot using polling method
    logger.info("co88ybot is starting...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
