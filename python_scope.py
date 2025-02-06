import time

my_global = "global"
#GitHub test 1
#GitHub test 
# #kjvbsdh

def my_function(argument):
    my_local = "local"
    

    variables =[my_global, argument, my_local]
    for var in variables:
        print(var)
        time.sleep(1)

my_function("argument")

