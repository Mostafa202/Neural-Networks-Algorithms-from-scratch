
import numpy as np
import target
import math
class weight_matrix:
    def __init__(self,x,y):
        self.train_error=[]
        self.test_error=[]
        self.final_weight=[]
        self.lst=target.get_targets(np.array(y))
        self.y=y
        
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
        
        
    def create_weight_matrix(self,x,y):
        self.total=np.zeros((x.shape[1],y.shape[1]))
        for i in range(len(x)):
            self.total+=x[i,:].T*y[i,:]   
        self.final_weight=self.total
        return self.total
    def propagation(self,x,y):
        self.p=np.array(x)*np.array(y)
        return self.binary_activation(self.p.sum())
        
    def training(self,x,y):
        self.weight_matrix=self.create_weight_matrix(x,y)
        for i in range(len(x)):
            for j in range(len(self.weight_matrix[0])):
                y_hat=self.propagation(x[i,:],self.weight_matrix[:,j])
                self.train_error.append(0.5*((y[i,j]- y_hat)*(y[i,j]-y_hat)))
        
    def testing(self,x,y,weight_):
        new=[]
        for i in range(len(x)):
            for j in range(len(weight_[0])):
                y_hat=self.propagation(x[i,:],weight_[:,j])
                new.append(y_hat)
                self.test_error.append(0.5*((y[i,j]- y_hat)*(y[i,j]-y_hat)))
                
        return new
    
    def filter_targets(self,lst):
        
        for i in range(len(lst)):
            test=[]
            targets=[]
            counter=0
            for i in range(len(lst)):
                if counter==self.y.shape[1]:
                    targets.append(test)
                    counter=0
                    test=[]
                test.append(lst[i])
                counter+=1
            targets.append(test)
        return targets
            
      
     
    def ret_final_weight(self):
        return self.final_weight
    def ret_train_error(self):
        return self.filter_targets(self.train_error)
    def ret_test_error(self):
        return self.filter_targets(self.test_error)
    def ret_predicted_vals(self,x,y,weight_matrix):
        return self.filter_targets(self.testing(x,y,weight_matrix))
    



"""
x=np.matrix([[1,-1,-1,-1],[-1,1,-1,-1],[-1,-1,1,-1],[-1,-1,-1,1]])
y=np.matrix([[1,-1,-1],[1,-1,1],[-1,1,-1],[-1,1,1]])
"""

"""
import pandas as pd

dataset=pd.read_csv('weight.csv')
x=dataset.iloc[:,:-3].values
y=dataset.iloc[:,-3:].values
x=np.matrix(x)
y=np.matrix(y)


m=weight_matrix(x,y)
m.training(x,y)

print(m.ret_final_weight())
print(m.ret_train_error())
t=[]
t.append(m.ret_final_weight())
print(m.ret_predicted_vals(x,y,t[0]))
print(m.ret_test_error())
"""





















