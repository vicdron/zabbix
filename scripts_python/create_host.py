############################################################
#  Cadastro de hosts automáticos no zabbix utilizando API
###########################################################

 # importando o zabbix-api
from zabbix_api import ZabbixAPI    
import config
import pandas as pd

zapi = ZabbixAPI(server=config.url)
zapi.login (config.login, config.passwd)
tabela = pd.read_excel("/Users/victor/workspace/zabbix/cadastro_host.xlsx")
print(tabela)

host = tabela["HOST"]
name = tabela["NAME"]
ips = tabela["IP"]
groupids = tabela['GROUPID']
#groupids  = ['273','273']
templates = tabela["TEMPLATEID"]
#porta = tabela ["Porta"]
#tipo = tabela ["Type"]
cont = tabela ["Contador"]

#groupids = ['00', '01']
#groups = [{"groupid": groupid} for groupid in groupids] # for para adicionar mais de um grupo de host

def host_agent (tabela):
    for x in cont:
        try:
            create_host = zapi.host.create({
                        "host": host[x], 
                                "status": 1,    # Status 0 = Ativo, 1 = Inativo
                                "name": name[x],
                               # "proxy_hostid": "", 
                        "interfaces":[{
                            "type": 1,  # type (1 - agent, 2 snmp, 3 ipmi, 4 jmx)
                            "main": 1,  # main (0 - not default, 1 - default)
                            "useip": 1, # useip ( 0 - 0 - connect using host DNS name, 1 - 1 - connect using host IP address for this host interface.)
                            "ip": ips[x],
                            "dns": "",  # dns (Can be empty if the connection is made via IP.)
                            "port": 10050,
                        }],
                        "groups":[{
                            "groupid": int(groupids[x])}], 
                        "templates":[{
                            "templateid": int(templates[x])
                        }],      
                    })  
            print (host[x], "cadastrado com sucesso!!")      
        except (IndexError, ValueError):
            print ("Erro na tentativa de cadastrar o host")

def host_snmp (tabela):
    for x in cont:
        try:
            create_host = zapi.host.create({
                        "host": host[x], 
                                "status": 1,    # Status 0 = Ativo, 1 = Inativo
                                 "name": name[x],
                               # "proxy_hostid": "",
                        "interfaces":[{
                            "type": 2,  # type (1 - agent, 2 snmp, 3 ipmi, 4 jmx)
                            "main": 1,  # main (0 - not default, 1 - default)
                            "useip": 1, # useip ( 0 - 0 - connect using host DNS name, 1 - 1 - connect using host IP address for this host interface.)
                            "ip": ips[x],
                            "dns": "",  # dns (Can be empty if the connection is made via IP.)
                            "port": 161,
                            "details":[{ 
                                "version" : 3,
                                "bulk" : 0,
                                "securityname": "{$USUARIO}", 
                                "contextname" :  "",
                                "securitylevel": 2,
                                "authpassphrase":"{$SENHA}",
                                "privpassphrase":"{$SENHA2}",
                                "authprotocol": 1,
                                "privprotocol": 1,
                            }] 
                        }],
                        "groups":[{
                            "groupid": int(groupids[x])}], 
                        "templates":[{
                            "templateid": 21667
                        }],      
                    })  
            print (host[x], "cadastrado com sucesso!!")      
        except (IndexError, ValueError):
            print ("erro ao adicionar host")    

host_agent(tabela)
#host_snmp(tabela)

