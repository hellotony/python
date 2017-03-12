import time;
import calendar;
import os;

# if True:
#     print "hello world"
#     print "learn python day one"
# else:
#     print "false"
# total = "hello " + \
#         "world"
# print total
#
#
# count = 200
# number = 2.4
# name = "john"
# print count
# print number
# print name
# a = b = c = "hello world"
# print a
# print b
# print c
#
# print name[0]
# print name[0:2]
# print name[2:]
# print name * 2
# print name + "hello "
#
# testObject = {'id': 1, 'name': "test"}
# print testObject["id"]
# print testObject["name"]
#
# listq = ["one", "two", "three"]
# for item in listq:
#     for i in listq:
#         if i == item:
#             continue
#         print i
#
# print time.asctime(time.localtime(time.time()))
# print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#
# print calendar.month(2017, 4)
#
# def addNum(str1, str2):
#     print str1 + str2
#     return str1 + str2
#
# addNum(1, 3)
#
# content = dir(time)
# print content
#
# print "------------------------------------->"
# print globals()
# print locals()
#
#
# obj = open("testIo.txt", "wb")
# print obj.name
# print obj.mode
#
# obj.write("test to insert into it")
# obj.close()
#
# obj = open("testIo.txt", "r+")
# str = obj.read()
# print obj.tell()
# print str
# obj.close()
#
# os.rename("testIo.txt", "testupdate.txt")

try:
    fh = open("testfile", "r")
    fh.write("fds")
except IOError:
    print "Error: fsdfdsa"
else:
    print "fds"
    fh.close()
