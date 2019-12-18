sikkerhedsmargin=3
reparationer=0.5
sm1=0.35
sm2=0.2
start = True
while start == True:
    output = float(input("Indtast Output Power i dB:"))
    sens = float(input("Indtast Recieve sensitivity i dBm:"))
    bruttooverskud = output-sens
    print ("Bruttooverskud =",output-sens, "dB")

    konnekter = float(input("Indtast antal konnekteringer:"))
    konnekter = konnekter*0.5
    splids = float(input("Indtast antal splidsninger:"))
    splids = splids*0.1
    meter = float(input("Indtast kilometer fiber:"))
    metode = int(input("Indtast om det er 1310nm(0.35 dB/km) fiber (0) eller 1550nm(0.2 dB/km) fiber (1)"))

    if metode==0:
        dbnm = 0.35*meter
        linkmargin = bruttooverskud-konnekter-splids-dbnm
        nettooverskud = linkmargin-sikkerhedsmargin-reparationer
        if nettooverskud >=0:
            print (nettooverskud, "dB")
            print ("Godkendt")
            print ("_______________________________________")
        elif nettooverskud <0:
            print (nettooverskud, "dB")
            print ("Fejl")
            print ("_______________________________________")
        
    if metode==1:
        dbnm = 0.2*meter
        linkmargin = bruttooverskud-konnekter-splids-dbnm
        nettooverskud = linkmargin-sikkerhedsmargin-reparationer
        if nettooverskud >=0:
            print (nettooverskud, "dB")
            print ("Godkendt")
            print ("_______________________________________")
        elif nettooverskud <0:
            print (nettooverskud, "dB")
            print ("Fejl")
            print ("_______________________________________")
           
    svar = int(input("Vil du prøve igen? 1)Ja eller 2)Nej:"))
    
    if svar == 1:
        start = True
    else:
        start = False
        
