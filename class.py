
class car(object):
    def __init__(self, model, color, company, speed_limit):
     self.color = color
     self.company = company
     self.model = model
     self.speed_limit = speed_limit

    def start(self):
     print("started")

    def stop(self):
     print("stopped")

    def accelarate(self):
     print("accelarating")
     "accelarator functionality here"

    def change_gear(self,gear_type):
     print("gear_changed")
     "gear related functionality here"

audi = car("A6", "blue", "audi", "220")
print(audi.start())
print(audi.color)
    