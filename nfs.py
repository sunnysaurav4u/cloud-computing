#!/usr/bin/python
import os,commands,cgi,cgitb
cgitb.enable()

print "content-type: text/html\n\n"

print ""

data=cgi.FieldStorage()

userid=data.getvalue("userid")

size=data.getvalue("size")

password=data.getvalue("password")


commands.getstatusoutput("sudo useradd "+userid)
commands.getstatusoutput("sudo echo "+password+" | passwd  "+userid+" --stdin")


commands.getstatusoutput("sudo  lvcreate    -V"+size+"G  --name "+userid+"  --thin vg1/pool1")

commands.getstatusoutput("sudo mkfs.xfs /dev/vg1/"+userid)

commands.getstatusoutput("sudo mkdir /mnt/"+userid)

commands.getoutput('sudo mount /dev/vg1/'+userid+'  /mnt/'+userid)


x='/mnt/'+userid+'     *(rw,no_root_squash)\n'

f=open("/etc/exports","a")

f.write(x)

f.close()

ec=commands.getstatusoutput('sudo systemctl restart nfs-server')

print "you are Done.........................."
