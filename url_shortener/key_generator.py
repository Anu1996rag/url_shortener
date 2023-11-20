import secrets
import string

chars = string.ascii_letters + string.digits


def create_random_key(length: int = 5) -> str:
    return "".join(secrets.choice(chars) for _ in range(length))
