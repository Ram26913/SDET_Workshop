myset={1,2,3,4,5,6,6,7,7,8}
myset1={1,2,4,5,6,7}
myset.discard(11)
myset.remove(4)
myset.add(14)
print(myset)
print(myset.union(myset1))
print(myset.intersection(myset1))

for x in myset:
    print(x)