#!/usr/bin/python
import os,commands,cgi,cgitb
cgitb.enable()

print "content-type:text/html"

print ""

data=cgi.FieldStorage()

userid=data.getvalue("userid")

size=data.getvalue("size")
password=data.getvalue("password")


commands.getstatusoutput("sudo useradd "+userid)
commands.getstatusoutput("sudo echo "+password+" | sudo passwd "+userid+"  --stdin")
commands.getstatusoutput("sudo  lvcreate    -V"+size+"G  --name "+userid+"  --thin vg1/pool1")
commands.getstatusoutput("sudo mkfs.xfs  /dev/vg1/"+userid)
commands.getstatusoutput("sudo mkdir /mnt/"+userid)
commands.getstatusoutput("sudo mount /dev/vg1/"+userid+" /mnt/"+userid)


print "YOU ARE DONE............................."
