from plotly.graph_objs import Bar,Layout
from plotly import offline
from random import randint
class Die:
    def __init__(self,num_sides=6):
        self.num_sides = num_sides
    def roll(self):
        return randint(1,self.num_sides)
    

die = Die()
results = []
for result in range(1000):
    value = die.roll()
    results.append(value)
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#visualizing the data
x_values = list(range(1,die.num_sides+1))
data = [Bar(x=x_values,y=frequencies)]

#configuration
x_config = {'title': "Values"}
y_config = {'title': "Occurance"}
my_layout = Layout(value = 'Relults which came after rolling a dice for 1000 times',xaxis=x_config,yaxis = y_config)
#plotting the graph
offiline.plot({'data':data, 'layout':my_layout}, filename ='d6.html')
