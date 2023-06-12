#!/usr/bin/env python
# coding: utf-8

# In[164]:


class Bank():
    
    def __init__(self,balance = 0,owner = 'Ndanga'):
        self.balance = balance
        self.owner = owner
        
    def __str__(self):
        
        owner = self.owner
        balance = str(self.balance)
        
        return(f'Account holder: {owner}, Avail. Balance : {balance}')
    
    def deposit(self,amount):
        self.balance = round((self.balance + amount),2)
        
        print(f' you have successfully deposited ${amount} , your new balance is ${self.balance}')
    
    def withdraw(self,amount):
        
        if self.balance >=amount*(1.07):
            self.balance = round((self.balance - amount),2)*0.93
            print(f'you have successfully withdrawn ${amount} , your new balance is ${self.balance}')
        else:
            print(f' You cannot withdraw ${amount}, you only have ${self.balance} available')
            
            


# In[165]:


account =  Bank()


# In[172]:


account.withdraw(10.00)


# In[171]:


print(account)


# In[ ]:




