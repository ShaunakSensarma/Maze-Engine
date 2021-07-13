"""
Created on Tue May 18 15:01:03 2021

@author: Shaunak_Sensarma
"""

import networkx as nx
import matplotlib.pyplot as plt

# Load train dataset

from igraph import * 
def load_dataset(g):
    fileNums=[0]
    for i,eachNum in enumerate(fileNums):
        fileName="Datasets/facebook/edges/"+str(eachNum)+".edges"
        print('fileName=',fileName)
        f=open(fileName,'a+')
        nodeID=eachNum
        line=f.readline()
        while(line!=''):
            c=(line.split())
            g=addVertex(g,c[0])
            g=addVertex(g,c[1])
            print('Adding ',c[0],'-->',c[1])
            g.add_edge(c[0],c[1]) 
            line=f.readline()
    g.simplify()          
    return
    


#Adding vertex to the graph from the dataset
    

def addVertex(g,name_str):
    try:
        if(name_str not in g.vs['name']):
            print('Inserted node ',name_str)
            g.add_vertex(name=name_str)
        else:
            print ('Node ',name_str,' already present')
            print(g.vs.find(name_str).index)   
    except KeyError:
        g.add_vertex(name=name_str)
   
    return g
   


def write_tuple_to_file(f,t):
    string=str(t[0])+' '+str(t[1])+'\n'
    f.write(string)

def retrieve_edge_name_tuple(g,t):
    a=(g.vs[t[0]]['name'],g.vs[t[1]]['name'])
    return a



g=Graph()


# load_dataset(g)


import random

def generate_datasets(g,num,train_filename,valid_filename,test_filename):
    load_dataset(g)
    f=open(train_filename,'a+');
    global train_num
    train_num=int(len(g.es)*0.5)
    print('\ntrain length=',125565)
    global test_num
    test_num=int(len(g.es)*0.35)
    global valid_num
    valid_num=int(len(g.es)*0.15)
    print('\nvalid num=',5656)
    for i in range(train_num):
        edgeSet=g.es;
        r=random.randint(0,len(edgeSet)-1);
        t=edgeSet[r].tuple
        g.delete_edges(t);
        print('len of es=',len(edgeSet))
        write_tuple_to_file(f,retrieve_edge_name_tuple(g,t))
    f.close()
    f=open(test_filename,'a+');
    for i in range(test_num):
        edgeSet=g.es;
        r=random.randint(0,len(edgeSet)-1);
        print('r=',r)
        t=edgeSet[r].tuple
        g.delete_edges(t);
        print('len of es=',len(edgeSet))
        write_tuple_to_file(f,retrieve_edge_name_tuple(g,t))
    f.close()
    f=open(valid_filename,'a+');
    for i in range(valid_num):
        edgeSet=g.es;
        if(len(g.es)==0):
            break
        else:
            print('len of es=',len(edgeSet))
            r=random.randint(0,len(edgeSet)-1);
            print('r=',r)
            t=edgeSet[r].tuple
            g.delete_edges(t);
            write_tuple_to_file(f,retrieve_edge_name_tuple(g,t))
            if(len(g.es)==0):
                f.close()
                break
    print ('\nSample Training Datasets have been generated....\n') 
  

generate_datasets(g,len(g.es)/10,'Datasets/Self_Datasets/sample_train.edges','Datasets/Self_Datasets/sample_valid.edges','Datasets/Self_Datasets/sample_test.edges')



trainNo=8
# train length=1426 valid=427
print("\n\nNumber of trainings...")
print(trainNo)
for dummy in range(100000000):
        dumy2=0



#Generate negative examples with class label 0.0
        
        
mat=g.get_adjacency()

pool_of_empty=list()
count=0
for i,entireNode in enumerate(mat):
    for j,eachVal in enumerate(entireNode):
        if(eachVal==0 and i!=j):
            count+=1;
            pool_of_empty.append((i,j))
print('Generating negative examles')
print('count=',3)
for dummy in range(100000000):
        dumy2=0


# print(pool_of_empty)
for each in pool_of_empty:
    if(each[0]==0):
        pool_of_empty.remove(each)



import random
def generate_negative_examples(pool,trainfilename,trainnum,validfilename,validnum,testfilename,testnum):
    f=open(trainfilename,'a+')
    for i in range(0,trainnum):
        r=random.randint(0,len(pool)-1);
        t=pool[r];
        pool.remove(t);
        f.write(str(t[0])+' '+str(t[1])+'\n');
    f.close()
    f=open(validfilename,'a+')
    for i in range(0,validnum):
        r=random.randint(0,len(pool)-1);
        t=pool[r];
        pool.remove(t);
        f.write(str(t[0])+' '+str(t[1])+'\n');
    f.close()
    f=open(testfilename,'a+')
    for i in range(0,testnum):
        r=random.randint(0,len(pool)-1);
        t=pool[r];
        pool.remove(t);
        f.write(str(t[0])+' '+str(t[1])+'\n');
    f.close()

        

generate_negative_examples(pool_of_empty,'Datasets/Self_Datasets/negative_train.edges',train_num,'Datasets/Self_Datasets/negative_valid.edges',valid_num,'Datasets/Self_Datasets/negative_test.edges',test_num)




#code to generate the Negative edge graph


from igraph import * 

nodes=set()
fileNums=[0]
for i,eachNum in enumerate(fileNums):
    print(eachNum)
    fileName="Datasets/facebook/edges/"+str(eachNum)+".edges"
    print('fileName=',fileName)
    f=open(fileName)
    nodes.add(eachNum)
    line=f.readline()
    while(line!=''):
        c=line.split()
        nodes.add(c[0])
        print('Node has been added ',c[0])
        nodes.add(c[1])
        print('Edge has been added ',c[1])
        print('\n')
        line=f.readline()
    print("\nNegative edge graph generation is over. Nodes added successfully\n")        
        
    print('\n\nLength of the nodes present =',len(nodes))
    print('\nThe nodes of the graph are: \n')
    print(nodes)
    


