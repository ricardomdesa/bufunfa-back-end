import binascii
import hashlib
import os


def verify_password(stored_password, password):
    ITERATIONS = 100000
    SALT_SIZE = 64
    salt = stored_password[:SALT_SIZE]
    stored_password = stored_password[SALT_SIZE:]
    password_hash = hashlib.pbkdf2_hmac("sha512", password.encode("utf-8"), salt.encode("ascii"), ITERATIONS)
    password_hash = binascii.hexlify(password_hash).decode("ascii")
    return password_hash == stored_password


def hash_password(password):
    ITERATIONS = 100000
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
    password_hash = hashlib.pbkdf2_hmac("sha512", password.encode("utf-8"), salt, ITERATIONS)
    password_hash = binascii.hexlify(password_hash)
    return (salt + password_hash).decode("ascii")
