import logging

import aiohttp
from telegram import __version__ as TG_VER

from heckin_chonker_bot.config import (
    OPENAI_API_KEY,
    OPENAI_API_URL,
    TELEGRAM_BOT_API_KEY,
)

try:
    from telegram import __version_info__

except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


async def request(text):
    async with aiohttp.ClientSession() as session:
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": text}],
        }
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json",
        }
        async with session.post(
            url=OPENAI_API_URL, json=data, headers=headers
        ) as response:
            json = await response.json()

        return json.get("choices", {})[0].get("message", {}).get("content", {})


async def chonk_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /chonk is issued."""

    raw_message = update.message.text.strip("/chonk ")
    response = await request(raw_message)

    await update.message.reply_text(f"{response}")


def main() -> None:
    """Start the bot."""
    application = Application.builder().token(TELEGRAM_BOT_API_KEY).build()

    application.add_handler(CommandHandler("chonk", chonk_command))

    application.run_polling()


if __name__ == "__main__":
    main()
