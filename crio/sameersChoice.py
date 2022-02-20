
import re
from collections import defaultdict


class Solution:

    def lucky_number(self, pattern_list, queries):
        
        # list2, qlist2 = [], []
        # for i in range(len(pattern_list)):
        #     list2.append(pattern_list[i][0]+' '+pattern_list[i][1])
        # for i in range(len(queries)):
        #     qlist2.append(queries[i][0]+' ' +queries[i][1])
            
        # pattern_list = list2
        # queries = qlist2

        dict_pat = {}
        #creating patterns to match in step 2
        for pat in pattern_list:
            # pat = pat.split(' ')
            s = []
            i=0
            # print(pat)
            while i < len(pat[1])-1:
                if pat[1][i+1] == '-':
                    s += ['['+pat[1][i:i+3]+']']
                    i += 3
                else:
                    s += [pat[1][i]]
                    i+=1
            if i<len(pat[1]):
                s+=[pat[1][i]]

            dict_pat[pat[0]] = s


        states = ["AP", "AR",	"AS", "BR",	"CG", "GA", "GJ",	"HR",	"HP", "JH", "KA",	"KL",	"MP",	"MH",	"MN",	"ML",	"MZ",
                    "NL", "OD", "PB",	"RJ", "SK",	"TN",	"TS", "TR",	"UP",	"UK",	"WB",	"AN",	"CH",	"DD", "DL", "JK",	"LA", "LD", "PY"]
        
        print1 = []
        print2 = []
        for q in queries:
            #step 1 -- Yes or No
            #states,
            valid = True

            # q = q.split(' ')
            no = q[0].split('-')
            # print(no)
            if len(no)<3:
                print1.append('No')
                continue

            if no[0] not in states:
                valid = False                
            if not re.match(r'\b[0-9]{2}\b', no[1]):
                valid = False
            if len(no)==3:
                lastNum = no[2] 
                if not re.match(r'\b[0-9]{4}\b', no[2]):
                    valid = False
            else:
                lastNum = no[3]
                if not re.match(r'\b[A-Z]{1,3}\b', no[2]):
                    valid = False
                if not re.match(r'\b[0-9]{4}\b', no[3]):
                    valid = False
            
            if not valid:
                print1.append('No')
                continue
            
            #valid
            else:
                # print('***', q[1], dict_pat.keys())
                if q[1] not in dict_pat.keys():
                    print1.append('Yes Good')
                    if self.ispal(lastNum):
                        print2.append(' '.join(q))
                else:
                    vehiclePatternList = dict_pat[q[1]]
                    if re.match(''.join(vehiclePatternList), lastNum):
                        print1.append('Yes Good')
                        if self.ispal(lastNum):
                            print2.append(' '.join(q))

                    else:
                        newLastNum = ''
                        # print(vehiclePatternList)
                        for i in range(4):
                            if not re.match(vehiclePatternList[i], lastNum[i]):
                                ind1 = 0 if len(vehiclePatternList[i]) == 1 else 1
                                newLastNum += vehiclePatternList[i][ind1]
                            else:
                                newLastNum+=lastNum[i]
                        print1.append('Yes Bad '+newLastNum)

        f=open('crio/sameersChoice_test/t3_me.txt', 'w')
        for p in print1:
            f.writelines(p+'\n')
            # print(p)
        

        # print(len(print2))
        f.write((str(len(print2)))+'\n')

        for p in print2:
            f.writelines(p+'\n')
            # print(p)

        f.close()

    def ispal(self, num):
        assert len(num) == 4
        return num[0]==num[3] and num[1] == num[2]



# s=Solution()
# f=open('crio/states.txt')
# pats, queries = [], []
# for i in range(int(f.readline().strip())):
#     pats.append(f.readline().strip())
# for i in range(int(f.readline().strip())):
#     queries.append(f.readline().strip())
# print(pats,queries)
# s.lucky_number(pats, queries)


f=open('crio/sameersChoice_test/t3.txt')
t = int(f.readline().strip())
pattern_list = list()
for _ in range(t):
    vehicle_type, pattern = f.readline().strip().split(" ")
    pattern_list.append([vehicle_type, pattern])

n = int(f.readline().strip())
queries = list()
for _ in range(n):
    plate_string, vehicle_type = f.readline().strip().split(' ')
    queries.append([plate_string, vehicle_type])
# print(queries, pattern_list)
Solution().lucky_number(pattern_list, queries)


