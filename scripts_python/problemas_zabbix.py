"""
Mostra lista com problemas atuais
"""
#importando a API do ZAbbix
from zabbix_api import ZabbixAPI
import config

zapi = ZabbixAPI(server=config.url)
zapi.login (config.login, config.passwd)

#Obter uma lista de todos os problemas com a chamada tigger.get
triggers = zapi.trigger.get(only_true=1,
                        skipDependent=1,
                        monitores=1,
                        active=1,
                        output="extend",
                        expandDescription=1,
                        selectHosts=['host'],
                        )
# Faça outra consulta para descobrir quais problemas não são reconhecidos
unack_triggers = zapi.trigger.get(only_true=1,
                                skipDependent=1,
                                monitored=1,
                                active=1,
                                output="extend",
                                expandDescription=1,
                                selectHosts=['host'],
                                )
# irá fazer a interação com as Triggers encontradas
unack_triggers_ids = [t['triggerid'] for t in unack_triggers]

# interação para as desconhecidas
for t in triggers:
    t['unacknowledged'] = True if t['triggerid'] in unack_triggers_ids \
    else False

# Imprime lista contendo só triggers atuais
#for t in trigger:
#    if int (t['value']) == 1:
#        print ("{0} - {1} {2} ".format(t['hosts'][0]['host'],
#                                       t['description'],
#                                        '(Unack)' if t['unacknowledged'] else ''))
