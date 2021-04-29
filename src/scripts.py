import string
import random

from passlib.hash import pbkdf2_sha256


def create_password(raw_pass: str):
    salt = string.ascii_lowercase
    salt = ''.join(random.choice(salt) for i in range(10)).encode('utf-8')
    pass_hash = pbkdf2_sha256.using(rounds=12000, salt_size=15, salt=salt).hash(raw_pass)
    return pass_hash, salt


def check_password(raw_pass: str, hash: bytes) -> bool:
    return pbkdf2_sha256.verify(raw_pass, hash)


if __name__ == '__main__':
    password = '16031989'
    hash_pass, salt = create_password(password)
    print(hash_pass)
    check = check_password(raw_pass='password', hash=hash_pass)
    print(check)

