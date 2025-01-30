mydict = {
    'name':'Ram',
    'exp':'10',
    'city':'Tirunelveli'
}
mydict['pincode']= 627002
print(mydict.items())
print(mydict.keys())
print(mydict.values())
print(mydict['name'])

for x in enumerate(mydict):
    print(x)