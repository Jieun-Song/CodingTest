'''
역정보가 주어졌을때, 역명과 부역명 출력

입력
{station_name}
{station_name} {open_character}{sub_station_name}{close_character}

출력
첫 번째 줄에 역명을, 두 번째 줄에 부역명을 출력해 주세요.
만약, 부역명이 없다면, 부역명을 출력할 때 '-'를 출력해 주세요.
'''
input = input()
if input.__contains__(" ("):
    sn, ssn = input.split(" (")
    print(sn+"\n"+ssn[:-1])
else :
    sn = input
    print(sn+"\n-")