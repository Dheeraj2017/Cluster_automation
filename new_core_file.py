#/usr/bin/python2  -tt
import os
def new_core_file(q):
        nc = open('/root/Desktop/typical/datanode/core-site.xml','w')
        nc.writelines('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://%s:9001</value>
</property>
</configuration>
'''%q)
        nc.close()
        #os.system("scp /root/Desktop/typical/datanode/core-site.xml  root@%s:/etc/hadoop/"%k)

