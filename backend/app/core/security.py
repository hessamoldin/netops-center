from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()

_fernet = Fernet(os.getenv("FERNET_KEY").encode())


def encrypt(plain: str) -> str:
    return _fernet.encrypt(plain.encode()).decode()


def decrypt(token: str) -> str:
    return _fernet.decrypt(token.encode()).decode()
