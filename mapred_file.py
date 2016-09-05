#/usr/bin/python2  -tt
import os
#jobtracker entry is done here
def mapred_file(ip_addr):
        mobj=open('mapred-site.xml','w')
        mobj.writelines('''
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>%s:9002</value>
</property>
</configuration>
'''%ip_addr)
        mobj.close()
        os.system("sshpass -p 'redhat' ssh -o StrictKeyHostChecking=no  root@%s  'scp /home/dheeraj/Desktop/ip/hadoop-project-master/hadoopdheeraj/mapred-site.xml  root@%s:/etc/hadoop/   > /dev/null' "%ip_addr)
