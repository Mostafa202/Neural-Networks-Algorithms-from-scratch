
import numpy as np
import pandas as pd
import target
import math
class perceptron:
    def __init__(self,x,y,bias_value=None,bias=None,weights=None,learning_rate=None,epochs=None):
        if bias_value is None:
            self.bias_value=1
        else:
            self.bias_value=bias_value
            
        if bias is None:
            self.bias=0
        else:
            self.bias=bias
            
        if weights is None:
            self.weights=np.zeros(len(x[0]))
        else:
            self.weights=weights
                   
        if learning_rate is None:
            self.learning_rate=1
        else:
            self.learning_rate=learning_rate

        self.epochs=epochs
        self.errors=[]
        self.errors_test=[]
        self.errors_epochs=[]
        self.insert_weights=[]
        self.insert_final_weights=[]
        self.lst=target.get_targets(y)

    #@staticmethod
    def activation(self,net):
        if(len(self.lst)==2):
            if net>0:
                return self.lst[1] 
            else:
                return self.lst[0]
        elif(len(self.lst)==3):
            if net>0:
                return self.lst[2]
            elif net == 0:
                return self.lst[1]
            else:
                return self.lst[0]
        else:
            return (1/(1+math.exp(-net)))
            
        
    def propagation(self,x):
        return ((self.weights*x)).sum()+(self.bias*self.bias_value)
    
    def learning(self,x,y):
            self.y_hat=self.activation(self.propagation(x))
            self.error=y-self.y_hat
            return self.error,self.y_hat
        
    def update_weights(self,x,y):
            self.error,self.y_hat=self.learning(x,y)
            self.errors.append(.5*((self.error)*(self.error)))
            
            self.insert_weights.append("weights : "+str(self.weights)+" :: Bias: "+str(self.bias)+"")
            
            if(self.error!=0):              
                self.weights+=(self.learning_rate*self.error*x)
                self.bias+=self.learning_rate*self.error*self.bias_value
                
            return self.y_hat
    
                
    def training(self,x,y):
        self.check=0
        for i in range(len(x)):
            self.new=self.update_weights(x[i,:],y[i])
            if(self.new!=y[i]):
                self.check=1
        return self.check
        
            #print('new weights: ',self.new,' bias: ',self.bias)
         
    def testing(self,x,y):
        hat=[]
        for i in range(len(x)):
            error,y_hat=self.learning(x[i,:],y[i])
            self.errors_test.append(0.5*(error*error))
            hat.append(y_hat)
        return hat
    
    def loop(self,x,y,num):
        for i in range(num):  
            
            self.tr=self.training(x,y)
            self.insert_final_weights.append(self.insert_weights)
            self.errors_epochs.append(np.array(self.errors).sum()/len(self.errors))
            self.errors=[]
            self.insert_weights=[]
            if(self.tr==0):
                break
            
    def ret_weights(self):
        return self.insert_final_weights

    def ret_errors_epochs(self):
        return np.array(self.errors_epochs)
    
    def predicted_vals(self,x,y):
        return self.testing(x,y)
    def ret_test_errors(self):
        return np.array(self.errors_test).sum()/len(self.errors_test)
    def ret_last_weights(self):
        return self.weights,self.bias

                    
    def call(self,x,y,x2,y2):
        self.loop(x,y,self.epochs)


    
  
    

"""   
   
x=np.full((3,3),[[0,0,1],[1,1,1],[1,0,1]])
y=np.full((3,1),[[0],[1],[1]])
x2=np.full((1,3),[[0,1,1]])
y2=np.full((1,1),[[0]])
"""


"""
dataset=pd.read_csv('project_data.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1:].values

from sklearn.preprocessing import*
s=StandardScaler()
x=s.fit_transform(x)
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size = 0.3, random_state = 0)

p=perceptron(x,y,1,0,[0,0,0,0,0,0,0],1,10)

p.call(train_x,train_y,test_x,test_y) 

print(p.ret_weights())
print(p.ret_errors_epochs())
print(p.predicted_vals(test_x,test_y))
print(p.ret_test_errors())

"""
        
        
    



















