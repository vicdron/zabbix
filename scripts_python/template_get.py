#####################################################
#Busca todos os templates 
#####################################################

# importando a class zabbix-api
from zabbix_api import ZabbixAPI
import config

zapi = ZabbixAPI(server=config.url)
zapi.login (config.login, config.passwd)

#template = zapi.template.get({"output": ["name", "templateid"],"selectTriggers":["triggerids","description","priority","status"]})
template = zapi.template.get({"output": ["name", "templateid"]})

for i in template:
    
    template_nome = i['name']
    template1 = zapi.template.get({"output": "extend","filter": {"host": [template_nome]},"selectTriggers": ["triggerids",
        "description","priority","status"]})
        
    for x in template1:

       print(template_nome, "*", x["triggers"][0]["triggerid"], "*",x["triggers"][0]["description"], "*", )












#template = zapi.template.get({"output": ["host", "name", "templateid"]}) 
#for x in template:    #print hosts
#    # print (x)["hostid"], " * ", (x)["host"], " * ", (x)["name"], " * ", (x)["status"] #python 2.7
#    print(x["host"], "*", x["name"], "*", x["templateid"])


######################################  Buscando o id
#id = zapi.template.get({"output": "shorten", 
#                        "filter": { "host": "Template OS Linux"}})
# 
#output
#>>> id
#[{u'templateid': u'10001'}]