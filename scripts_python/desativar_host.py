#####################################################
#  Ativar / Desativar host
#####################################################

# importando a class zabbix-api
from zabbix_api import ZabbixAPI
import config

zapi = ZabbixAPI(server=config.url)
zapi.login (config.login, config.passwd)

hosts = zapi.host.update({"hostid": "000000", "status": "1"})    # DESATIVAR
hosts = zapi.host.update({"hostid": "000000", "status": "0"})    # ATIVAR



