import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
subj = np.array(["English","Maths","Science","Sst","Hindi"])  
Marks1 = np.array([87,99,67,89,45])

#def pie_chart(df):

plt.pie(Marks1)
plt.pie(Marks1,startangle=90,shadow='true')
plt.legend(subj)
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#def scatter_plot(df):

subj = np.array(["English","Maths","Sst","Science","Sanskrit","Hindi"])  
Marks1 = np.array([87,77,44,99,56,85])
plt.plot(subj,Marks1,color='r',marker='o',mec='k',ms=10)
plt.show()