#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import string
import time
import datetime
import MySQLdb
import redis,json
import logging
import logging.config

def cur_file_dir():
    return os.path.split(os.path.realpath(__file__))[0]

# redisip = '172.22.131.42:6379'   

def check_redis(redisip):
    try:
        r=redis.StrictRedis(host=redisip.split(':')[0],port=int(redisip.split(':')[1]),db=0,socket_timeout=3,charset='utf-8') 
        allkeys = r.info(section="All").keys()
        sectionkeys=[]
        
        section_Server=r.info(section="Server")
        print u"[section_Server_服务器信息]:\r"
        for i in sorted(section_Server.keys()):
            print "%s : %s"%(i,section_Server[i])
            sectionkeys.append(i)
            
        section_Clients=r.info(section="Clients")
        print u"\r\n[section_Clients_客户端信息]:\r"
        for i in sorted(section_Clients.keys()):
            print "%s : %s"%(i,section_Clients[i])
            sectionkeys.append(i)

        section_Memory=r.info(section="Memory")
        print u"\r\n[section_Memory_内存信息]:\r"
        for i in sorted(section_Memory.keys()):
            print "%s : %s"%(i,section_Memory[i])
            sectionkeys.append(i)         
        
        section_CPU=r.info(section="CPU")
        print u"\r\n[section_CPU_ CPU 计算量统计信息]:\r"
        for i in sorted(section_CPU.keys()):
            print "%s : %s"%(i,section_CPU[i])
            sectionkeys.append(i)
            
        section_Persistence=r.info(section="Persistence")
        print u"\r\n[section_Persistence_RDB 和 AOF 的相关信息]:\r"
        for i in sorted(section_Persistence.keys()):
            print "%s : %s"%(i,section_Persistence[i])
            sectionkeys.append(i)
        
        section_Replication=r.info(section="Replication")
        print u"\r\n[section_Replication_主/从复制信息]:\r"
        for i in sorted(section_Replication.keys()):
            print "%s : %s"%(i,section_Replication[i])
            sectionkeys.append(i)
        
        section_Keyspace=r.info(section="Keyspace")
        print u"\r\n[section_Keyspace_数据库相关的统计信息]:\r"
        for i in sorted(section_Keyspace.keys()):
            print "%s : %s"%(i,section_Keyspace[i])
            sectionkeys.append(i)
            
        section_Stats=r.info(section="Stats")
        section_Stats_2=r.info(section="Stats")
        print u"\r\n[section_Stats_一般统计信息]:\r"        
        for i in sorted(section_Stats.keys()):
            print "%s : %s"%(i,section_Stats[i])
            sectionkeys.append(i)
        print "current_commands_processed : %s"%(int(section_Stats_2['total_commands_processed'] - section_Stats['total_commands_processed']))        
        
        section_Commandstats=r.info(section="Commandstats")
        print u"\r\n[section_Commandstats_命令统计信息]:\r"
        for i in sorted(section_Commandstats.keys()):
            print "%s : %s"%(i,section_Commandstats[i])
            sectionkeys.append(i)
            
        section_Cluster=r.info(section="Cluster")
        print u"\r\n[section_Cluster_集群信息]:\r"
        for i in sorted(section_Cluster.keys()):
            print "%s : %s"%(i,section_Cluster[i])
            sectionkeys.append(i)        

        for i in allkeys:
            if i not in sectionkeys:
                print "other keys : %s"%i
          
    except Exception, info:
        print str(info)      

if __name__ == "__main__":
    check_redis(sys.argv[1])
    # main()