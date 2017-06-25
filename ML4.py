'''

Program = ML4.py

Author = Archana Raghu

Purpose = concepts using histogram to visualize a feature

'''

import numpy as np
import matplotlib.pyplot as plt

greyhounds = 500
lab = 500

grey_height = 28 + 4 * np.random.randn(greyhounds)
lab_height = 24 + 4 * np.random.randn(lab)

plt.hist([grey_height, lab_height], stacked=True, color=['r','b'])
plt.show()
