import re 
import string	
import io
import operator
from operator import itemgetter, attrgetter
import HTML
import xml.etree.ElementTree as ET
import urllib2
from cgi import escape
import sys, os
def getCoursesForParameters(year):
	allList = []
	httpCall="http://courses.rice.edu/admweb/!SWKSECX.main?term="+year
	response = urllib2.urlopen(httpCall)
	st = response.read()
	root = ET.fromstring(st)
	for course in root:
		allList.append(course)
	return allList
def createMapping():
	listB = getCoursesForParameters("201510")
	listA = getCoursesForParameters("201310")
	f = open("mapping", 'w')

	for course in listA:
		courseName = course.find("subject").text + " " + course.find("course-number").text + " "+course.find("section").text
		crnA = course.find("crn").text
		for courseB in listB:
			crnB = courseB.find("crn").text
			courseNameB = courseB.find("subject").text + " " + courseB.find("course-number").text + " "+courseB.find("section").text
			if courseName == courseNameB:
				f.write(crnB+", "+crnA+"\n")
				break
	f.close()

def getOldCRNForNewCRN(newCRN):
	f = open(".\\"+"mapping", "r")
	lines={}
	for st in f:
		aList = st.strip().split(', ')
		lines[aList[0]] = aList[1]
	f.close()
	return lines[newCRN]
	
def main():
	print getOldCRNForNewCRN("11346")

main()
	