# 1번
def grade(score):
    if (score >= 90) and (score <= 100):
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# 2번
def quadrant(x, y):
    if x > 0:
        if y > 0:
            return "제 1사분면"
        else:
            return "제 4사분면"
    elif y > 0:
        return "제 2사분면"
    else:
        return "제 3사분면"
    

# 3번
def leapYear(year):
    if year%4 == 0:
        if year%100 != 0:
            return "윤년입니다."
        elif year%400 == 0:
            return "윤년입니다."
        else:
            return "윤년이 아닙니다."
    else:
        return "윤년이 아닙니다."


# 4번
def dice(a, b, c):
    if (a==b) and (b==c):
        return 10000 + a * 1000
    elif (a == b) or (b == c) or (a == c):
        if a == b:
            return 1000 + a * 100
        elif b == c:
            return 1000 + b * 100
        else:
            return 1000 + a * 100
    else:
        return max(a,b,c) * 100
        

# 5번
def alarm(time):
    time = str(time)
    if len(time) == 2:
        minute = int(time)
        hour = 0
    elif len(time) == 3:
        minute = int(time[-2:])
        hour = int(time[0:1])
    else:
        minute = int(time[-2:])
        hour = int(time[0:2])
    
    minute = minute - 45
    
    if minute < 0:
        hour = hour - 1
        minute = minute + 60
    
    if hour < 0:
        hour = hour + 24
    
    output = f"{hour}시 {minute}분"
    return output

print(alarm(900))
print(alarm(30))
print(alarm(2315))
print(alarm(1050))


# time = str(900)
# if len(time) == 2:
#     minute = int(time)
#     hour = 0
# elif len(time) == 3:
#     minute = int(time[-2:])
#     hour = int(time[0:1])
# else:
#     minute = int(time[-2:])
#     hour = int(time[0:2])
        
# print(minute)
# print(hour)
