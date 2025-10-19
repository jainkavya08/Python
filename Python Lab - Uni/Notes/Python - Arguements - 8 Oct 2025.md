**There are different types of arguements :**
- Positional Arguements 
- Default Arguements
- Unlimited-Positional Arguements
- Keyword Arguements 

### Positional Arguements 
---
```python
# Addition 

def add (a,b) :  
    c = a + b  
    return c  
c = add (90,78)  
print("Addition is : " , c)

# Subtraction
def add (c,d) :  
    e = a - b  
    return e 
e = add (90,78)  
print("Subtraction is : " , e)

# Multiplication 
def add (f,g) :  
    h = f * h  
    return h 
h = add (90,78)  
print("Multiplication is : " , h)
```

###  Default Arguements
---
```python 

def add ( a , b = 10) :  
    c = a + b  
    return c  
c = add (90)  
print("addition is: " , c)
```

### Unlimited - Positional Arguements 
---


### Keyword Arguements
---
```python

def my_function(child3, child2, child1) :  
    print ("The youngest child is " + child3)  
my_function(child1= " Ved " , child2= "Kavya" , child3= "Sanika")
```

#### Arbitrary Keyword Arguements
---
```python
def my_function (**kid) :  
    print("His last name is " + kid["lname"])  
  
my_function(fname = "ingole" , lname = "jain")
```

