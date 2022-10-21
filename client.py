from random import randint

#this class simulates the behavior of a customer, be it from a supermarket
class Client:

    def __init__(self, time):
        self.__itemsAmount = randint(1, 35)
        self.__payMethod = randint(1,2) #This attribute contain 1 for cash or 2 for card
        self.__timeStamp = time

    def toString(self):
        print(self.__itemsAmount)
        print(8*'-')
        print(self.__payMethod)

    def getItemsAmount(self):
        return self.__itemsAmount

    def getPayMethod(self):
        return self.__payMethod

    def waitingTime(self, actualTime):
        return actualTime - self.__timeStamp

    def getTimeStamp(self):
        return self.__timeStamp



