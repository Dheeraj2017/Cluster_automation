#/usr/bin/python2  -tt
import os,sys
import time
'''
A primary requirment is that we need a fresh system (commodity system) 
1)Fresh installed system 
2)there is no specific software is install (or pre install ) because it will create some error while installation
3)thinks which are required for hadoop installation not pre install
   example: 
'''
def yum_install(ip_addr):
        a=os.system("sshpass -p 'redhat' ssh -o StrictKeyHostChecking=no  root@%s yum install nmap  -y > /dev/null  2> /dev/null"%ip_addr)
	
        c=os.system("sshpass -p 'redhat' ssh -o StrictKeyHostChecking=no  root@%s yum install java  -y > /dev/null  2> /dev/null"%ip_addr)
		
        d=os.system("sshpass -p 'redhat' ssh -o StrictKeyHostChecking=no  root@%s yum install jdk  -y > /dev/null  2> /dev/null"%ip_addr)
        e=os.system("sshpass -p 'redhat' ssh -o StrictKeyHostChecking=no  root@%s yum install hadoop  -y > /dev/null  2> /dev/null"%ip_addr)
        if a==0 :
                print 'succesfully installation of NMAP is done'
	else :
                print 'sorry some error in NMAP installation'
                time.sleep(3.0)
	if b==0:
		print 'Successfully installation of JAVA is done'
	else :
		print 'Sorry some error in JAVA installation'
		time.sleep(3.0)
	if c==0:
		print 'Successfully installation of JDK is done !!'
	else:
		print 'There is some error in JDK installation may be already installed'
		#print 'There is some error in Hadoop RPM installation !! maY be already installed!! check it out '
		time.sleep(3.0)
	if d==0:
		print 'Hadoop installation is complete go and made further work!!!'
	else :
		print 'There is some error in Hadoop RPM installation !! maY be already installed!! check it out '
