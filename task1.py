def check_auth(login: str, password: str):
    if login == "admin" and password == "password":
        result = "Добро пожаловать"
        # В этом блоке напишите код, который выполнится, если условие True. Используйте result, как в задании выше
    else:
        result = "Доступ ограничен"
        # В этом блоке напишите код, который выполнится, если условие False. Используйте result, как в задании выше

    return result


