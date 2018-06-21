import os
os.environ['QT_QPA_PLATFORM']='offscreen'

import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
plt.ion()

from IPython import get_ipython
get_ipython().magic("load_ext autoreload")
get_ipython().magic("%autoreload 2")
