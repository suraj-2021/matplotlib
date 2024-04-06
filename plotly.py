Rolling two dices and plotting the result using PLOTLY

#creating a file name die.py

#die.py
from random import randint
class Die:
     def __init__(self,num_sides=8):
         self.num_sides = num_sides
    def roll(self):
          return randint(1,numsides)

#next create a different file named data_visual.py

#data_visual.py

from pyplot.bar_objs import Bar, Layout
from pyplot import offiline
from die import Die

die1 = Die()
die2 = Die()

result = []
for num in range(1000):
      value = die1.roll() + die2.roll()
      result.append(value)

max_sides = []
for x in range(1,die1.num_sides+1):
          max_side = die1.roll()+die2.roll()
          max_sides.append(max_side)

frequencies = [ ]
for x in range(len(2,die1.max_sides+1))
      frequency = result.count(x)
      frequencies.append(frequency)


x_values = list(len(1, num_sides+1))
data = [Bar(x= x_values,y = frequencies)]

x_axis_config = {"value": Number Sides}
y_axis_config = {"occurance": Appearing in the roll}
my_layout = Layout(value = 'Rolling two dices for 5000 times', xaxis = x_axis_config, yaxis = y_axis_config)

offline.plot({"data": data, "layout": my_layout}, filename= 'd6.html')
