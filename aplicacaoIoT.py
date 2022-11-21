#usar paho mqtt para tentar conexão via mosquitto
#hostname para contactar mosquitto -> hostname = "test.mosquitto.org"
#http://www.steves-internet-guide.com/into-mqtt-python-client/
#https://pypi.org/project/paho-mqtt/

fountain = False
presence = False
timer = 0
while True:
    option = input('escolha uma opcao:\n1-On/Off fonte\n2-Controles da fonte.\n3-Receber dados.\n')
    option = str(option)
    if(option == "1"):
        option2 = input('escolha uma opcao:\n1-Ligar fonte.\n2-desligar fonte.\n')
        if(option2=="1"):
            if(fountain==True): print('a fonte já estava ligada.\n')
            else:
                fountain = True
                print('fonte foi ligada!')
        elif(option2=="2"):
            if(fountain==False): print('a fonte já estava desligada.\n')
            else:
                fountain = False
                print('fonte foi desligada!')
    elif(option=="2"):
        option3 = input('escolha uma opcao de fonte:\n1-Por deteccao de presença\n2-Por temporizador.\n')
        if(option3=="1"):
            if(fountain==True):
                if(presence==True): print('modo de deteccao já estava ativado!.\n')
                else:
                    print('modo de deteccao ativado!.\n')
                    presence = True
                    timer = 0
            else: print('ative a fonte antes de selecionar essa opcao!.\n')
        elif(option3=="2"):
            if(fountain==True):
                timer = input('selecione o intervalo da fonte em segundos.\nobs: valor mínimo 30s.\n')
                time = int(timer)
                if(time<30):
                    print('valor '+timer+'eh invalido!\n')
                    timer = "0"
                else: print('timer de '+timer+' segundos foi estabelecido!\n')
            else: print('ative a fonte antes de selecionar essa opcao!\n')
                    
