#!usr/env/bin/python2.7

import sqlite3
import datetime


def take_attendance(strength,course,conn_obj):
	today = str(datetime.date.today())
	print ("Attendance for %s" %today)
	try:
		conn_obj.execute("ALTER TABLE %s ADD COLUMN '%s' 'char'" %(course,today))
	except sqlite3.OperationalError:
		print "Attendance for the date already taken"
		return
	print "Enter p | a | m  for  Present | Absent | Manual_entry" 
	for x in range(1,strength):
		print ("%d." %x)
		att = raw_input("").lower()
		while(1):
			if  att =='p' :
				print "present"
				conn_obj.execute("UPDATE %s SET '%s'='P' WHERE 'roll'=%d" %(course,today,x))
				break
			elif  att == 'a' :
				print "absent"
				conn_obj.execute("UPDATE %s SET '%s'='A' WHERE 'roll'=%d" %(course,today,x))
				break
			elif att == 'm' :
				man = int(raw_input("Enter the roll call\n"))
				man_att = raw_input("Enter p | a  for  Present | Absent\n").lower()
				if man_att == 'p' :
					print "present"
					conn_obj.execute("UPDATE %s SET '%s'='P' WHERE 'roll'=%d" %(course,today,man))
				elif man_att == 'a' :
					print "absent"
					conn_obj.execute("UPDATE %s SET '%s'='A' WHERE 'roll'=%d" %(course,today,man))
				break	
			else:
				print "Enter a valid input"
				continue

def course_exist(course,conn_obj):
	for x in conn_obj.execute("SELECT name from courses;"):
		if (x[0].lower()) == (course.lower()):
			return True
	return False


def create_course(course,strength,conn_obj):
	conn_obj.execute('CREATE TABLE %s(roll int);' %course)
	for x in range(1,strength):
		conn_obj.execute("INSERT INTO %s VALUES(%d);" %(course,x))
		

if __name__ == "__main__":main()
