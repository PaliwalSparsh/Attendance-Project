import sqlite3
import os.path

if os.path.isfile("/attendance/all.db"): 
	conn=sqlite3.connect("/attendance/all.db")
	c = conn.cursor()
	c.execute()
else :
	conn=sqlite3.connect("/attendance/all.db")
	c = conn.cursor()
	c.execute("CREATE TABLE course(name char,strength int)")
	con.commit()
