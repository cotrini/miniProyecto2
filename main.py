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

def simulation1(simulationTime, clientsOnMinut):
    waitingTimeList = []
    cashier1 = Cashier()
    cashier2 = Cashier()
    cashier3 = Cashier()
    clientsQueue1 = Queue()
    clientsQueue2 = Queue()
    clientsQueue3 = Queue()
    for minut in range(simulationTime):
        if(minut % clientsOnMinut == 0):
            possibility = randint(0,1)  # possibility make new client into any client queue if is 1 , 0 makes nothing
            if(possibility == 1):
                for i in range(randint(1,8)): #this for makes it possible for 1 to 5 people to arrive in line at that moment
                    queueElection = randint(1,3)
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
    print('Waiting list of simulation 2: ',waitingTimeList)
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
                for i in range(randint(1, 8)): #this for makes it possible for 1 to 5 people to arrive in line at that moment
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
    print('Waiting list of simulation 2: ',waitingTimeList)
    print(8*'_')
    


for i in range(10):
    print(8*'--')
    print('Simulation ',i + 1)
    print(8*'--')
    simulation1(480, 5)
    simulation2(480, 5)
    print(8*'*')