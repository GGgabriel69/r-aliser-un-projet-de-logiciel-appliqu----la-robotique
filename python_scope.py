import time

my_global = "global"
#GitHub test 1
#GitHub test 


def my_function(argument):
    my_local = "local"
    

    variables =[my_global, argument, my_local]
    for var in variables:
        print(var)
        time.sleep(10000000000000000000000000)

my_function("argument")

