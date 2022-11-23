from zabbix_api import ZabbixAPI
import time, config

zapi = ZabbixAPI(server=config.url)
zapi.login(config.login, config.passwd)


#hostid = ('d', [13328,11053,15732])
links = open("/Users/victor/workspace/zabbix/links.txt")
linha =[line.strip() for line in links]
links.close()

#for i in hostid[1]:
for line in linha:
    eventos = zapi.event.get ({
        "output": "extend",
        "selectHosts": ["hostid", "host"],   
        "selectRelatedObject": ["description", "lastchange"],
        "select_acknowledges": "extend",
        "hostids": line,                             
        "sortfield": ["eventid","clock"]})              

    for i in eventos:
        nomeHost = i["hosts"][0]["host"]
        dataEvento = time.strftime("%d-%m-%Y %H:%M:%S",time.localtime(float(i["clock"])))

        if i["value"] == "1":
            statusEvento = "INCIDENTE"

        else:
            statusEvento = "OK"
            triggers = zapi.trigger.get ({            
                                    "triggerids": i["relatedObject"]["triggerid"],
                                    "output": ["description"],
                                    "expandDescription": True
                                    })
        
            try:
                 print ('{0:20} | {1:15} | {2:72} | {3}'.format(dataEvento, nomeHost, triggers[0]["description"], statusEvento))
            except (IndexError, ValueError):
                print ("")


        #arquivo = open('novo_arquivo.txt', 'w')
        #if triggers[0]["description"] == ("Operational status was up (1) on interface VPN_DC_2.2" or
        #"Operational status was up (1) on interface VPN_DC_1.1"):
       
        #if triggers[0]["description"] == "Operational status was down (2) on interface VPN_DC_2.2":
        #    print ('{0:20} | {1:15} | {2:70} | {3:10} | {4:20} | {5}'
        #    .format(dataEvento, nomeHost, triggers[0]["description"], statusEvento, duracaoEvento, dataFinal))
        #
        #if triggers[0]["description"] == "Operational status was down (2) on interface VPN_DC_1.1":
        #    print ('{0:20} | {1:15} | {2:70} | {3:10} | {4:20} | {5}'
        #    .format(dataEvento, nomeHost, triggers[0]["description"], statusEvento, duracaoEvento, dataFinal))





