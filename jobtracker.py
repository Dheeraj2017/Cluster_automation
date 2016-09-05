#!/usr/bin/python2  -tt

import os

#####JOBTRACKER FUNCTION
def jobtracker(job,add):
#mapred-site
        f=open("/root/mapred-site.xml",'w')
        f.writelines('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>     
<!-- Put site-specific property overrides in this file. -->     
<configuration>
<property>
<name>mapred.job.tracker</name>
<value>%s:9002</value>
</property>
</configuration>'''%job)
        f.close()
#core site      
        f=open("/root/core-site.xml",'w')
        f.writelines('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>     
<!-- Put site-specific property overrides in this file. -->     
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://%s:9001</value>
</property>
</configuration>'''%add)
        f.close()
        x=os.system('scp /root/{core-site.xml,mapred-site.xml} root@%s:/etc/hadoop/'%job)
        #x=os.system("sshpass -p 'redhat' ssh -o StrictKeyHostChecking=no  root@%s  'scp /home/dheeraj/Desktop/ip/hadoop-project-master/hadoopdheeraj/{core-site.xml,mapred-site.xml}  root@%s:/etc/hadoop/   > /dev/null 2>/dev/null' "%job)
#command to start job tracker
        if x==0:
                print"files successfully created"

                os.system('ssh %s hadoop-daemon.sh start jobtracker'%job)
                #os.system("sshpass -p 'redhat' ssh -o StrictKeyHostChecking=no root@%s 'hadoop-daemon.sh start jobtracker >/dev/null 2> /dev/null'"%job)
                print "job tracker created on ip %s"%job
        else:
                print "error creating files on jobtracker"

