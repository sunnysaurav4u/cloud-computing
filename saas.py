#!/usr/bin/python
import os,commands,cgi,time
print "content-type:text/html"

print "";

data=cgi.FieldStorage()

userid=data.getvalue("userid")
password=data.getvalue("password")

print commands.getstatusoutput('sudo useradd '+userid)
print commands.getstatusoutput('sudo echo '+password+' | sudo passwd '+userid+'  --stdin')
if a[0]==0 and b[0]==0 :
	print "your account is created!!"
