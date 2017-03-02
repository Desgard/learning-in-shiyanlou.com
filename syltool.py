# -*- coding: utf-8 -*-

import sys
import os
import argparse
from urllib.request import urlopen
from course import Course
from bs4 import BeautifulSoup

DEFALUT_ROOTWEB_URL = 'https://www.shiyanlou.com/courses/'

parser = argparse.ArgumentParser()

parser.add_argument("-g", "--gett", help = "get the name of course by course code. [given a number]", type = int)
parser.add_argument("-cc", "--cf-c", help = "create a folder in default path in client.", action = 'store_true')
parser.add_argument("-cs", "--cf-s", help = "create a folder in default path in server.", action = 'store_true')
parser.add_argument("-s", "--scp", help = "scp the files to server folder", action = 'store_true')

args = parser.parse_args()
course_msg = Course()
course_code = args.gett

if args.gett:
    url = str(DEFALUT_ROOTWEB_URL) + str(course_code)
    print('Get ready to fetch the', course_code, 'course message...')
    print("Checking in", url)

    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")

    # Get the course name
    title = soup.find_all('h4', attrs = {
        'class': 'pull-left course-infobox-title',
    })[0].find_all('span')[0].string

    print("This course is   <", title, ">")

    # Get the course chapter
    chapter_obj = soup.find_all('div', attrs = {
        'class': 'lab-item-title',
    })

    chapters = []
    for ch in chapter_obj:
        chapters.append(ch.string)

    # Get the course obj
    course_msg = Course(url = url, name = title, code = course_code, chapter = chapters)

if args.cf_c:
    print("Build folders...")
    cmd = "mkdir '" + str(course_msg.name) + "'"
    os.system(cmd)
    for chapter in course_msg.chapter:
        cmd = "mkdir '" + str(course_msg.name) + "/" + str(chapter) + "'"
        os.system(cmd)



if args.cf_s:
    print("s, build")
