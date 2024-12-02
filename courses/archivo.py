from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("PRAGMA table_info(courses_chapter);")
    for row in cursor.fetchall():
        print(row)
