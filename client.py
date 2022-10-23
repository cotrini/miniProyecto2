from random import randint
from random import gauss

#this class simulates the behavior of a customer, be it from a supermarket
class Client:

    def __init__(self, time):
        self.__itemsAmount = abs(int(gauss(22.6, 15.99)))
        self.__payMethod = randint(1,2) #This attribute contain 1 for cash or 2 for card
        self.__timeStamp = time

    def toString(self):
        print(self.__itemsAmount)
        print(self.__payMethod)
        print(8*'-')

    def getItemsAmount(self):
        return self.__itemsAmount

    def getPayMethod(self):
        return self.__payMethod

    def waitingTime(self, actualTime):
        return actualTime - self.__timeStamp

    def getTimeStamp(self):
        return self.__timeStamp



