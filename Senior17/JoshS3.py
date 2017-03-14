import itertools
import time

startT = time.time()

# Test cases
#a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]
#a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
#a = [1, 2, 2, 3]
#a = [1, 10, 100, 1000, 2000]
a = [1, 2, 3, 4]

#gets every pair of numbers
b = itertools.combinations (a, 2)
# list of the sums
sums = []
for c in b:
    print(c)
    sums.append(sum(c))


counter = 0
lenght = 0

for hight in sums:
    # Most common hieght
    if sums.count(hight) > lenght:
        lenght = sums.count(hight)
        counter = 1
        hight_H = hight

    #Repeated lenghts
    elif sums.count(hight) == lenght and hight != hight_H:
        counter += 1    
    

print (str(lenght) + " " + str(counter))
print (time.time() - startT)

