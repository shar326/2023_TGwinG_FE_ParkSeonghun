# 1번
def sum(a, b):
    summation = a+b
    return summation

# 2번
def sub(a, b):
    substraction = a-b
    return substraction

# 3번
def mul(a, b):
    multiply = a*b
    return multiply

# 4번
def div(a, b):
    division = a/b
    return division

# 5번
def distance(x1, y1, x2, y2):
    d = pow((x1-x2)**2+(y1-y2)**2,0.5)
    return d

# 6번
def title():
    lylics = "Switch sides and I'm beside you."
    Main_Title = lylics[-11:-1]
    return Main_Title

# 7번
def reverseStr(string):
    reversed_String = string[::-1]
    return reversed_String

# 8번
def introduce():
    name = input("이름을 입력하세요 : ")
    hobby = input("취미를 입력하세요 : ")
    school = input("재학 중인 학교를 입력하세요 : ")
    birthday = input("생일을 입력하세요 : ")
    month = int(birthday[2:4])
    day = int(birthday[4:6])

    sentence = f"제 이름은 {name}입니다. 취미는 {hobby}입니다. 저는 {school}를 다니고 있습니다. 제 생일은 {month}월 {day}일 입니다."
   
    print(sentence)

#introduce()
#신입생 교육 당시 f-string에 대해서 배우지 않았던 것 같은데 이렇게 코드를 짜도 될까요?

# 9번
def calc():
    a = int(input("첫 번째 수를 입력하세요 : "))
    b = int(input("두 번째 수를 입력하세요 : "))
    print("두 수의 합 : ",a+b)
    print("두 수의 차 : ",abs(a-b))
    print("두 수의 곱 : ",a*b)
    print("두 수의 몫 : ",a%b)

#calc()