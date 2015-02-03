#!usr/env/bin/python2.7

import sqlite3

def take_attendace(strength):
	for x in range(1,strength):
		if (raw_input("").lower())=='p':
			print "present"
		if (raw_input("").lower())=='A':
			print "absent"

def course_exist(course,conn_obj):
	for x in conn_obj.execute("SELECT name from courses;"):
		if (x.lower())==(course.lower()):
			return True
	return False

def create_course(course,strength,conn_obj):
	conn_obj.execute('CREATE TABLE ? (roll int);',course)
	for x in range(1,strength):
		conn_obj.execute("INSERT INTO %s VALUES(%d);" %course %x)

if __name__ == "__main__":main()
