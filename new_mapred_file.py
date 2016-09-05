#!/usr/bin/python2  -tt
import os
def new_mapred_file(q):
        nj = open('/root/Desktop/typical/datanode/mapred-site.xml','w')
        nj.writelines('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>%s:9002</value>
</property>

</configuration>
'''%q)
        nj.close()
        #os.system("scp /root/Desktop/typical/datanode/mapred-site.xml  root@%s:/etc/hadoop/"%k)
