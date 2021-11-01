from exceptions_project import *


def is_cor_log_pas(login, password):
    cor_login = ['Ruslan', 'Amir']
    if login not in cor_login:
        raise ErrorLoginPassword("Данные введены не корректно!")
    cor_password = '123'
    if password != cor_password:
        raise ErrorLoginPassword("Данные введены не корректно!")
    return True


def is_restriction_password(password):
    if len(password) < 8 and password.is_alpha() and password.is_decimal() and three_podryad_keys(password):
        raise ErrorPasswordRestriction("asdjf;lkjsad;fl")
    return True


if __name__ == '__main__':
    login = input()
    password = input()
    is_ok = False
    try:
        is_ok = is_cor_log_pas(login, password)
    except ErrorLoginPassword as e:
        print(e, is_ok)
