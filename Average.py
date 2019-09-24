  GNU nano 2.3.1                    File: Average.py

import statistics
sum = 0
n = 20
for i in range(1, n + 1):
    sum += i
average = sum / 20
print(average)
list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
average2 = statistics.mean(list)
print(average2)
