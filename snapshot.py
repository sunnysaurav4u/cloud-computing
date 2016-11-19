#!/usr/bin/python
import os,commands,cgi,cgitb,random
cgitb.enable()

print "content-type: text/html\n\n"

print ""

data=cgi.FieldStorage()

userid=data.getvalue("userid")

password=data.getvalue("password")
os=data.getvalue("os")
#size=data.getvalue("")
cpu=data.getvalue("cpu")
ram=data.getvalue("ram")
cl_ip = cgi.os.environ["REMOTE_ADDR"]
commands.getstatusoutput("sudo useradd "+userid)

commands.getstatusoutput("sudo echo "+password+" |sudo passwd  "+userid+" --stdin")

r=str(random.randint(5900,5999))

s=str(random.randint(7777,9999))

commands.getstatusoutput("sudo qemu-img create -f qcow2 -b ubuntu.qcow2 snap"+s+".qcow2")
commands.getstatusoutput('sudo virt-install --vnc --vnclisten='+cl_ip+' --vncport='+r+' --noautoconsole --name '+userid+' --ram '+ram+' --vcpu '+cpu+' --disk path=/var/lib/libvirt/images/ubuntu.qcow2 --import')

commands.getstatusoutput("sudo python /var/www/html/websockify-master/run -D "+s+"  "+cl_ip+":"+r)

# print  "<html>"
print '<a href="http://'+cl_ip+'/vnc/index.html?host='+cl_ip+'&port='+s+'">CLICK HERE</a>'
 #print "</html>"

print "===============================you are done========================="
