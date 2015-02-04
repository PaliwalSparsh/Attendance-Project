#!usr/env/bin/python2.7

import checkdb
import sqlite3
import func

#main
def main():
	in_course = raw_input("Enter the course name.\n")
	if func.course_exist(in_course,checkdb.c) :
		checkdb.c.execute('SELECT strength FROM courses where name=?',(in_course,))
		strength = checkdb.c.fetchone()
		func.take_attendance(strength[0],in_course,checkdb.c)

	else :
		in_strength = int(raw_input("Ohh..New Course..Enter the strength of class\n"))
		checkdb.c.execute('INSERT INTO courses VALUES(?,?)',(in_course,in_strength))
		func.create_course(in_course,in_strength,checkdb.c)
		func.take_attendance(in_strength,in_course,checkdb.c)


if __name__ == "__main__" : main()

