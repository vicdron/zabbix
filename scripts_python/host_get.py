########################################################
#Busca todos os hosts com o nome, hostid e status e ip
########################################################

# importando a class zabbix-api
from zabbix_api import ZabbixAPI
import config

zapi = ZabbixAPI(server=config.url)
zapi.login (config.login, config.passwd)

hosts = zapi.host.get({"output": ["hostid", "host", "name", "status"]})  # "sortfied":"name" #ordenar por hostid

print ("HOSTID  *   HOST     *    NAME    *    STATUS     *     IP")

for x in hosts:    #print hosts
    # print (x)["hostid"], " * ", (x)["host"], " * ", (x)["name"], " * ", (x)["status"] #python 2.7
    hostinterface = zapi.hostinterface.get({"output": ["interfaceid", "dns", "ip"], "filter":{"hostid":[x["hostid"]]}})
    print(x["hostid"], "*", x["host"], "*", x["name"], "*", x["status"], "*", hostinterface[0]["ip"])

