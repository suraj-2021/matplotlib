# Molecular Motion -- Simulating a path of pollen grain in a drop of water
from random import choice
import matplotlib.pyplot as plt

class PollenMotion:
    def __init__(self,num_points= 50_0000):
        self.num_points = num_points
        
        self.x_values=[0]
        self.y_values=[0]
    
    def random_float(self):
       while len(self.x_values) <self.num_points:    
           x_direction = choice([1,-1])
           x_distance = choice([0,1,2,3,4])
           x_steps = x_direction*x_distance
           
           y_direction = choice([1,-1])
           y_distance = choice([0,1,2,3,4])
           y_steps = y_direction*y_distance
           
             
           x = self.x_values[-1]+x_steps
           y =self.y_values[-1]+ y_steps
           
           self.x_values.append(x)
           self.y_values.append(y)

           
motion = PollenMotion()
motion.random_float()
fig,ax = plt.subplots(figsize=(15, 9))
plt.style.use("fivethirtyeight")
ax.scatter(motion.x_values, motion.y_values,c='green',s=5)
plt.show()
