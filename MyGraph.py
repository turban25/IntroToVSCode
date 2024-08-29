import matplotlib.pyplot as plt
import numpy as np

x = np.linspac(0, 20, 100)
plt.plot(x, np.sin(x))

plt.show()




#step 1 Create your Vitrual Environment 
    #PC  py -3 -m vev ______
    #mac python3 -m venv _____

#step 2 Activate your VE
    #PC  myvenv/scripts/activate
    #mac source myvenv/bin/activate

#Step 3 Install 3rd party libraries
    # pip3 install _______