from telegram.ext import Application
from create_event import create_event
from rsvp import send_rsvp, choose_rsvp, handle_rsvp
from inline_rsvp import inline_rsvp
from basic import start, help, get_id, set_birthday
import logging
from dotenv import load_dotenv
import os

load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    """Run the bot."""
    # Create the Application and pass it the bot's token.
    application = (
        Application.builder()
            # .token(os.getenv('TELE_BOT_TOKEN'))  # Main bot
            .token(os.getenv('TELE_BOT_TOKEN_TEST')) # Test bot
            .arbitrary_callback_data(True)
            .build()
    )

    application.add_handler(start())
    application.add_handler(help())
    application.add_handler(get_id())
    application.add_handler(set_birthday())
    application.add_handler(choose_rsvp())
    application.add_handler(create_event())
    application.add_handler(send_rsvp())
    application.add_handler(handle_rsvp())
    application.add_handler(inline_rsvp())
    # application.add_handler(
    #     CallbackQueryHandler(handle_invalid_button, pattern=InvalidCallbackData)
    # )

    # Run the bot
    application.run_polling()


if __name__ == "__main__":
    main()
