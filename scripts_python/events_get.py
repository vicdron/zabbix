from zabbix_api import ZabbixAPI
import time, config

zapi = ZabbixAPI(server=config.url)
zapi.login(config.login, config.passwd)

eventos = zapi.event.get ({
        "output": "extend",
        "selectHosts": ["hostid", "host"],    
        "groupids": "558",                                      # ID do grupo de host
        "selectRelatedObject": ["description", "lastchange"],
        "select_acknowledges": "extend",
        "time_from": "1630368000",                              # data inicial no formato timestamp
        "time_till": "1630454399",                              # data final no formato timestamp
        "sortfield": ["eventid","clock"],
        "sortorder": "DESC"
})

print ('{0:20} | {1:15} | {2:72} | {3:10} | {4}'                 #número da coluna e tamanho 
    .format("Data", "Nome do host", "Descrição do evento", "Status", "Duração"))
print ("")
for i in eventos:
        nomeHost = i["hosts"][0]["host"]
        dataEvento = time.strftime("%d-%m-%Y %H:%M:%S",time.localtime(float(i["clock"])))
        dataFinal = time.strftime("%d-%m-%Y %H:%M:%S",time.localtime(float(i["relatedObject"]["lastchange"]))) 

    
        if i["value"] == "1":
            duracao = float(i["relatedObject"]["lastchange"]) - float(i["clock"]) 
            statusEvento = "OK"

        else:
            duracao =  time.time() - float(i["relatedObject"]["lastchange"]) 
            statusEvento = "INCIDENTE"


        triggers = zapi.trigger.get ({            
                                    "triggerids": i["relatedObject"]["triggerid"],
                                    "output": ["description"],
                                    "expandDescription": True
                                    })

        pegadia = "{0.tm_yday}".format(time.gmtime(duracao))
        dia = int(pegadia) - 1
        horaMinuto = "d {0.tm_hour}h {0.tm_min}m {0.tm_sec}s".format(time.gmtime(duracao))
        duracaoEvento = str(dia)+str(horaMinuto)

        #print ('{0:20} | {1:15} | {2:72} | {3:10} | {4}'.format(dataEvento, nomeHost, triggers[0]["description"], statusEvento, duracaoEvento))
        #arquivo = open('novo_arquivo.txt', 'w')
        #if triggers[0]["description"] == ("Operational status was up (1) on interface VPN_DC_2.2" or
        #"Operational status was up (1) on interface VPN_DC_1.1"):
       
        if triggers[0]["description"] == "Operational status was down (2) on interface VPN_DC_2.2":
            print ('{0:20} | {1:15} | {2:70} | {3:10} | {4:20} | {5}'
            .format(dataEvento, nomeHost, triggers[0]["description"], statusEvento, duracaoEvento, dataFinal))
        
        if triggers[0]["description"] == "Operational status was down (2) on interface VPN_DC_1.1":
            print ('{0:20} | {1:15} | {2:70} | {3:10} | {4:20} | {5}'
            .format(dataEvento, nomeHost, triggers[0]["description"], statusEvento, duracaoEvento, dataFinal))





