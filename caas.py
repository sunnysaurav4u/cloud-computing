#!/usr/bin/python

import cgitb,cgi,commands,random

print "Content-type:text/html"
print ""

cgitb.enable()

data = cgi.FieldStorage()
number = data.getvalue("container")
cl_ip = cgi.os.environ["REMOTE_ADDR"]
port=random.randint(6000,7000)
commands.getoutput("sudo systemctl restart docker")
print "access your containers using links:"
print "<br>"
for i in range(int(number)):
	commands.getoutput("sudo docker run -it -p "+ str(port) +":4200 -d sunny")
	print (" <a href='http://"+cl_ip+":" + str(port) +"' target='_blank'> Container " + str(i) +"</a>")
	print "<br>"
print "<br>"
print "===============CONGATES!!!!! Your container/s is/are ready.=================="
print "<br>"
print "Access containers using < login - root ; password - redhat >"

