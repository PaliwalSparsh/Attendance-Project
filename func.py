#!usr/env/bin/python2.7

import sqlite3
import datetime

def take_attendance(strength,course,conn_obj): 
	today = str(datetime.date.today())
	conn_obj.execute("ALTER TABLE %s ADD %s char" %(course,today))  
	for x in range(1,strength):
		print ("%d ." %x)
		if (raw_input("").lower())=='p':
			print "present"
			conn_obj.execute("UPDATE %s SET %s='P' WHERE roll=%d" %(course,today,x))
		if (raw_input("").lower())=='a':
			print "absent"
			conn_obj.execute("UPDATE %s SET %s='A' WHERE roll=%d" %(course,today,x))

def course_exist(course,conn_obj):
	for x in conn_obj.execute("SELECT name from courses;"):
		if (x[0].lower())==(course.lower()):
			return True
	return False

def create_course(course,strength,conn_obj):
	conn_obj.execute('CREATE TABLE %s(roll int);' %course)
	for x in range(1,strength):
		conn_obj.execute("INSERT INTO %s VALUES(%d);" %(course,x))
		

if __name__ == "__main__":main()
