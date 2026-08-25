class Car:
    def __init__(self):
        self.acc = False 
        self.brk = False
        self.clutch = False
#--------------------------------------------------        
    def engine(self):
        self.acc = True
        self.clutch = True
        print("car started...")
    #This part was abstraction
#---------------------------------------------------
c1 = Car()
c1.engine()