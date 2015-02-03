#!usr/env/bin/python2.7

import sqlite3

def take_attendace(strength):
	for x in range(1,strength):
		if (raw_input("").lower())=='p':
			print "present"
		if (raw_input("").lower())=='A':
			print "absent"

def course_exist(course):
	for x in c.execute("SELECT name from courses;"):
		if (x.lower())==(course.lower()):
			return true
	return false

def create_course(course,strength):
	c.execute("CREATE TABLE ? (roll int);",course)
	for x in range(1,strength):
		c.execute("INSERT INTO %s VALUES(%d);" %course %x)

if __name__ == "__main__":main()
