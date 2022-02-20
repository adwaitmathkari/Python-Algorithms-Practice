
def f1(par1):
    par1 += [30]
    print("inside the function", par1)


val1=[10,20]
# f1(val1)
# print("outside the function", val1)


def f2(p):
    p+="def"
    print("inside", p)
v="abc"
f2(v)
print("outside",v)