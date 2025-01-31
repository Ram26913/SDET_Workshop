import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([34,56,78])
print(x.shape)
print(np.concatenate([x,y]))
slice = x[1:3:2]

arr = np.array([[1,2],[3,4],[5,7],[8,9],[11,14],[15,17],[18,19],[12,13]])
newarr = np.array_split(arr,3)
print(newarr)