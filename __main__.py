#!usr/env/bin/python2.7

import checkdb
import sqlite3
import func

#main
def main():
	in_course = raw_input("Enter the course name.")
	if func.course_exist(in_course,checkdb.c) :
		strength = checkdb.c.execute("SELECT strength FROM courses where name=?;",in_course);
		func.take_attendace(in_course)

	else :
		in_strength = raw_input("Ohh..New Course..Enter the strength of class")
		checkdb.c.execute("INSERT INTO courses VALUES(?,?);",course,strength)
		func.create_course(in_course,in_strength,checkdb.c)
		func.take_attendance(in_course)


if __name__ == "__main__" : main()
