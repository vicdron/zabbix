#####################################################
# Lista todas as triggers de um determinado hostid
#####################################################

# importando o zabbix-api
from os import read
from zabbix_api import ZabbixAPI
import config

zapi = ZabbixAPI(server=config.url)
zapi.login (config.login, config.passwd)

#hostid = ('d', [13328,11053,15732])
hostid = open("/home/victor/Workspace/Zabbix/hostid.txt")
linha =[line.strip() for line in hostid]
hostid.close()


#for line in linha:
#    triggers = zapi.triggerprototype.get({"output": ["triggerid", "description", "priority", "status"],"hostids":line})
#
#    for x in triggers:    #print hosts
#    # print (x)["hostid"], " * ", (x)["host"], " * ", (x)["name"], " * ", (x)["status"] #python 2.7
#        print(line, "*",  x["triggerid"], "*", x["description"], "*", x["priority"], "*", x["status"])

#triggers = zapi.triggerprototype.get({"output": ["triggerid", "description", "priority", "status"]})
triggers = zapi.triggerprototype.get({"output": ["triggerid", "description", "priority", "status"],"selectTags": "extend"})
for x in triggers:
    try:
        print(x["triggerid"], "*", x["description"], "*", x["priority"], "*", x["status"], "*", x["tags"][0]["value"])
    except (IndexError, ValueError):
        print(x["triggerid"], "*", x["description"], "*", x["priority"], "*", x["status"], "*")