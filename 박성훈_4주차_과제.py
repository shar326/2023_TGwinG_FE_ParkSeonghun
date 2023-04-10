# # your code 를 지우고 그 부분에 본인의 코드를 작성해주세요.
# 4주차 과제에는 출력이나 입력을 요구하는 문제가 없습니다. print(), input() 사용하지 마세요.
# 코드 실행 시 컴파일 에러, 런타임 에러가 발생하면 해당 문제 0점 처리하겠습니다.
# 함수 이름 변경하지 마세요. 변경 시 해당 문제 0점 처리 하겠습니다.
# 제출 기한 : 2023년 4월 10일 23시 59분
# 지각 제출 기한 : 2023년 4월 11일 23시 59분

# 1번
def double(lst):
    number_count = 0
    for i in lst:
        if i*2 in lst:
            number_count = number_count + 1
    return number_count


# 2번
def pascal(n):
    pascal_triangle = [1]
    for i in range(1,n):
        up_row = pascal_triangle[i-1]
        down_row = []
        down_row.append(1)
        for j in range(1,i):
            down_row.append(up_row[j-1] + up_row[j])
        down_row.append(1)
        pascal_triangle.append(down_row)

    return pascal_triangle[-1]


# 3번
def beerRefrigerator(n):
    
    return

# 4번 못풀었습니다..

# def matrixMul(mat1, mat2):
#     m = len(mat1)
#     n = len(mat2)
#     k = len(mat2[0])
    
#     multiply_result = m * [[0] * k]
    

#     for i in range(m):
#         for j in range(k):
#             for l in range(n):
#                 multiply_result[i][j] = multiply_result[i][j] + mat1[i][l] * mat2[l][j]
#     return multiply_result

# a=[[1,2],[3,4],[5,6]]
# b=[[-1,2,0],[0,0,3]]
# print(matrixMul(a,b))