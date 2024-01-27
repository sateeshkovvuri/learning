def wrap_generator(func):
    def wrap(*args):
        print("performing addition")
        print("inserting + operator between the operands")
        func(*args)
        print("operations completed")
    return wrap

@wrap_generator
def addition(*args):
    result = 0
    for x in args:
        result+=x
    print(result)

#addition = wrap_generator(addition)

addition(1,2,3,-4,10)
