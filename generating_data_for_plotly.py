from random import randint

class Die:
    def __init__(self,die_sides = 6):
        self.die_sides = die_sides
        
    def roll(self):
        return randint(1,self.die_sides)
        
die = Die()
data = []
for roll_num in range(100):
    x = die.roll()
    data.append(x)

print(data)
