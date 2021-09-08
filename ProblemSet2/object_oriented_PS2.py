#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Question 1 


##Part 1
class Backpack:



    '''A backpack object class. Has a name, color, and a list of objects
    
    Attributes:
    name(str): The name of the backpacks owner
    color(str): The color of the backpack
    max_size(int): The maximum number of items that can fit inside
    contents(list): The contents of the backpack
    
    '''
    
     
    def __init__(self, name, color, max_size = 5): # constructor
        ''' Initializes the name, color, and max size attributes 

Parameters:
    name(str): The name of the backpacks owner
    color(str): The color of the backpack
    max_size(int): The maximum number of items that can fit inside
        '''
    
        self.name = name
        self.color = color
        self.max_size = max_size
        self.contents = []
        
        
    def put(self, item):
        if len(self.contents) < 5:
            self.contents.append(item)
        else:
            print("No room!")
            
            "Adds the item to the back pack as long as the size constraint is not yet met"
        

        
    def dump(self):
        self.contents.clear()
        
        '''Clears all contents from the backpack'''
        
        
 #Part 2   

class Jetpack(Backpack):
    """A jetpack object class. Inherits from the backpack class. Has a name, color, a list of objects, and fuel
    
    Attributes:
    name(str): The name of the jetpacks owner
    color(str): The color of the jetpack
    max_size(int): The maximum number of items that can fit inside
    fuel(int): The maximum level of fuel 
    contents(list): The contents of the jetpack
    """

    def __init__(self, name, color, max_size = 2, amount_fuel = 10): 
        ''' Initializes the name, color, max size, and fuel attributes 

Parameters:
    name(str): The name of the backpacks owner
    color(str): The color of the backpack
    max_size(int): The maximum number of items that can fit inside
    fuel(int): the maximum level of fuel 


        '''

        self.name = name
        self.color = color
        self.max_size = max_size
        self.fuel = fuel
        self.contents = []


    def fly(self, x): 
        if x <= self.fuel:
            self.fuel = self.fuel - x
        else:
            print("Not Enough Fuel!")
            
            '''Accepts a level of fuel consumption, x, and then deincrements total fuel by that amount.
        If the input is greater than what is left, it prints that there is not enough fuel'''
            
            
    def dump(self):
        self.contents.clear()
        self.amount_fuel.clear()
        
        '''Clears all contents and fuel from the jetpack'''
        
        


# In[ ]:




