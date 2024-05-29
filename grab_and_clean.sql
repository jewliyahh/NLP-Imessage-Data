SELECT
    DISTINCT
	message.ROWID, 
	message.text, 
	message.attributedBody,
	message.handle_id,
	message.is_from_me, 
   datetime (message.date / 1000000000 + strftime ("%s", "2001-01-01"), "unixepoch", "localtime") AS message_datetime, 
   strftime("%Y-%m-%d", datetime(message.date / 1000000000 + strftime("%s", "2001-01-01"), "unixepoch", "localtime")) AS message_date,
   chat.display_name
FROM
    message
    LEFT JOIN handle ON message.handle_id = handle.ROWID
	JOIN chat on chat.room_name = message.cache_roomnames
WHERE 
display_name = "The real housewives of GT"
AND datetime (message.date / 1000000000 + strftime ("%s", "2001-01-01"), "unixepoch", "localtime")>= "2023-01-01"
AND datetime (message.date / 1000000000 + strftime ("%s", "2001-01-01"), "unixepoch", "localtime")<= "2024-01-01"
