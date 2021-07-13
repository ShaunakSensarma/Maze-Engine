"""
Created on Tue May 18 15:01:03 2021

@author: Shaunak_Sensarma
"""


# Add code to visualize the centrality of the graph. Basically this section is to get an idea about the structure of the graph


# In[2]:

from igraph import * 
g=Graph()


# In[3]:


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
    for dummy in range(10000):
        dum2=0
        
    return g
   


def write_tuple_to_file(f,t):
    string=str(t[0])+' '+str(t[1])+'\n'
    f.write(string)

def retrieve_edge_name_tuple(g,t):
    a=(g.vs[t[0]]['name'],g.vs[t[1]]['name'])
    return a


# In[4]:


def load_dataset(fileName,g):
    fileNums=[0]
    for i,eachNum in enumerate(fileNums):
        print(eachNum)
        fileName="Datasets/facebook/edges/"+str(eachNum)+".edges"
        print('fileName=',fileName)
        f=open(fileName)
        line=f.readline()
        while(line!=''):
            c=(line.split())
            g=addVertex(g,c[0])
            g=addVertex(g,c[1])
            print('\nAdding Nodes',c[0],'-->',c[1])
            g.add_edge(c[0],c[1]) 
            line=f.readline()
    g.simplify()    
    return


# In[5]:

load_dataset('abd',g)
#print(len(g.vs))


# In[7]:

print("\n\nNumber of nodes added here = ")
print(len(g.vs))


# In[20]:

def calculate_eigen(g):
    print("\n\Displaying maximum eigen value nodes...")
    eigen=g.evcent(directed=False)
    for i in range(1,6):
        maxVal=max(eigen)
        print(i,'==node',g.vs[eigen.index(maxVal)]['name'],' with score of ',maxVal)
        eigen.remove(maxVal)
    eigen=g.evcent(directed=False)
    return eigen


# In[21]:

def calculate_closeness(g):
    print("\n\Displaying maximum closeness centrality value nodes...")
    close=g.closeness(g.vs)
    for i in range(1,6):
        maxVal=max(close)
        print(i,'==node',g.vs[close.index(maxVal)]['name'],' with score of ',maxVal)
        close.remove(maxVal)
    close=g.closeness(g.vs)
    return close


# In[22]:

def calculate_between(g):
    print("\n\Displaying maximum betweeness centrality value nodes...")
    between=g.betweenness(g.vs)
    for i in range(1,6):
        maxVal=max(between)
        print(i,'==node',g.vs[between.index(maxVal)]['name'],' with score of ',maxVal)
        between.remove(maxVal)
    between=g.betweenness(g.vs)
    return between


# In[23]:

print('\nEigen Vector')
global eigen
eigen=calculate_eigen(g)

global close
global between
print('\nCloseness Measure vector')
close=calculate_closeness(g)
print('\nBetweenness Measure vector')
between=calculate_between(g)


# In[24]:

print("\nCentrality value of individual nodes....\n")
for ele in range(len(close)):
    print("Node-",ele," - ",close[ele])

