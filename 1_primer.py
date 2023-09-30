import numpy as np
import openpnm as op 
# Lists: Python arrays 
# -----------
L  = [0,2,4,6,8]

L[0] = L[2]*L[4]
print(L)

T = (0,2,4,6,8)
#T[0] = 1 # tuples are immutable 
print(T)

L.append(100)
print(L)

L.extend([200,300])
print(L)

L.pop(2)
print(L)

print(L)
l = [L.pop(i) for i in [0,0,0]]
print(l,L)

try:
    print(L+2)
except TypeError:
    print("Adding to a list assumes we're trying to concatenate lists")
    print(L+[2])

print(L)
try: 
    print(L*2)
except:
    print("Failed")


# Numpy: Numerical arrays
# ----------
print(dir(np))

a = np.arange(0,100,20)
print(a)

print(a[2])

a[0] = 999
print(a)

a[[0,1,2]] = [1,2,3]
print(a)

mask = a>3
a[mask] = 0
print(a)

print(a+1)
print(a*2)

print(a)
print(np.sum(a))
print(a.sum())


# Dictionaries 
d = dict()
print(d)
d["arr"] = a
d["list"] = L
print(d)

print(d["arr"])

print(d.keys())
print(d.values())

d["test"] = 1.0
print(d)

del d["test"]
print(d)

d["test"] = 1.0
test = d.pop("test")
print(test)

# Subclassing dictionaries 
# Subclassing means, taking the basic functionality of the class and then adding to it 
# In openpnm we subclass dictionaries extensively 

class NewDict(dict):

    # overwrite the bass magic functions
    def __setitem__(self, key,value): 
        # This is our custimisation 
        print("The key being written is:", key)
        print("The value being written is:", value)

        # Now call setitem on the base dict class to actually set the item 
        super().__setitem__(key,value)

    def __getitem__(self, key,value):
        print("The key being retrived is:",key)
        return super().__getitem__(key)

d = NewDict()
print(d)

d["test"] = 1
print(d)
#a = d["test"]

