import RIGFramework as RIG
import time
import math
from matplotlib import pyplot as plt
#form of n, m, p, colour count, time (seconds)
output = open("log.txt", 'w')
output.write("n, m, p, colour count, time taken\n")
alpha = 0.6
for n in range(1000,1000000,1000):
    timeTaken = []
    for i in range(50):
        graph = RIG.RIG()
        m = int(n**0.6)
        p = 1/(math.log(n)*m)
        graph.fromNMP(n, m, p)
        start = time.time()
        graph.CliqueColour()
        end = time.time()
        timeTaken.append(end - start)
    agvTaken = sum(timeTaken)/len(timeTaken)
    timeTaken.sort()
    median = timeTaken[int(len(timeTaken)/2)]
    output.write(f"{n},{m},{p},{agvTaken},{median}\n")
output.close()
plotting = False
if plotting:
    plt.plot([i for i in range(100,10000,100)], timetaken)
    plt.show()

print("finished")
