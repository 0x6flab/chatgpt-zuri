import logging
import os
import openai

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}."
        f"To view the {TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import ForceReply, Update
from telegram.ext import (
    Application, CommandHandler, ContextTypes, MessageHandler, filters
)

openai.api_key = os.environ['ZURI_OPENAI_API_KEY']

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(name="telegram-chatgpt-zuri")

# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    with open("messages/start.txt", "r") as f:
        message = f.read()
    print(user)
    logger.info(
        f'''User {user.first_name} with id {user.id}
        started the conversation.'''
    )
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!{message}",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    with open("messages/help.txt", "r") as f:
        message = f.read()
    await update.message.reply_text(message)


async def stop_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    with open("messages/stop.txt", "r") as f:
        message = f.read()
    await update.message.reply_text(message)


async def chat_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    # Use the OpenAI API to generate a response to the user's message
    with open("messages/prompt.txt", "r") as f:
        prompt = f.read()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": update.message.text}
        ],
        max_tokens=256,
        n=1,
        stop=None,
        temperature=0.7,
    )
    logger.info(
        f'''User {update.effective_user.first_name} with id 
        {update.effective_user.id}
        started the conversation.'''
    )
    await update.message.reply_text(
        response.choices[0].message.content,
        reply_markup=ForceReply(selective=True)
    )


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(os.environ['ZURI_TELEGRAM_TOKEN']).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("stop", stop_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, chat_command)
    )

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
