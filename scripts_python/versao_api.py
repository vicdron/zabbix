##########################################
#  Busca informação da versão do Zabbix
##########################################

#importando o zabbixapi
from zabbix_api import ZabbixAPI
import config

#logon
zapi = ZabbixAPI(server=config.url)
zapi.login(config.login, config.passwd)

print ("Versão da API: ", zapi.api_version())
