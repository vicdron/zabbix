#####################################################
# Lista todas as triggers de um determinado hostid
#####################################################

# importando a class zabbix-api
from os import read
from zabbix_api import ZabbixAPI
import config

zapi = ZabbixAPI(server=config.url)
zapi.login (config.login, config.passwd)

#hostid = ('d', [13328,11053,15732])
hostid = open("/home/victor/Workspace/Zabbix/hostid.txt")
linha =[line.strip() for line in hostid]
hostid.close()

#for i in hostid[1]:
for line in linha:
    triggers = zapi.trigger.get({"output": ["triggerid", "description", "priority", "status"],"hostids":line})

    for x in triggers:    #print hosts
    # print (x)["hostid"], " * ", (x)["host"], " * ", (x)["name"], " * ", (x)["status"] #python 2.7
        print(line, "*",  x["triggerid"], "*", x["description"], "*", x["priority"], "*", x["status"])

