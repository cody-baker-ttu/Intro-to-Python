def GCcontent(G, C):
        mycontent = (G + C) / 5000
        print(mycontent)
import random
bases = [ "A", "C", "T", "G"]
sequence= " "
for k in range (50):
        for i in range(100):
                base = random.choice(bases)
                sequence+=base
                G = sequence.count("G")
                C = sequence.count("C")
        print(sequence)
        GCcontent(G, C)
