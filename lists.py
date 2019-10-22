
import random
bases = [ "A", "C", "U", "G"]
sequence = random.choices(bases, k=1000)
print(sequence)
string1=''.join(sequence)
print(string1)
list1 = string1.split("AUG")
print(list1)
newlist=[]
for element in list1:
        if len(element) > 50:
                newlist.append(element)
print(newlist)
for gene in newlist:
        print len(gene)

