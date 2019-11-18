import numpy as np
a1 = np.arange(1,101,1)
a2 = np.reshape(a1,(10,10))
A = a1**2
print (A)
div=A%3
Afinal = A[div==0]
print ('Elements divisible by 3:',Afinal)
np.save('div_by_3.npy',Afinal)