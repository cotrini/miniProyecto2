from random import randint
from client import Client
from Queue import Queue
from cashier import Cashier
from math import ceil

def serveCustomer(cashier: Cashier, client):
    serveTime = 0
    for item in range(client[0]):
        serveTime += cashier.passItem()
    serveTime += cashier.receive(client[1])
    return serveTime

#Above simulation corresponding to 3 cashier and 3 lines model clints per minut in the line 3 aprox

def simulation1(simulationTime, clientsPerMinut):
    waitingTimeList = []
    cashier1 = Cashier()
    cashier2 = Cashier()
    cashier3 = Cashier()
    clientsQueue1 = Queue()
    clientsQueue2 = Queue()
    clientsQueue3 = Queue()
    for minut in range(simulationTime):
        if(minut % clientsPerMinut == 0):
            possibility = randint(0,1)  # possibility make new client into any client queue if is 1 , 0 makes nothing
            if(possibility == 1):
                queueElection = randint(1,3) #queue election put client into any queue
                for i in range(randint(1, 5)): #this for makes it possible for 1 to 5 people to arrive in line at that moment
                    if(queueElection == 1):
                        newClient = Client(minut)
                        clientsQueue1.enQueue((newClient.getItemsAmount(), newClient.getPayMethod(), newClient.getTimeStamp()))
                    elif(queueElection == 2):
                        newClient = Client(minut)
                        clientsQueue2.enQueue((newClient.getItemsAmount(), newClient.getPayMethod(), newClient.getTimeStamp()))
                    else:
                        newClient = Client(minut)
                        clientsQueue3.enQueue((newClient.getItemsAmount(), newClient.getPayMethod(), newClient.getTimeStamp()))
            else:
                pass    #makes nothing, nobody arrive to the line        
        if(not clientsQueue1.isEmpty() and not cashier1.getBusyStatus()):
            client = clientsQueue1.deQueue()
            waitingTimeList.append((minut - client[2]))
            cashier1.setBusyStatus(True)
            cashier1.setBusyTime(ceil(serveCustomer(cashier1, client)))
        elif(cashier1.getBusyStatus()):
            cashier1.timeChanger()

        if(not clientsQueue2.isEmpty() and not cashier2.getBusyStatus()):
            client = clientsQueue2.deQueue()
            waitingTimeList.append((minut - client[2]))
            cashier2.setBusyStatus(True)
            cashier2.setBusyTime(ceil(serveCustomer(cashier2, client)))
        elif(cashier2.getBusyStatus()):
            cashier2.timeChanger()

        if(not clientsQueue3.isEmpty() and not cashier3.getBusyStatus()):
            client = clientsQueue3.deQueue()
            waitingTimeList.append((minut - client[2]))
            cashier3.setBusyStatus(True)
            cashier3.setBusyTime(ceil(serveCustomer(cashier3, client)))
        elif(cashier3.getBusyStatus()):
            cashier3.timeChanger()
    print('The Average time in 3 cashier and three lines simulation per client is: ')
    print((sum(waitingTimeList)/len(waitingTimeList)), ' Minuts')
    print('Amount of clients served: ',len(waitingTimeList))
    print('Amount of clients not served: ',(clientsQueue1.size() + clientsQueue2.size() + clientsQueue3.size()))
    print(8*'_')

def simulation2(simulationTime, clientsPerMinut):
    waitingTimeList = []
    cashier1 = Cashier()
    cashier2 = Cashier()
    cashier3 = Cashier()
    clientsQueue= Queue()
    for minut in range(simulationTime):
        if(minut % clientsPerMinut == 0):
            possibility = randint(0,1)  # possibility make new client into any client queue if is 1 , 0 makes nothing
            if(possibility == 1):
                for i in range(randint(1, 5)): #this for makes it possible for 1 to 5 people to arrive in line at that moment
                    newClient = Client(minut)
                    clientsQueue.enQueue((newClient.getItemsAmount(), newClient.getPayMethod(), newClient.getTimeStamp()))
            else:
                pass    #makes nothing, nobody arrive to the line   

        if(not clientsQueue.isEmpty() and not cashier1.getBusyStatus()):
            client = clientsQueue.deQueue()
            waitingTimeList.append((minut - client[2]))
            cashier1.setBusyStatus(True)
            cashier1.setBusyTime(ceil(serveCustomer(cashier1, client)))
        elif(cashier1.getBusyStatus):
            cashier1.timeChanger()

        if(not clientsQueue.isEmpty() and not cashier2.getBusyStatus()):
            client = clientsQueue.deQueue()
            waitingTimeList.append((minut - client[2]))
            cashier2.setBusyStatus(True)
            cashier2.setBusyTime(ceil(serveCustomer(cashier2, client)))
        elif(cashier2.getBusyStatus):
            cashier2.timeChanger()

        if(not clientsQueue.isEmpty() and not cashier3.getBusyStatus()):
            client = clientsQueue.deQueue()
            waitingTimeList.append((minut - client[2]))
            cashier3.setBusyStatus(True)
            cashier3.setBusyTime(ceil(serveCustomer(cashier3, client)))
        elif(cashier3.getBusyStatus):
            cashier3.timeChanger()

       


    print('The Average time in 3 cashier and one line simulation per client is: ')
    print((sum(waitingTimeList)/len(waitingTimeList)), ' Minuts')
    print('Amount of clients served: ',len(waitingTimeList))
    print('Amount of clients not served: ',clientsQueue.size())
    print(8*'_')
    


