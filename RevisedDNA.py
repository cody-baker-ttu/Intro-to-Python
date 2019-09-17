
import random
bases = [ "A", "C", "T", "G"]
sequence = random.choices(bases, k=100)
Gcount = sequence.count("G")
print("The number G's is: ", Gcount)
Ccount = sequence.count("C")
print "The number of C's is: " , Ccount)
Acount = sequence.count("A")
C_int = str2num(Ccount)
A_int = str2num(Acount)
AandC_int = C_int + A_int
AandC = num2str(AandC_int)
print("The number of A's and C's combined in this sequence is: ", AandC)
