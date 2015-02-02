#!usr/env/bin/python2.7

import checkdb
import sqlite3
import func

#main
def main():
	check_db()
	in_course = raw_input("Enter the course name.")
	if course_exist(in_course) :
		strength = c.execute("SELECT strength FROM courses where name=?;",in_course);
		take_attendace(in_course)

	else :
		in_strength = raw_input("Ohh..New Course..Enter the strength of class")
		c.execute("INSERT INTO courses VALUES(?,?);",course,strength)
		create_course(in_course,in_strength)
		take_attendance(in_course)


if __name__ == "__main__" : main()
