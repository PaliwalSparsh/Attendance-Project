#!usr/env/bin/python2.7

import sqlite3
import os.path

def check_db():
	if os.path.isfile("/attendance/all.db"):
		conn = sqlite3.connect("/attendance/all.db")
		c = conn.cursor()
		c.execute()
	else:
		conn = sqlite3.connect("/attendance/all.db")
		c = conn.cursor()
		c.execute("CREATE TABLE courses(name char,strength int);")
		con.commit()

if __name__ == "__main__":main()
