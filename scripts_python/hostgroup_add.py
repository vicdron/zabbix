#####################################################
#  Adicionar grupos de hosts a hosts
#####################################################

# importando o zabbix-api
from zabbix_api import ZabbixAPI
import config

zapi = ZabbixAPI(server=config.url)
zapi.login (config.login, config.passwd)

hostid = open("/Users/victor/Documents/Workspace/Zabbix/hostid.txt")
linha =[line.strip() for line in hostid]
hostid.close()

#hosts = zapi.hostgroup.massadd({"groups":[{"groupid":"570"}],"hosts":[{"hostid":"19034"}]})

for line in linha:
    hosts = zapi.hostgroup.massadd({"groups":[{"groupid":"587"}],"hosts":[{"hostid":line}]})
