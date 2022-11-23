#####################################################
#  Criando host no zabbix pela api
#####################################################

 # importando o zabbix-api
from zabbix_api import ZabbixAPI    
import config
import pandas as pd

zapi = ZabbixAPI(server=config.url)
zapi.login (config.login, config.passwd)


groupids = ['273']
groups = [{"groupid": groupid} for groupid in groupids] # for para adicionar mais de um grupo de host

# INTERFACE *************************************
# type (1 - agent, 2 snmp, 3 ipmi, 4 jmx)
# main (0 - not default, 1 - default)
# useip ( 0 - 0 - connect using host DNS name, 1 - 1 - connect using host IP address for this host interface.)
# dns (Can be empty if the connection is made via IP.)

info_interfaces = {
    "1": {"type": "agent", "id": "1", "port": "10050"},
    "2": {"type": "SNMP", "id": "2", "port": "161"},
}

try:
    create_host = zapi.host.create({
                 "host": "host_teste",
                 "interfaces": [{
                                    "type": info_interfaces['1']['id'], 
                                    "main": 1,
                                    "useip": 1,
                                    "ip": "192.168.3.1",
                                    "dns": "",
                                    "port": info_interfaces ['1']['port']
                                }],
                 "groups": groups, 
                 "templates":[{
                            "templateid": "10939"
                        }],      
        })

except (IndexError, ValueError):
     print ("erro ao adicionar host")
