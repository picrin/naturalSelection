from naturalSelection import *
import matplotlib.pyplot as plt
import numpy as np
import sys, csv

proportions = []
mrca = []
i = 0

with open(sys.argv[1], "r") as sims:
    g = loadGraph(sims)
    for genNo, _ in enumerate(g["generations"]):
        ap = alleleProportion(g, genNo)
        m = quickMRCA(g, i, 200)[1]
        i += 1
        proportions.append(ap)
        mrca.append(m)
        print(ap)

#plt.plot(proportions)
#plt.plot(mrca)
#plt.ylim([0,250])


fig, ax1 = plt.subplots()
t1 = np.arange(0, 260, 50)
ax1.plot(proportions,'b')
ax1.set_xlabel('generation')
# Make the y-axis label and tick labels match the line color.
ax1.set_ylabel('number of advantageous alleles')
ax1.set_yticks(t1)
for tl in ax1.get_yticklabels():
    tl.set_color('b')


ax2 = ax1.twinx()
t2 = np.arange(0, 50, 1)
print dir(ax2)
ax2.plot(mrca,'g',marker='o')
ax2.set_ylabel('T_MRCA')
ax2.set_yticks(t2)
for tl in ax2.get_yticklabels():
    tl.set_color('g')
plt.show()
