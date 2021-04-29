import string
import random

from passlib.hash import pbkdf2_sha256


def create_password(raw_password: str) -> str:
    ascii_string = string.ascii_lowercase
    salt = ''.join(random.choice(ascii_string) for _ in range(10)).encode('utf-8')
    pass_hash = pbkdf2_sha256.using(rounds=random.randint(120, 99999), salt_size=10, salt=salt).hash(raw_password)
    return pass_hash


def verify_password(raw_password: str, hash_pass: str) -> bool:
    return pbkdf2_sha256.verify(raw_password, hash_pass)
