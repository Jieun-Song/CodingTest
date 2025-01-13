got = input()
list = got.split(".")
# print(list)
result = ""
for i in list:
    if i != "":
        n = len(i)
        iter = n // 4
        left = n % 4
        if left % 2 != 0:
            result = "-1 "
            break
        result = result + "AAAA"*iter+"BB"*(left//2)+ "."
    else:
        result = result + "."

print(result[:-1])