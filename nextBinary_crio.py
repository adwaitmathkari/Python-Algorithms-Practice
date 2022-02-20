def next_greater(num):
    b = bin(num).replace("0b", "")  
    b=list(b)
    # print(b)
    for i in range(len(b)-1, 0,-1):
        # print(i)
        if b[i]=='1' and b[i-1] =='0':
            # print('in')
            b[i]='0'
            b[i-1]='1'
            b = b[0:i+1] + sorted(b[i+1:])
            return int(''.join(b), 2)
    return int('10'+ ''.join(sorted(b[1:])), 2)


def next_smaller(num):
    b = bin(num).replace("0b", "")
    b=list(b)
    for i in range(len(b)-1, 0,-1):
        if b[i]=='0' and b[i-1] =='1':
            # print('in')
            b[i]='1'
            b[i-1]='0'
            b= b[0:i+1] + sorted(b[i+1:], reverse=True)
            return int(''.join(b), 2)
    return -1

for i in [9,10,12,14,22,81,102,12345,123456]:
    print(bin(i))
    print(bin(next_greater(i)))
    print(bin(next_smaller(i)))
    print('------------------')