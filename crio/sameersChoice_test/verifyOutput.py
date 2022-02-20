f1=open("crio/sameersChoice_test/t2_o.txt")
f2 = open("crio/sameersChoice_test/t2_me.txt")

assert f1.read() == f2.read()
print('verified')
