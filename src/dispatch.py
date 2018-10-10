from telegram.ext import Updater, CommandHandler, RegexHandler, MessageHandler, Filters, CallbackQueryHandler
from config import settings, command as cmd
from src import bot
import logging

updater = Updater(token=settings.BOT_TOKEN)
dispatcher = updater.dispatcher
bot = bot.ScheduleBot()


# ********* BASE DISPATCH *********
start_hand = CommandHandler(cmd.START, bot.menu_before_register)
dispatcher.add_handler(start_hand)


# ********* AFTER REGISTER DISPATCH *********
today_hand = RegexHandler(cmd.TODAY, bot.get_today)
dispatcher.add_handler(today_hand)

tomorrow_hand = RegexHandler(cmd.TOMORROW, bot.get_tomorrow)
dispatcher.add_handler(tomorrow_hand)

week_hand = RegexHandler(cmd.WEEK, bot.get_week)
dispatcher.add_handler(week_hand)

two_week_hand = RegexHandler(cmd.TWO_WEEK, bot.get_two_week)
dispatcher.add_handler(two_week_hand)


# ********* BEFORE REGISTER DISPATCH *********
about_bot_hand = RegexHandler(cmd.ABOUT_BOT, bot.about)
dispatcher.add_handler(about_bot_hand)

call_back_handler = CallbackQueryHandler(bot.init_search_field)
dispatcher.add_handler(call_back_handler)

register_hand = MessageHandler(Filters.text, bot.register)
dispatcher.add_handler(register_hand)


# ********* BEFORE REGISTER DISPATCH *********
admin_hand = CommandHandler(cmd.ADMIN_PANEL, bot.admin_panel)
dispatcher.add_handler(admin_hand)

get_my_id = CommandHandler(cmd.GET_MY_ID, bot.get_my_id)
dispatcher.add_handler(get_my_id)

# ========== LOGGING ==========
if settings.LOGGING_ENABLE:
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
    logger = logging.getLogger(__name__)

    def error(bot, update, error):
        logger.warning('Update "%s" caused error "%s"', update, error)

    dispatcher.add_error_handler(error)
