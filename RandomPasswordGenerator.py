#!/usr/bin/env python
# coding: utf-8

# In[61]:


import string
import random


# In[62]:


class Characters:    
    def _symbols(self):
        symbols = "! ` $ % ^ & * ( ) _ - + = # ~ } ] { [ : ; ' ] } < , > . / * |"
        symbols = symbols.split()
        return symbols
    
    def _numbers(self):
        numbers = "0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5".split()
        return numbers
    
    def _capital_letters(self):
        caps = list(string.ascii_uppercase)
        return caps
        
    def _small_letters(self):
        small = list(string.ascii_lowercase)         
        return small


# In[63]:


class Password_generator:
    
    def password(self, value):        
        character = Characters()
        numbers = character._numbers()
        capital_letters = character._capital_letters()
        small_letters = character._small_letters()
        symbols = character._symbols()
        characters = [numbers, capital_letters, small_letters, symbols]
        password = ""
        for passw in range(value):
            index1 = random.randint(0, 3)
            index2 = random.randint(0, 25)
            password += str(characters[index1][index2])
        return password
    
   
        


# In[64]:


def main():
    value = int(input("How long do you want your password to be: "))

    if value < 1: 
        raise Exception("Would not accept a password length less than 1!")

    gene = Password_generator()
    return gene.password(value)


# In[ ]:




