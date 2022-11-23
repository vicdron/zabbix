
# importando a class zabbix-api
from zabbix_api import ZabbixAPI
import config

zapi = ZabbixAPI(server=config.url)
zapi.login (config.login, config.passwd)


#hostid = ('d', [13328,11053,15732])
hostid = open("/Users/victor/codigos/Workspace/Zabbix/hostid.txt")
linha =[line.strip() for line in hostid]
hostid.close()

for line in linha:
    items = zapi.item.get({"output": ["itemid", "name", "key_"],"hostids":line})

    for x in items:    #print hosts
        print(line, "*", ["itemid"], "*", x["name"], "*", x["key_"])

