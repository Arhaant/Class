class Car:
    def __init__(self,model,color,company):
        self.model = model
        self.color = color
        self.company = company
    def start(self):
        print('Car has started: ')
    def speed(self,value):
        print('The car speed is ', value)

c1 = Car('M2','Blue','BMW')
print(c1.model)
print(c1.company)
c1.start()
c1.speed(60)


        