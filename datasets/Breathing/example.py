import pickle
from matplotlib import pyplot as plt

# Load data
data = pickle.load(open("breathing.pickle",'rb'))

# Visualise
plt.figure(figsize=(10,8))
plt.subplot(2,2,1)
plt.plot(data[('breath', 1)][20][0])
plt.title('Breathing - 1m')

plt.subplot(2,2,2)
plt.plot(data[('breath', 2)][20][0])
plt.title('Breathing - 2m')

plt.subplot(2,2,3)
plt.plot(data[('static', 1)][20][0])
plt.title('Static Scene')

plt.subplot(2,2,4)
plt.plot(data[('random', 2)][20][0])
plt.title('Random Activity')
plt.show()

