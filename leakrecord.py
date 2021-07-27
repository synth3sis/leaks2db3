#!/usr/bin/env python3

import csv
import os
import os.path
import locale
import sys
import sqlite3
from sqlite3 import Error

####################################################################
#		Change the following 2 lines to modify parameters
####################################################################
csvFile = 'facebook.csv'
facebookleaks_db = 'facebookleaks.db'




def create_conn(db_file):
	conn = None
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)
	return conn





def create_leaks():
	create_leaks_table =  '''
						CREATE TABLE IF NOT EXISTS leaks (
							id INTEGER PRIMARY KEY AUTOINCREMENT,
							phone 		BIGINT,
							facebook_id VARCHAR(60),
							name 		VARCHAR(60),
							surname		VARCHAR(60),
							sex			VARCHAR(20),
							city		VARCHAR(120),
							regione 	VARCHAR(120),
							rel			VARCHAR(120),
							job			VARCHAR(3000),
							ex_date		VARCHAR(60),
							email		VARCHAR(250),
							birth_date	VARCHAR(60)
						);
					  	'''

	conn = create_conn(facebookleaks_db)

	try:
		cur = conn.cursor()
		cur.execute(create_leaks_table)
		print("[+] TABLE 'leaks' created successfully")
		conn.commit()
		conn.close()
	except Error as err:
		print ("Cannot create tables")
		print (err)
		exit(2)




def leaks_index():
	conn = create_conn(facebookleaks_db)
	cur = conn.cursor()
	print ("    > Phone Indexes...")
	index_query = "CREATE INDEX phone_index ON leaks (phone);"
	cur.execute(index_query)
	print ("    > Name Indexes...")
	index_query = "CREATE INDEX name_index ON leaks (name);"
	cur.execute(index_query)
	print ("    > Surname Indexes...")
	index_query = "CREATE INDEX surname_index ON leaks (surname);"
	cur.execute(index_query)
	print ("    > Email Indexes...")
	index_query = "CREATE INDEX email_index ON leaks (email);"
	cur.execute(index_query)
	print ("    > Facebook ID Indexes...")
	index_query = "CREATE INDEX facebookid_index ON leaks (facebook_id);"
	cur.execute(index_query)


def print_usage():
	print("Usage: ./python3 csvFile.csv ")
	exit(0)



def main():

	print ("[+] Creating new database with:")
	print ("    > csv data  = " + csvFile)
	print ("    > target DB = " + facebookleaks_db)

	if not os.path.isfile(facebookleaks_db):
		with open(facebookleaks_db, 'w'): pass
		print("[+] " + facebookleaks_db + " created successfully")
		create_leaks()
	try:
		conn = create_conn(facebookleaks_db)
		cur = conn.cursor()
		cur.execute("DELETE FROM leaks")
		print ("[+] Previous records deleted successfully from table leaks")
	except Error as err:
		print ("Cannot delete previous leaks content");
		print (err)
		exit(2)


	csv.field_size_limit(sys.maxsize)
	nation_id = 1 		# italy
	i = 0
	jump = 0
	with open(csvFile) as f:
		rdr = csv.reader(f, delimiter = ':')
		print ("[+] Inserting records in database...")
		for row in rdr:
			i = i + 1
			try:
				if len(row) == 12:
					record = (i,int(row[0]),row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])
				else:
					print ("[ERR] Index range is " + str(len(row)) + " in row " + str(i) + ". Row Content:")
					print ("      " + str(row))
					jump = 1
			except IndexError as err1:
				print ("Error assigning record. N=" + str(i))
				print (row)
				print (err1)
				exit(0)

			try:
				if jump != 1:
					cur.execute("INSERT INTO leaks VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", record)
					if (i % 52123) == 0:
						conn.commit()
						print ("[+] Record inserted: " + str(f'{i:,}').replace(",",".") + "    ", end = "\r")
				else:
					jump = 0
			except Error as err:
				print ("Error insering record N." + str(i))
				print (err)
				exit(2)
		print("[+++] Total Record inserted: " + str(i))
		conn.commit()
		conn.close()

	try:
		print ("[+] Creating indexes for table leaks")
		leaks_index()
		print ("[+++] Success! Your DB is ready")
	except Error as err:
		print ("Couldn't create indexes over 'leaks'")
		print (err)
		exit(2)

if __name__ == '__main__':
	main()
