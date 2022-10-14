from random import uniform

# This class simulates the behavior of a cashier of some entity, financial, commercial or of any kind
class Cashier:

    def __init__(self):
        self.__busyTime = 0
        self.__busyStatus = False

    #This function simulate query, items or transaction from the client or user to cashier or employee
    def passItem(self):
        return uniform(0.1, 1.0) # In minutos

    #This function simulate one action from client to cashier, collect money, ask for qualification, or do nothing
    def receive(self, payMethod):
        if(payMethod == 1):
            return uniform(1, 5)
        else:
            return uniform(0.5, 5)

    def setBusyStatus(self, status):
        self.__busyStatus = status

    def timeChanger(self): #this function reduce busy time and change the busy status when time is near to cero
        self.__busyTime -= 1
        if(self.__busyTime <= 0):
            self.setBusyStatus(False) 

    def setBusyTime(self, newTime): #this function set time to this cashier is busy
        self.__busyTime = newTime

    def getBusyStatus(self):   #True when this cashier is busy
        return self.__busyStatus

 
