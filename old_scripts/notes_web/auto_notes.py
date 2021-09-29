#!/usr/bin/env python3.9

######################################################################
# @author      : mic (mic@$HOSTNAME)
# @file        : auto_notes.sh
# @created     : Saturday Jun 26, 2021 03:52:05 WEST
#
# @description : Publish notes inserted on cli on the website
######################################################################


from mysql.connector import connect, Error
import shutil
from low_range import low_range
from high_range import high_range
from medium_range import medium_range
from datetime import datetime


def auto():
    try:
        conn = connect(
            host="localhost",
            user="mic",
            password="xxxx",
            database="notes")
        cur = conn.cursor()
        null_list = []
        query = "SELECT * FROM notes WHERE url is NULL"
        cur.execute(query)
        records = cur.fetchall()
        for row in records:
            null_list.append(row)
        null_list = [[str(x) for x in tup] for tup in null_list]
    except Error as e:
        print("Error while connecting to db", e)

    null_list = [[x.replace('-', '') for x in i] for i in null_list]
    null_list = [[x.replace('\n', '<br>') for x in i] for i in null_list]
    
    new_id_list = []
    for lst in null_list:
        new_id_list.append(lst[0])

    new_url_list = []
    for lst in null_list:
        source = '/srv/http/notes/pages/styled_notes/index.php'
        destination = '/srv/http/notes/pages/styled_notes/' + str(lst[0]) + '-page.php'
        url = 'http://localhost/notes/pages/styled_notes/' + str(lst[0]) + '-page.php'
        new_url_list.append(url)
        shutil.copyfile(source, destination)
        with open(destination, 'r') as f:
            lines = f.readlines()
        lines[21] = str(lst[5])
        with open(destination, 'w') as f:
            f.writelines(lines)

    line_count = []
    for lst in null_list:
        line_count.append(lst[5].count('<br>'))

    result = zip(line_count, new_id_list, new_url_list)
    result = (list(result))
    for i in result:
        if i[0] >= 11 and i[0] <= 18:
            low_range(i[1])
            with open("/srv/http/notes/pages/styled_notes/" + i[1] + "-page.php", "r") as f:
                lines = f.readlines()
                lines[15] = "<div class='box-" + i[1] + "'><i class='fas fa-quote-left fa2'></i><div class='text'><i class='fas fa-quote-right fa1'></i><div>"
            with open('/srv/http/notes/pages/styled_notes/' + i[1] + '-page.php', 'w') as f:
                f.writelines(lines)
                print('low  range')
        if i[0] > 18 and i[0] <= 36:
            medium_range(i[1])
            with open("/srv/http/notes/pages/styled_notes/" + i[1] + "-page.php", "r") as f:
                lines = f.readlines()
                lines[15] = "<div class='box-" + i[1] + "'><i class='fas fa-quote-left fa2'></i><div class='text'><i class='fas fa-quote-right fa1'></i><div>"
            with open('/srv/http/notes/pages/styled_notes/' + i[1] + '-page.php', 'w') as f:
                f.writelines(lines)
                print('medium range')
        if i[0] > 36:
            high_range(i[1])
            with open("/srv/http/notes/pages/styled_notes/" + i[1] + "-page.php", "r") as f:
                lines = f.readlines()
                lines[15] = "<div class='box-" + i[1] + "'><i class='fas fa-quote-left fa2'></i><div class='text'><i class='fas fa-quote-right fa1'></i><div>"
            with open("/srv/http/notes/pages/styled_notes/" + i[1] + "-page.php", "w") as f:
                f.writelines(lines)
                print('high range')

    try:
        conn = connect(
            host="localhost",
            user="mic",
            password="xxxx",
            database="notes")
        cur = conn.cursor()
        for i in result:
            print('url - ', str(i[2]))
            print('id - ', str(i[1]))
            query = "UPDATE notes SET url = '" + str(i[2]) + "' WHERE ntid = " + str(i[1])
            print(query)
            cur.execute(query)
            conn.commit()
    except Error as e:
        print("Error while connecting to db", e)

    now = datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
    auto()
