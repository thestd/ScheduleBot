import telegram
import datetime as dt

from config import command as _
from config import notification as notific
from config import settings
from src.web import ScheduleScrapper
from src.database import DataBase


class ScheduleBot:
    def __init__(self):
        self.db = DataBase()
        self.scrapper = ScheduleScrapper()
        self._keyboard_before_register = [
            [_.ABOUT_BOT]
        ]

        self._keyboard_after_register = [
            [_.TODAY, _.TOMORROW],
            [_.DAY_AFTER_TOMORROW, _.WEEK],
            [_.TWO_WEEK, _.ABOUT_BOT]
        ]

        self._keyboard_admin_panel = [
            ["/"+_.GET_MY_ID, _.MAIN_MENU],
        ]

    def menu_before_register(self, bot, update):
        '''
        The method of outputting the menu before the user's registration
        :param bot: bot-object
        :param update: last received data
        :sending: menu and message
        '''
        reply_markup = telegram.ReplyKeyboardMarkup(self._keyboard_before_register)
        bot.send_message(chat_id=update.message.chat_id,
                         text=notific.MESSAGE_BEFORE_REGISTER,
                         reply_markup=reply_markup)

    def menu_after_register(self, bot, update):
        '''
        The method of outputting the menu after the user's registration
        :param bot: bot-object
        :param update: last received data
        :sending: menu and message
        '''
        reply_markup = telegram.ReplyKeyboardMarkup(self._keyboard_after_register)
        bot.send_message(chat_id=update.message.chat_id,
                         text=notific.MESSAGE_AFTER_REGISTER,
                         reply_markup=reply_markup)

    def menu_admin_panel(self, bot, update, message: str):
        '''
        The method of outputting the admin menu
        :param bot: bot-object
        :param update: last received data
        :sending: menu and message
        '''
        reply_markup = telegram.ReplyKeyboardMarkup(self._keyboard_admin_panel)
        bot.send_message(chat_id=update.message.chat_id,
                         text=message,
                         reply_markup=reply_markup,
                         parse_mode='HTML')

    def _send_schedule_message(self, bot, update, response: list):
        '''
        Sending method
        :param bot: bot-object
        :param update: last received data
        :param response: list with messages
        :sending: message
        '''
        if len(response) == 0:
            response.append(notific.SCHEDULE_NONE_EXISTS)
        for el in response:
            bot.send_message(chat_id=update.message.chat_id, text=el, parse_mode='HTML')

    def register(self, bot, update):
        '''
        Registration method
        :param bot: bot-object
        :param update: last received data
        :sending: message with keyboard after registration
        '''
        text = update.message.text.upper()
        keyboard = []
        result = [self.scrapper.groups_get(text), self.scrapper.teachers_get(text)]
        for item in result[0]:
            keyboard.append([telegram.InlineKeyboardButton(item, callback_data=f'g_{item}')])
        for item in result[1]:
            keyboard.append([telegram.InlineKeyboardButton(item, callback_data=f't_{item}')])
        if len(keyboard) == 0:
            update.message.reply_text(text=notific.NOT_EXISTS)
        else:
            update.message.reply_text(text=notific.OVER_RESULT if len(keyboard) > 10 else "" + notific.CHOSE_FROM_LIST,
                                      reply_markup=telegram.InlineKeyboardMarkup(keyboard[:10]), parse_mode='HTML')

    def init_search_field(self, bot, update):
        '''
        Checks whether a user exists. If not - creates a record in the database. Otherwise we will overwrite it
        :param bot: bot-object
        :param update: last received data
        :sending: Notification of successful registration or overwriting
        '''
        query = update.callback_query
        user_id = query.message.chat_id
        if self.db.user_id_exists(user_id):
            self.db.change_group_name(user_id, query.data)
        else:
            self.db.add_user(query.message.chat_id, query.data)
        bot.edit_message_text(text=notific.SUCCESS_REGISTER % query.data[2:],
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
        self.menu_after_register(bot, query)

    def get_today(self, bot, update):
        '''
        Schedule today
        :param bot: bot-object
        :param update: last received data
        :sending: message with schedule today or error
        '''
        data = self.db.get_group_name(update.message.chat_id).split('_')
        if data[0] == 'g':
            response = self.scrapper.get_schedule(
                group=data[1]
            )
        else:
            response = self.scrapper.get_schedule(
                teacher=data[1]
            )
        self._send_schedule_message(bot, update, response)

    def get_tomorrow(self, bot, update):
        '''
        Schedule tomorrow
        :param bot: bot-object
        :param update: last received data
        :sending: message with schedule tomorrow or error
        '''
        tomorrow = (dt.datetime.today().date() + dt.timedelta(days=1)).strftime(settings.DATE_FORMAT)
        data = self.db.get_group_name(update.message.chat_id).split('_')
        if data[0] == 'g':
            response = self.scrapper.get_schedule(
                group=data[1],
                sdate=tomorrow, edate=tomorrow
            )
        else:
            response = self.scrapper.get_schedule(
                teacher=data[1],
                sdate=tomorrow, edate=tomorrow
            )
        self._send_schedule_message(bot, update, response)

    def get_day_after_tomorrow(self, bot, update):
        '''
        Schedule the day after tomorrow
        :param bot: bot-object
        :param update: last received data
        :sending: message with schedule tomorrow or error
        '''
        tomorrow = (dt.datetime.today().date() + dt.timedelta(days=2)).strftime(settings.DATE_FORMAT)
        data = self.db.get_group_name(update.message.chat_id).split('_')
        if data[0] == 'g':
            response = self.scrapper.get_schedule(
                group=data[1],
                sdate=tomorrow, edate=tomorrow
            )
        else:
            response = self.scrapper.get_schedule(
                teacher=data[1],
                sdate=tomorrow, edate=tomorrow
            )
        self._send_schedule_message(bot, update, response)

    def get_week(self, bot, update):
        '''
        Weekly Schedule
        :param bot: bot-object
        :param update: last received data
        :sending: message with Weekly Schedule or error
        '''
        today = dt.datetime.today().date().strftime(settings.DATE_FORMAT)
        end_day = (dt.datetime.today().date() + dt.timedelta(days=7)).strftime(settings.DATE_FORMAT)
        data = self.db.get_group_name(update.message.chat_id).split('_')
        if data[0] == 'g':
            response = self.scrapper.get_schedule(
                group=data[1],
                sdate=today, edate=end_day
            )
        else:
            response = self.scrapper.get_schedule(
                teacher=data[1],
                sdate=today, edate=end_day
            )
        self._send_schedule_message(bot, update, response)

    def get_two_week(self, bot, update):
        '''
        Schedule for two weeks
        :param bot: bot-object
        :param update: last received data
        :sending: message with Schedule for two weeks or error
        '''
        today = dt.datetime.today().date().strftime(settings.DATE_FORMAT)
        end_day = (dt.datetime.today().date() + dt.timedelta(days=14)).strftime(settings.DATE_FORMAT)
        data = self.db.get_group_name(update.message.chat_id).split('_')
        if data[0] == 'g':
            response = self.scrapper.get_schedule(
                group=data[1],
                sdate=today, edate=end_day
            )
        else:
            response = self.scrapper.get_schedule(
                teacher=data[1],
                sdate=today, edate=end_day
            )
        self._send_schedule_message(bot, update, response)

    def admin_panel(self, bot, update):
        '''
        The admin panel for managing the bot and viewing the number of active users
        :param bot: bot-object
        :param update: last received data
        :sending: message with the number of active users and the admin key
        '''
        if update.message.chat_id in settings.ID_ADMINS:
            self.menu_admin_panel(bot, update, message=notific.ADMIN_MESSAGE % (
                                    update.message.chat['username'], self.db.get_count_users())
                                  )

    def get_my_id(self, bot, update):
        '''
        Method for getting your own ID
        :param bot: bot-object
        :param update: last received data
        :sending: chat id
        '''
        bot.send_message(chat_id=update.message.chat_id, text=update.message.chat_id)

    def about(self, bot, update):
        '''
        Message with bot data
        :param bot: bot-object
        :param update: last received data
        :sending: Message about bot
        '''
        bot.send_message(chat_id=update.message.chat_id, text=notific.MESSAGE_ABOUT_BOT, parse_mode='HTML')
