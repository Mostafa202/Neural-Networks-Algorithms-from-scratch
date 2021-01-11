


import numpy as np
import target
import math
class weight_matrix:
    def __init__(self,x,y,learning_rate,epochs,matrix):
        self.train_error=[]
        self.test_error=[]
        self.final_weight=[]
        #self.current_matrix=np.random.rand(x.shape[1],y.shape[1])
        self.current_matrix=matrix
        self.lst=target.get_targets(np.array(y))
        self.x=x
        self.y=y
        self.learning_rate=learning_rate
        self.train_errors=[]
        self.test_errors=[]
        self.epochs=epochs
        self.epoch_weights=[]
        self.epoch_error=[]
        
        
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
        
        
    def propagation(self,x,y):
        self.p=np.array(x)*np.array(y)
        return self.binary_activation(self.p.sum())
        
    def update_weight_matrix(self,x_i,app):
        #print("app::: ",app)
        mean=np.array(app).sum()/len(app)
        test=[]
        
        for i in range(len(app)):
            test.append(0.5*(app[i]*app[i]))
        self.train_errors.append(np.array(test).sum()/len(test))

        matrix=self.current_matrix
        if(mean==0):
            return matrix
        else:
            for i in range(len(matrix[0])):
                res=np.multiply(x_i,(self.learning_rate*app[i]))
                matrix[:,i]=np.add(matrix[:,i],res)
            return matrix
            

    def learning(self,x_i,y_i):
        app=[]
        for i in range(len(self.current_matrix[0])):
            y_hat=self.propagation(x_i,self.current_matrix[:,i])
            app.append(y_i[:,i]-y_hat)
        self.current_matrix=self.update_weight_matrix(x_i,app)
        
        
        
    def training(self,x,y):
        for i in range(len(x)):
            self.learning(x[i,:],y[i,:])
            #print(self.current_matrix)
            #print(app)
        self.train_error=np.array(self.train_errors).sum()/len(self.train_errors)
            
    def testing(self,x,y):
        new_=[]
        for i in range(len(x)):
            app=[]
            for j in range(len(self.current_matrix[0])):
                y_hat=self.propagation(x[i,:],self.current_matrix[:,j])
                new_.append(y_hat)
                app.append(0.5*((y[i,j]-y_hat)*(y[i,j]-y_hat)))
            self.test_errors.append(app)
        return new_
    
    def loop(self,x,y):
        for i in range(self.epochs):
            self.training(x,y)
            self.epoch_weights.append(self.current_matrix)
            self.epoch_error.append(self.train_error)
            if(self.train_error==0):
                break
            
        
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
        return self.current_matrix
    def ret_epoch_weights(self):
        return self.epoch_weights
    def ret_train_error(self):
        return self.epoch_error
    def ret_test_error(self):
        return self.filter_targets(self.test_errors)
    def ret_predicted_vals(self,x,y):
        return self.filter_targets(self.testing(x,y))   



"""
x=np.matrix([[1,-1,-1,-1],[-1,1,-1,-1],[-1,-1,1,-1],[-1,-1,-1,1]])
y=np.matrix([[1,-1,-1],[1,-1,1],[-1,1,-1],[-1,1,1]])
"""
"""
dataset=pd.read_csv('weight.csv')
x=dataset.iloc[:,:-3].values
y=dataset.iloc[:,-3:].values
x=np.matrix(x)
y=np.matrix(y)

m=weight_matrix(x,y,1,10)
m.loop(x,y)


#print(m.create_weight_matrix(x,y))

"""
"""
print(m.ret_final_weight())
print(m.ret_epoch_weights())
print(m.ret_train_error())
print(m.ret_predicted_vals(x,y))
print(m.ret_test_error())
"""








































