import emoji

# -------BOT MESSAGES-------
MESSAGE_ABOUT_BOT = emoji.emojize(
    "<b>Бот-помічник для зручного перегляду розкладу</b>\n\n"
    "Автор ідеї, 1.0v: @fortim\n"
    "Удосконалення, 2.0v: @thestd [http://std.community]\n"
    "GitHub: https://github.com/thestd/ScheduleBot \n\n"
    "Технічна підтримка: [@bkorzhak, @Mr_Luck] :smiling_imp:",
    use_aliases=True)

ADMIN_MESSAGE = "<b>Адмін. панель бота</b>\n\n" \
                "Привіт, %s. За допомогою цієї панелі ти можеш управляти ботом\n\n" \
                "<pre>Кількість зареєстрованих користувачів: 32</pre>"


# -------SCHEDULE MESSAGES-------
MESSAGE_BEFORE_REGISTER = emoji.emojize("Привіт. Введи свою групу, або прізвище викладача :grinning:", use_aliases=True)
MESSAGE_AFTER_REGISTER = emoji.emojize("Ну що ж, бажаю хорошого розкладу :wink:", use_aliases=True)
MAYBE = emoji.emojize("Можливо ви мали на увазі:", use_aliases=True)
NOT_EXISTS = emoji.emojize("Не можу знайти, спробуй ще раз :no_mouth:", use_aliases=True)
CHOSE_FROM_LIST = emoji.emojize("Ось що мені вдалось знайти :mag_right:\n"
                                "Вибери потріний :ballot_box_with_check:",
                                use_aliases=True)

SUCCESS_REGISTER = emoji.emojize("Всі наступні запити будуть по \"%s\" :pushpin:\n"
                                 "Щоб змінити групу, або викладача просто надішли мені нове ім'я, я все зроблю за тебе"
                                 ":smile: :ok_hand:",
                                 use_aliases=True)
FAILURE_REGISTER = emoji.emojize("Ми не знайшли такої групи. Спробуй ще раз :fearful:", use_aliases=True)

OVER_RESULT = emoji.emojize("<i>Нам прийшлось обмежити кількість результатів до 10. "
                            "Будь ласка, вкажіть більш конкретні дані</i>\n", use_aliases=True)

SCHEDULE_NONE_EXISTS = emoji.emojize("<b>Дозволяю відпочити. Немає пар</b> :smiling_imp:", use_aliases=True)
