def check_email(email: str) -> bool:
    # Напишите ваш код здесь
    if " " not in email and "@" in email and "." in email:
        return True
    else:
        return False

