import requests
import datetime as dt

headers = {
        'Content-Type': 'application/json',
        'Authorization' : 'Token 0207139c29a658d57cd1cd4c1df85d2476bf8aaf'
        }
startDate='2020-05-01'
endDate = '2020-05-10'
endDate = dt.datetime.strptime(endDate, '%Y-%m-%d').date()
print(dt.datetime.now() + dt.timedelta(days=-1))
print(dt.date.today())
count = 0
while True:
        count+=1
        print(count, endDate)
        url = f"https://api.tiingo.com/tiingo/daily/GOOGL/prices?startDate={endDate}&endDate={endDate}"

        requestResponse = requests.get( url, headers=headers)
   
        l = requestResponse.json()
        if len(l):
                break

        endDate = endDate + dt.timedelta(days=-1)
print(len(l))
print(endDate)
print(l)
# for i in range(5):
#         print(l[i])
# for key in l:
        # print(key)
        # print()




# print((requests.get("https://api.tiingo.com/tiingo/daily/GOOGL/prices", headers=headers)).json())
