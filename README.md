# leaks2sqlite3

leaks2sqlite3 is a simple python3 parser to import 03/04/2021 published facebook leaks, from a csv to a SQLite3 DB.
<br>
The script automatically goes past the malformed csv lines and creates indexes for the phone numbers.

<br>

## Important

Before you run leakrecord.py you must adjust the csv file because is full of "12:00:00"
where the csv delimiter is the character ":"

<br>

#### Proved replace method:
```bash
sed -i 's^12:00:00^12.00.00^g' your_filelist.csv
```
