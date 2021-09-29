from mysql.connector import connect, Error
from loguru import logger
from colr import color

################################################################################
# @author      : mclds
# @file        : status
# @created     : 12/08/2021
# @email       : mclds@protonmail.com
# @description :
#
################################################################################

fmt = "{time} - {name} - {level} - {message}"
logger.add("spam.log", level="DEBUG", format=fmt, backtrace=True, diagnose=True)
logger.add("error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)


@logger.catch  # Decorator for loguru. All errors will go log. Has to be on all functions
def search():
    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="bkmks")
        cur = conn.cursor()
        query = "EXPLAIN SELECT * FROM bkmks"
        cur.execute(query)
        records = cur.fetchall()
        for row in records:
            print(color(" [*] TITLE » ", fore="#85a585"), color(str(row[1]), fore="#fdf3d3"))
            print(color(" [*] COMMENT » ", fore="#85a585"), color(str(row[2]), fore="#fdf3d3"))
            print(color(" [*] LINK ? ", fore="#85a585"), color(str(row[3]), fore="#f29b85"))
            print(color(" [*] KEYWORD 1 » ", fore="#85a585"), color(str(row[4]), fore="#fdf3d3"))
            print(color(" [*] KEYWORD 2 » ", fore="#85a585"), color(str(row[5]), fore="#fdf3d3"))
            print(color(" [*] KEYWORD 3 » ", fore="#85a585"), color(str(row[6]), fore="#fdf3d3"))
            print(color(" [*] TIME » ", fore="#85a585"), color(str(row[7]), fore="#fdf3d3"))
            print("\n")
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    search()
