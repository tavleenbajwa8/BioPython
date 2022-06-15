#!/usr/bin/env python
# coding: utf-8

# Get total number of reads from the user. A read is basically(a string) short sequence of nucleotide for example, 'ATTGCCTTC'. then ask user to
# give bases for each read, If user entered 10 a total get 10 sequence separtely. Show user which is the longest read and show total number of
# 'A','T','G','C' across all reads

# In[ ]:


reads = map(int,list(map(str,input("Enter reads: ").upper().split())))
longest_read = 0
longest_seq = ""
longest_ind = 0
acount = 0
gcount = 0
ccount = 0
tcount = 0
for ind,i in enumerate(reads):
    for j in i:
        if j == "A":
            acount+=1
        elif j == "G":
            gcount+=1
        elif j == "T":
            tcount+=1
        elif j == "C":
            ccount+=1
        else:
            pass
    print(i,len(i),len(i) > longest_read)
    if len(i) > longest_read:
        longest_read = len(i)
        longest_seq = i
        longest_ind = ind
print("The longest sequence is: ", reads[longest_ind])
# for read in reads:
#     if longest_read == len(read):
#         print("Longest read(s) is: ",read)

print("Total no. of A:", acount, ", G:",gcount, ", C:",ccount, ",T:", tcount)

