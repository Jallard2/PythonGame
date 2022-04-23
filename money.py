class moneyFunctions():
    def __init__(self):
        self.money = -1
    
    def setMoneyAmount(self, amount):
        self.money = amount
    
    def getMoneyAmount(self):
        return self.money

    def purchaseUpgrade(self, cost:int):
        self.money -= cost
        return self.money
    
