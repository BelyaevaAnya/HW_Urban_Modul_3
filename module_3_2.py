# Цель: закрепить знания о параметрах по умолчанию и именованных аргументах.
#
# Задача "Рассылка писем":
# Часто при разработке и работе с рассылками писем(e-mail) они отправляются от одного
# и того же пользователя(администрации или службы поддержки). Тем не менее должна быть
# возможность сменить его в редких случаях.
# Попробуем реализовать функцию с подробной логикой.
#
# Создайте функцию send_email, которая принимает 2 обычных аргумента:
# сообщение и получатель и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.
# Внутри функции реализовать следующую логику:
# Проверка на корректность e-mail отправителя и получателя.
# Проверка на отправку самому себе.
# Проверка на отправителя по умолчанию.
end_mail_lst = ('.com', '.ru', '.net')


def send_email(message, recipient, sender=None):
    # проверка на "@" или нет оканчания на ".com"/".ru"/".net"
    try:
        flag_wrng_end_mail = True
        if sender is None:
            sender = 'university.help@gmail.com'
        else:
            sender.index('@')
            flag_wrng_end_mail &= sender.endswith(end_mail_lst)
        recipient.index('@')
        flag_wrng_end_mail &= recipient.endswith(end_mail_lst)
        if not flag_wrng_end_mail:
            raise ValueError('Work with Positive Numbers Only')
    except ValueError:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    else:
        if sender == recipient:
            print('Нельзя отправить письмо самому себе!')
        elif sender != 'university.help@gmail.com':
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        else:
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

# Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com.
# НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru.
# Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
# Нельзя отправить письмо самому себе!
