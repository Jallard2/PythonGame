class idle:
    def __init__(self):
        self.FPS = 60
        self.amountPerIdle = -1
    
    def setAmountPerIdle(self, amount:int):
        self.amountPerIdle = amount
    
    def getAmountPerIdle(self):
        return self.amountPerIdle