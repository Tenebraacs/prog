#valtozok hatokore
#local scope: A variable created inside a function is available inside that function
def myfunc():
    x = 300
    print(x)

myfunc()

def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc

myfunc()

#global scope: Global variables are available from within any scope, global any local.
#1.) lehetoseg: fv-en kivul deklaralok
x = 300

def myfunc():
    print(x)

myfunc()
print(x)

#2.) fv-en belul a "global" kulcsszoval deklaralok
def myfunc():
    global x
    x = 300

myfunc()
print(x)