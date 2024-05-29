import sqlite3
import datetime
import subprocess
import os


def read_messages(db_location, query, n=30000, self_number='Me', human_readable_date=True):
    conn = sqlite3.connect(db_location)
    cursor = conn.cursor()

    if n is not None:
        query += f" ORDER BY message.date DESC LIMIT {n}"

    results = cursor.execute(query).fetchall()
    messages = []

    for result in results:
        rowid, text, attributed_body, handle_id, is_from_me, message_datetime, message_date, display_name= result

        if text is not None:
            body = text
        elif attributed_body is None:
            continue
        else:
            attributed_body = attributed_body.decode('utf-8', errors='replace')

            if "NSNumber" in str(attributed_body):
                attributed_body = str(attributed_body).split("NSNumber")[0]
                if "NSString" in attributed_body:
                    attributed_body = str(attributed_body).split("NSString")[1]
                    if "NSDictionary" in attributed_body:
                        attributed_body = str(attributed_body).split("NSDictionary")[0]
                        attributed_body = attributed_body[6:-12]
                        body = attributed_body


        messages.append(
            {"rowid": rowid, "body": body, "handle_id": handle_id, "is_from_me": is_from_me,
             "message_datetime": message_datetime, "message_date": message_date, "display_name": display_name, 'group_chat_name' : display_name})

    conn.close()
    return messages
