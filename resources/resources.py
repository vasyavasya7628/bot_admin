def text_parse_mode() -> str:
    return "HTML"


def text_tell_about_your_problem() -> str:
    return "Сообщить о неисправности/проблеме (Для специалистов)"


def text_register_for_admins() -> str:
    return "Зарегистрироваться(Для администраторов)"


def text_end_register_for_admins() -> str:
    return "Регистрация завершена!"


def text_choose_button() -> str:
    return "Выберите"


def text_incorrect_text() -> str:
    return "Если вы хотите сообщить о неполадках, следуйте кнопкам в меню"


def text_incorrect_image() -> str:
    return "Этот бот не для того, чтобы отправлять стикеры."


def text_incorrect_gif() -> str:
    return "Этот бот не для того, чтобы отправлять Гиф-файлы."


def text_write_to_it() -> str:
    return "Написать в IT-Отдел."


def text_admin_choose_district() -> str:
    return "Выберите ведомство из списка(Для It специалистов):"


def text_user_choose_district() -> str:
    return "Выберите ведомство из списка(Для специалистов c окно):"


def text_return_to_main_menu() -> str:
    return "Вернуться в главное меню"


def text_admin_login() -> str:
    return "Зарегистрироваться(для it специалистов)"


def text_order_list() -> str:
    return "Список заявок(для it специалистов)"


def my_orders_at_work() -> str:
    return "В работе"

def all_orders() -> str:
    return "Все заявки"
def my_orders_delayed() -> str:
    return "Отложены"


def my_orders_completed() -> str:
    return "Выполненные"


def my_orders() -> str:
    return "Мои заявки"


def text_orders() -> str:
    return "Выберите ведомство в котором вы хотите посмотреть заявки?"


def text_register_complete() -> str:
    return "Регистрация завершена!"


def text_greetings() -> str:
    return ("Здравствуйте, чем я могу вам помочь?\n"
            "Если вы специалист и у вас есть проблема, нажмите кнопку 'Написать в IT-Отдел'.\n")


def text_describe_your_problem() -> str:
    return "Опишите вашу проблему"


def text_message_correct() -> str:
    return "Вы уверены, что описали проблему правильно?"


def text_lower_case() -> str:
    return "_"


def text_order_send() -> str:
    return "Заявка успешно создана! Специалисты свяжутся с вами в ближайшее время."


def get_districts() -> list:
    districts = [

        "Отдел 'Мои документы' город Кемерово, бр Пионерский, 3",
        "26",

    ]
    return districts
