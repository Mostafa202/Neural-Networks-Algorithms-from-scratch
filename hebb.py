
import numpy as np
import matplotlib.pyplot as plt
import target
import math
class hebb:
    def __init__(self,x,y,bias_value=None,bias=None,weight=None):
        if weight is None:
            self.weight=np.zeros(len(x[0]))
        else:
            self.weight=weight
            
        if bias is None:
            self.bias=np.zeros(1)
        else:
            self.bias=bias
        if bias_value is None:
            self.bias_value=1
        else:
            self.bias_value=bias_value
        self.insert_weights=[]
        self.errors=[]
        self.test_errors=[]
        self.lst=target.get_targets(y)
        

    #@staticmethod
    def binary_activation(self,net):
        
        if(len(self.lst)==2):
            if net>=0:
                return self.lst[1]
       
            else:
                return self.lst[0]
            
        elif(len(self.lst)==3):
    
            if net>0:
                return self.lst[2]
            elif net==0:
                return self.lst[1]
            else:
                return self.lst[0]
        else:
            return (1/(1+math.exp(-net)))
            
        
    def activation_feedforward(self,x):

        return self.binary_activation((x*self.weight).sum()+(self.bias_value*self.bias))
   
    
    def learning(self,x,y):
        w="Weights:"+str(self.weight)+" Bias:"+str(self.bias)
        self.insert_weights.append(w)
        self.weight+=(x*y)
        self.bias+=y
    
    
    def training(self,x,y):
        for i in range(len(x)):
            y_hat=self.activation_feedforward(x[i,:])

            self.errors.append(0.5*((y[i]-y_hat)*(y[i]-y_hat)))
            self.learning(x[i,:],y[i])
        w="Weights:"+str(self.weight)+" Bias:"+str(self.bias)
        self.insert_weights.append(w)
        
            
    def testing(self,x,y):
        hat=[]
        for i in range(len(x)):
            y_hat=self.activation_feedforward(x[i,:])
            self.test_errors.append(0.5*((y[i]-y_hat)*(y[i]-y_hat)))
            hat.append(y_hat)
        return hat
    
    def ret_weights(self):
        return self.insert_weights
    
    def ret_final_weight(self):
        return self.weight,self.bias
    
    def ret_training_error(self):
        return self.errors
        
    def ret_predicted_vals(self,x,y):
        return(self.testing(x,y))
        
    def ret_test_error(self):
        return np.array(self.test_errors).sum()/len(self.test_errors)
            
    def call(self,x,y):
        self.training(x,y)

        
        
        
"""  
x=np.full((4,2), [[1,1],[1,-1],[-1,1],[-1,-1]])
y=np.full((4,1), [[1],[-1],[-1],[-1]])


h=hebb(x,y,1,0,[0,0])
h.call(x,y,x,y)


print(h.ret_weights())
print(h.ret_final_weight())
print(h.ret_training_error())
print(h.ret_predicted_vals(x,y))
print(h.ret_test_error())

"""


