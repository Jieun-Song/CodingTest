# 올해가 몇프로남았는지 출력

# 절대/상대 오차는 1분의 10의 9제곱승까지 허용한다.

#우선 1분이 1년의 몇 %를 차지하는지 생각해야할것같다.
# print(round((100/365/24/60),15))
# 0.000190258751903

#입력된 날짜를 1년 기준으로해서 시간단위로 잘라 저 위의 값을 곱한후
# 소수점 9자리에서 자르면 될거같은디
import datetime

def monthToNum(key):
  monthNum = {"January":1, "February":2, "March":3, "April":4, "May": 5,
            "June":6, "July":7, "August":8, "September":9, "October":10,
            "November" : 11, "December" : 12}.get(key)
  return monthNum;

# 차라리 달 -> 일/ 일 -> 분으로 바꾸는 함수를 각각 만드는건 어떨까?

def monthToDay(dates, month):
  result = 0
  for i in range(month-1):
    result += dates[i]
  return result

def dayToMin(date):
  return date * 24 * 60

def hoursToMin(hours):
  hour, min = map(int, hours.split(":"))
  return (hour * 60 + min)

front, back = input().split(", ")
month, day = front.split()
year, hour = back.split()
month = monthToNum(month)

dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
oneYear = 365

if int(year) % 4 == 0 :
  # 윤년
  dates[1] = 29
  oneYear = 366

# 달 -> 일
days = monthToDay(dates, month) + int(day)
mins = dayToMin(days) + hoursToMin(hour)

print(mins*100/dayToMin(oneYear))




#해야하는것
# 00:00으로 되어있는 형태를 분으로 바꾸어야한다,,,,,,,,
# 앞에 것들을 분으로 바꾸는 건 됨
