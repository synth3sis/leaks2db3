# leaks2sqlite3

leaks2sqlite3 is a simple python3 parser to import 03/04/2021 published facebook leaks, from a csv to a SQLite3 DB.
<br>
The script automatically goes past the malformed csv lines and creates indexes for phone numbers, names, surnames, facebook_id.

<br>

### REQUIREMENTS
 - python3
 - sqlite3

```bash
apt install -y python3
apt install -y sqlite3
```

<br>

### RUN

Change the informations in the first 2 assignment and simply run
```bash
./leakrecord.py
```

<br>

### IMPORTANT

Before you run leakrecord.py you must adjust the csv file because is full of "12:00:00" strings
which are inteded to represent time, while the csv delimiter is the character ":".
<br>

#### Proved replace method:
```bash
sed -i 's^12:00:00^12.00.00^g' your_filelist.csv
```

<br>

### PoC
With bash grep:
<br>
<br>
![alt tag](https://i.ibb.co/GRBf3k6/before-grep.png)
<br>
<br>
With sqlite3 query:
<br>
<br>
![alt tag](https://i.ibb.co/XSp7ZLS/after-sqlite3.png)

