# importando a class zabbix-api
from os import read
from zabbix_api import ZabbixAPI
import config

zapi = ZabbixAPI(server=config.url)
zapi.login (config.login, config.passwd)

#hostid = ('d', [13328,11053,15732])
hostid = open("/Users/victor/Documents/Workspace/Zabbix/hostid.txt")
linha =[line.strip() for line in hostid]
hostid.close()

print ("HOSTID * HOST  *  NAME  *  STATUS_HOST * GROUPID * NAME_GROUP")
print ("")
#for i in hostid[1]:
for line in linha:
    hostgroup = zapi.hostgroup.get({"output": ["groupid", "name"],
    "hostids":line,"selectTags": "extend"})


    for x in hostgroup:    #print hosts
        hosts = zapi.host.get({"output": ["hostid", "host", "name", "status"], "filter":{"hostid":[line]}})
        hostinterface = zapi.hostinterface.get({"output": ["interfaceid", "dns", "ip"], "filter":{"hostid":[line]}})

        #tratamento de excesões devido a erros na busca por tags quando resultado é nulo
        try:
            print(hosts[0]["hostid"], "*", hosts[0]["host"], "*",hosts[0]["name"], "*",hosts[0]["status"], "*",
            x["groupid"], "*", x["name"] )

        except (IndexError, ValueError):
            print(hosts[0]["hostid"], "*", hosts[0]["host"], "*",hosts[0]["name"], "*",hosts[0]["status"], "*",
            x["groupid"], "*", x["name"])