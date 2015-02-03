#!usr/env/bin/python2.7

import sqlite3
import os.path

def check_db():
	if os.path.isfile("all.db"):
		conn = sqlite3.connect("all.db")
		c = conn.cursor()
	else:
		conn = sqlite3.connect("all.db")
		c = conn.cursor()
		c.execute("CREATE TABLE courses(name char,strength int);")
		conn.commit()

if __name__ == "__main__":main()
