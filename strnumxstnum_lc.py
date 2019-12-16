class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1=['0','1','2','3','4','5','6','7','8','9']
        num1N=0
        num2N=0
        for ch in num1:
            num1N = num1N*10 + l1.index(ch)
        for ch in num2:
            num2N = num2N*10 + l1.index(ch)
        prod=num1N*num2N
        print('asdf',prod)

        prodS=''
        if prod==0:
            return '0'
        while prod!=0:
            prodS=l1[int(prod%10)]+prodS
            print(prod, l1[int(prod%10)],prodS)
            prod = prod - prod%10
            print(prod)
            print(prod*0.1)
            prod = prod/10      
            print(prod)

        return prodS

s=Solution()
print(s.multiply("6913259244","71103343"))


