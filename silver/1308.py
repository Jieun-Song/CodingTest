# 오늘부터 캠프가 끝날 떄까지 며칠이나 남았는지 알아본다.
# 윤년 포함할수도(4로 떨어지는 햇수.100은 평년, 400은 윤년) -> 366
#(2월 29일 / 윤년은 30일)
# 너무 길어지면 무단으로 빠질수도
# 오늘부터 D-Day까지 x일이 남았다면, "D-"를 출력하고 그 뒤에 공백 없이 x를 출력한다.
# 만약 캠프가 천년 이상 지속된다면 (오늘이 y년 m월 d일이고, D-Day가 y+1000년 m월 d일과
# 같거나 늦다면) 대신 "gg"를 출력한다. 오늘이 2월 29일인 경우는 주어지지 않는다.
import datetime

def inputToDate(list0):
  list2 = []
  for i in list0:
    list2.append(int(i))
  year,month,date = list2

  day = datetime.date(year,month,date)
  return day

listToday = input().split(" ")
dayToday = inputToDate(listToday);
listEnd = input().split(" ")
dayEnd = inputToDate(listEnd);

btwDate = (dayEnd-dayToday).days

# 1000년 뒤 날짜 계산 (천년 뒤 같은 월, 일)
thousandYearsLater = datetime.date(dayToday.year + 1000, dayToday.month, dayToday.day)


if dayEnd < thousandYearsLater:
  print("D-{a}".format(a = btwDate))
else : 
  print("gg")


# 4년기준으로 먼저 나누기
# 그리고 365일보다 더 남았으면 정확한 년수를 구하고,
# 안남았으면 거기서 멈춰서 1000이 넘는지 확인
# 넘으면 gg 출력
# 안넘으면 날 출력


