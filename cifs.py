#!/usr/bin/python
import os,commands,cgi,cgitb
cgitb.enable()

print "content-type: text/html"

print ""

data=cgi.FieldStorage()

userid=data.getvalue("userid")

size=data.getvalue("size")
password=data.getvalue("password")

commands.getstatusoutput("sudo useradd "+userid)
commands.getstatusoutput('sudo echo  -e "'+password+'\n'+password+'" | sudo smbpasswd  -a '+userid) 
commands.getstatusoutput("sudo  lvcreate    -V"+size+"G  --name "+userid+"  --thin vg1/pool1")

commands.getstatusoutput("sudo mkfs.xfs /dev/vg1/"+userid)

commands.getstatusoutput("sudo mkdir /mnt/"+userid)



commands.getstatusoutput('sudo mount /dev/vg1/'+userid+'  /mnt/'+userid)
#commands.getstatusoutput('sudo chmod 777 /etc/samba/smb.conf')
f=open("/etc/samba/smb.conf","a")
f.write('\n['+userid+']\n path=/mnt/'+userid+' \n writable=yes\n')


f.close()
commands.getstatusoutput('sudo chmod 777 /mnt/'+userid)
commands.getstatusoutput('sudo systemctl restart smb')


print "=========================you are done========================"
