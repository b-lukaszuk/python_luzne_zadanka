#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from typing import List


# Chapter 3. Describing Data


# table 3.1
age: List[float] = [7,7,8,8,8,9,11,12,12,13,13,14,14,15,16,17,17, 17,17,19,19,20,23,23,23]
pi_max: List[float] = [80, 85,110,95,95,100,45,95,130,75,80,70,80, 100,120,110,125,75,100,40,75,110,150,75,95]
tab31: pd.DataFrame = pd.DataFrame({"age": age, "pi_max": pi_max})

# fig 3.15
sns.scatterplot(data=tab31, x="age", y="pi_max", s=200, color="lightblue", legend=False)
plt.xlim((5, 25))
plt.title("Fig. 3.15. Scatter diagram of PImax by age")
plt.xlabel("Age [years]")
plt.ylabel("PImax [cm $H_20$]")
plt.show()


# table 3.2
igm: np.ndarray  = np.concatenate((np.arange(0.1, 1.9, 0.1), np.asarray([2.0, 2.1, 2.2, 2.5, 2.7, 4.5])))
num_of_children: np.ndarray = np.asarray([3,7,19,27,32,35,38,38,22,16,16,6,7,9,6,2,3,3,3,2,1,1,1,1])
tab32 = pd.DataFrame({"igm": igm, "num_of_children": num_of_children})

# figure 3.3
sns.histplot(data=tab32, x="igm", bins=np.arange(0.1, 4.6, 0.1), weights="num_of_children")
plt.title("Fig. 3.7. (a) Concentration of IgM in\n298 children aged 6 months to 6 years")
plt.xlabel("IgM [g/l]")
plt.ylabel("Number of children")
plt.show()
