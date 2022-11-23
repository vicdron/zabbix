##############################################################
#  Busca as interfaces dos hosts com o interfaceid, dns e ip
#############################################################

# importando o zabbix-api
from zabbix_api import ZabbixAPI
import config

zapi = ZabbixAPI(server=config.url)
zapi.login (config.login, config.passwd)


hostinterface = zapi.hostinterface.get({"output": ["interfaceid", "dns", "ip"]})

for x in hostinterface:  
    print(x["interfaceid"], "*", x["dns"], "*", x["ip"])