func = lambda a:a+2
print(func(6))

numbers = [1,2,3,4,5]
funcsq = lambda nums: [x**2 for x in nums]

print(funcsq(numbers ))

functuptolst = lambda tup : [x for x in tup]
print(functuptolst((1,2,3,4)))#converts a tuple to list

funcnamemod = lambda lst,branch : [f"{name}-{branch}" for name in lst]
print(funcnamemod(["sateesh","sai","pranav","abhi","krishna","pavan","kalyan"],"cse"))#modifies a list of names {demonstration that lambdas can accept more than one parameters}
print(funcnamemod(["rakesh","surya"],"eee"))