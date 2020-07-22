from passlib.hash import pbkdf2_sha256

password = '1234'

hash_pw = pbkdf2_sha256.hash(password)
print(hash_pw)
print(pbkdf2_sha256.verify(password, hash_pw))
# print(hash_pw =='$pbkdf2-sha256$29000$mzOmdC7l/B.DUIqRcq4Vwg$f6L9GhLEk2Hd5SQoOuycTlfTSZZKlJqWHEWYU3t9MSg')