##First, I will need to initialize a variable which contains the DNA sequence provided to us in the$
seq="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
#Now, I will need to count the number of A's and the number of T's
A_count=seq.count("A")
T_count=seq.count("T")
#Now, I will print the count of A's and T's
print("The number of A's is: ", A_count)
print("The number of T's is: ", T_count)
#Now, I need to add the number of A's and T's so that I can print the sum of the A's and the T's
total = A_count + T_count
#Now, I need to print the total of A's and T's together
print("The total number of A's and T's is: ", total)
#Now, I need to count the occurences of A and T adjacent to each other and print
A_and_T=seq.count("AT")
print("The number of A's followed by a T is: ", A_and_T)
#Now, I need to count T followed by A
T_and_A=seq.count("TA")
print("The number of T's followed by an A is: ", T_and_A)
