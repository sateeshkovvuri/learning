test = {
    "name":"sateesh",
    "branch":"cse",
    "college":"jntuhcej",
    "branch":"computer science and engineering"
}
#second branch occurance will replace first occurance

items = test.items()
for key,value in items:
    print(key+" : "+value)

#print(test["semester"]) : throws error
#instead use:
print(test.get("semester",0)) #gives value if present else returns 0 , if 0 is not mentioned returns None