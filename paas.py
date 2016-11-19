#!/usr/bin/python

import cgitb,cgi,commands,random

print "Content-type:text/html"
print ""

cgitb.enable()

data = cgi.FieldStorage()
platform = data.getvalue("platform")

port=random.randint(6000,7000)
cl_ip = cgi.os.environ["REMOTE_ADDR"]
commands.getoutput("sudo systemctl restart docker")
#print "access your containers using links:"
#print "<br>"
if platform=="python":
	commands.getoutput("sudo docker run -it -p "+ str(port) +":4200 -d sunny")
	print (" <a href='http://"+cl_ip+":" + str(port) +"' target='_blank'> click here to get python</a>")
	print "<br>"
	print "login using user:sunny passwd:123"
	print "<br/>"
if platform=="bash":
	commands.getoutput("sudo docker run -it -p "+ str(port) +":4200 -d sunny")	
	print (" <a href='http://"+cl_ip+":" + str(port) +"' target='_blank'> Click here to get bash </a>")
	print "<br/>"
	print "login using user:saurav  passwd:123"


