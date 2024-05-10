CREATE_USER_TABLE_QUERY = '''CREATE TABLE IF NOT EXISTS telegramm_users(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
USERNAME CHAR(50),
FIRST_NAME CHAR(50),
LAST_NAME CHAR(50),
UNIQUE (TELEGRAM_ID))'''
INSERT_USER_QUERY = '''INSERT OR IGNORE INTO telegramm_users VALUES (?, ?, ?, ?, ?)'''

SELECT_USER = '''SELECT * FROM telegramm_users'''


CREATE_PROFILE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS profiles 
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
NICKNAME CHAR(50),
BIO CHAR(50),
PHOTO TEXT,
UNIQUE (TELEGRAM_ID)
)
"""

INSERT_PROFILE_QUERY = """
INSERT INTO profiles VALUES(?,?,?,?,?)
"""