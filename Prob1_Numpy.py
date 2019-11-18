import numpy as np
X = np.random.random((5,5))
print ('Original Matrix: ',X)
sd = X.std()
m = X.mean()
Z = (X-m)/sd
print ('Normalized Matrix:',Z)
np.save('X_normalized.npy',Z)