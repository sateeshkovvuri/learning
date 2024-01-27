lst1 = ["sateesh","pranav","sai","krishna"]

for name in lst1 :  print(name)

print([name+"-cse" for name in lst1]) #concats -cse to each name in the lst1

lst2 =["Quic protocol","gui password","webassembly"]


#pairs corresponding index elements in each iteration,iterations: len(shortest list)

print(list(zip(lst1,lst2)))#output is same as we get in dictionary.items()
for name,seminar in zip(lst1,lst2):
    print(name + " : " + seminar)

print(list(enumerate(lst1))) #pairs each element in the list with its index

