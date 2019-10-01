##First, I need to initialize the sequence of DNA that I will be splitting, including an "*" symbol$
#restriction site = G*AATTC
#the comment above indicates to me where my restriction site is for my restriction enzyme
seq= "ACTGATCGATTACGTATAGTAG*AATTCTATCATACATATATATCGATGCGTTCAT"
#Now, I need a command which will split the sequence into two fragments at the asterisk.
seq1,seq2=seq.split("*")
#Now, I will print my two fragments to ensure my "enzyme" cut in the proper place.
print(seq1)
print(seq2)
#Now, I will calculate the lengths of each fragment.
length1=len(seq1)
length2=len(seq2)
#Finally, I will print the length of each fragment.
print("The length of fragment 1 is: ", length1)
print("The length of fragment 2 is: ", length2)
