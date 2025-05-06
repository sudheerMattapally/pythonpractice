global x
x='Mattapally'
def myfun():
    global x
    x='sudheer'
    print(x)
myfun()
print(x) 