#!/usr/bin/python2 -tt

import os,sys
def client(add,name):
        #CORE-SITE.XML
        f=open("/root/Desktop/core-site.xml",'w')
        f.writelines(''' <?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>     
<!-- Put site-specific property overrides in this file. -->     
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://%s:9001</value>
</property>
</configuration>'''%name)
        f.close()