for i in range(10):
    print(8*'--')
    print('Simulation ',i + 1)
    print(8*'--')
    simulation1(480, 36)
    simulation2(480, 36)
    print(8*'_')




























# def simulation1(clientsAmount ):
    
#     firstSimulationQueue = Queue()
#     secondSimulationQueue = Queue()
#     for i in range(clientsAmount):
#         myClient = Client()
#         firstSimulationQueue.enQueue((myClient.getItemsAmount(), myClient.getPayMethod())) #save information into queue in tuple type
#         secondSimulationQueue.enQueue((myClient.getItemsAmount(), myClient.getPayMethod()))

#     #This Section is for first simulation for 3 casher and 3 lines
#     firstCashierLine = Queue()
#     secondCashierLine = Queue()
#     thirdCashierLine = Queue()

#     while(not firstSimulationQueue.isEmpty()):
#         lineSelection = randint(1,3)
#         if(lineSelection == 1):
#             firstCashierLine.enQueue(firstSimulationQueue.deQueue())
#         elif(lineSelection == 2):
#             secondCashierLine.enQueue(firstSimulationQueue.deQueue())
#         else:
#             thirdCashierLine.enQueue(firstSimulationQueue.deQueue())


#     firstCashier = Cashier()
#     secondCashier = Cashier()
#     thirdCashier = Cashier()

#     totalClients = 0
#     clientsLine1 = 0 
#     clientsLine2 = 0
#     clientsLine3 = 0
#     waitTimeLine1 = 0
#     waitTimeLine2 = 0
#     waitTimeLine3 = 0
#     waitTimeAverage = 0

#     while( not firstCashierLine.isEmpty()):
#         client = firstCashierLine.deQueue()
#         waitTimeLine1 += serveCustomer(firstCashier, client)
#         clientsLine1 += 1
#         totalClients += 1
#         waitTimeAverage += waitTimeLine1 / clientsLine1
        

#     while( not secondCashierLine.isEmpty()):
#         client = secondCashierLine.deQueue()
#         waitTimeLine2 += serveCustomer(secondCashier, client)
#         clientsLine2 += 1
#         totalClients += 1
#         waitTimeAverage += waitTimeLine2 /clientsLine2

#     while( not thirdCashierLine.isEmpty()):
#         client = thirdCashierLine.deQueue()
#         waitTimeLine3 += serveCustomer(thirdCashier, client)
#         clientsLine3 += 1
#         totalClients += 1
#         waitTimeAverage += waitTimeLine3 /clientsLine3

#     print('SIMULATION 1 (3 CASHIERS 3 LINES)')
#     print( 8*'_')
#     print('Total Clients Simulation: ', clientsAmount )
#     print( 8*'_')
#     print('Total Clients Line 1: ', clientsLine1, 'Total wait time last client in the line: ', waitTimeLine1)
#     print( 8*'_')
#     print('Total Clients Line 2: ', clientsLine2, 'Total wait time last client in the line: ', waitTimeLine2)
#     print( 8*'_')
#     print('Total Clients Line 3: ', clientsLine3, 'Total wait time last client in the line: ', waitTimeLine3)
#     print( 8*'_')
#     print('Wait time average: ', waitTimeAverage)
#     print( 8*'_')
#     print( 8*'_')

#     #This Section is for second simulation for 3 cashier and 1 line 
#     waitTime = 0
#     waitTimeAverage = 0
#     while( not secondSimulationQueue.isEmpty()):
        
#         if(secondSimulationQueue.size()>=3):
#             client1 = secondSimulationQueue.deQueue()
#             client2 = secondSimulationQueue.deQueue()
#             client3 = secondSimulationQueue.deQueue()
#             waitTime += serveCustomer(firstCashier, client1)
#             waitTime += serveCustomer(firstCashier, client2)
#             waitTime += serveCustomer(firstCashier, client3)
            
        
#         elif(secondSimulationQueue.size() == 2):
#             client1 = secondSimulationQueue.deQueue()
#             client2 = secondSimulationQueue.deQueue()
#             waitTime += serveCustomer(firstCashier, client1)
#             waitTime += serveCustomer(firstCashier, client2)
#         else:
#             client1 = secondSimulationQueue.deQueue()
#             waitTime += serveCustomer(firstCashier, client1)

#     print('SIMULATION 2 (3 CASHIERS 1 LINE)')
#     print(8*'_')
#     print('Wait time last person in the line: ', waitTime)
#     print(8*'_')
#     print('Wait time average: ', (waitTime/clientsAmount))
#     print(8*'_')



   
        