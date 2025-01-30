def div(a,b):
    return a/b
print(div(b=2,a=0))

def id(uid):
    print(uid)
id('123')
id('1')

def id(name, uid1="23"):
    print(name,uid1)
id(name='Ram')
id(name='Rithika',uid1='45')


def myfunc(*args):
    for x in args:
        print(x)
myfunc(1,2,3,4,5)


def myfunc2(**kwargs):
    for x,y in kwargs.items():
        print(x,y)
myfunc2(name=('Ram','Rithika'),uid=('12','34'),city=('Chennai','Tirunelveli'))

