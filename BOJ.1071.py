# 시행착오 1
# N = int(input())
# L = list(map(int, input().split()))
#
# j = 0
# while j <= N - 2:
#     if L[j] + 1 == L[j + 1]:
#         L.append(L.pop(j))
#         if j > 0:
#             j -= 1
#     else:
#         j += 1
#
# print(*L)
# 예제 1이 순서가 안맞음
#
# 시행착오 2
# N = int(input())
# L = list(map(int, input().split()))
#
# j = 0
# while j <= N - 2:
#     if L[j] + 1 == L[j + 1]:
#         L.insert(0, L.pop(j))
#     else:
#         j += 1
#
# print(*L)
# 예제 4가 순서가 안맞음
#
# # 시행착오 3
# N = int(input())
# L = list(map(int, input().split()))
#
# j = 0
# while j <= N - 2:
#     if L[j] + 1 == L[j + 1]:
#         # 바꾸고 돌아가기
#         L[j], L[j+1] = L[j+1], L[j]
#         if j > 0:
#             j -= 1
#     else:
#         j += 1
#
# print(*L)
# 예제 4가 순서가 안맞음
#
#
# 시행착오 4
# N = int(input())
# L = list(map(int, input().split()))
#
# j = 0
# while j <= N - 3:
#     if L[j] + 1 == L[j + 1]:
#         # 아예 뒤쪽을 바꾸기
#         L[j+1], L[j+2] = L[j+2], L[j+1]
#     else:
#         j += 1
#
# if L[-2] + 1 == L[-1]:
#     L[-2], L[-1] = L[-1], L[-2]
#
# print(*L)
# # 예제 2, 5에서 문제 발생..
#
#
# # 시행착오 5
# N = int(input())
# L = list(map(int, input().split()))
#
# j = 0
# while j < N - 1:
#     if L[j] + 1 == L[j + 1]:
#         # 아예 뒤쪽을 바꾸기 그런데 이제 케이스를 곁들인
#         if j < N -2:
#             if L[j + 1] == L[j + 2]:
#                 k = 1
#                 # 일단 아웃오프랭지 방지
#                 while True:
#                     if j + k < N:
#                         if L[j+1] == L[j+k]:
#                             k += 1
#                         else:
#                             L[j], L[j+k-1] = L[j+k-1], L[j]
#                             break
#                     else:
#                         L.append(L.pop(j))
#                         if j > 0:
#                             j -= 1
#                         break
#             else:
#                 L[j+1], L[j+2] = L[j+2], L[j+1]
#         else:
#             L[-1], L[-2] = L[-2], L[-1]
#         if j > 0:
#             j -= 1
#     else:
#         j += 1
#
# print(*L)
# # 예제 5에서 문제 발생..
# 이러한 방식으로는 예제 5와 예제 4를 동시에 해결하는 것이 불가능함을 깨달음.

"""
조건을 분석해보자.
먼저, 사전순으로 가장 빠른 문자열을 출력하므로, 같은 수는 모두 이어져있어야 한다.
주어진 수에서 가장 작은 수는 다음 경우를 제외하고 반드시 가장 앞에 존재한다.
- Set의 개수가 2이고, 두 수가 연속됨
    - 이 경우에서는 두 수의 자리가 뒤바뀐것이 올바른 출력이다.
    - 이를 Case Alpha라 하자.

이 조건을 이용한다면, 주어진 수 list를 set으로 변환한 후, 위 경우인지 확인한다.
그 다음, 가장 작은 수를 가장 앞에 넣고, 남은 수들로 다시 실행한다
-> 재?귀적 구성
ㅎㅊㅇㄴ?

주의 할 점
1. 주어지는 수는 연속되지 않을 수 있다.
2. 주어지는 수는 정렬되어 있지 않다.
3. N이 1일 수 있다.
"""
#
# N = int(input())
# L = list(map(int, input().split()))
# S = list(set(L))
#
# if N != 1:  # N이 1이면 아래 판별식에서 IndexError가 나므로, 먼저 판별해주어야 한다.
#     if len(S) == 2 and (S[0] + 1 == S[1] or S[1] + 1 == S[0]):  # Case Alpha의 판별
#         L.sort(reverse=True)
#         print(*L)
#     else:  # 일반적인 상황의 방법
#         outList = []
#         while True:
#             cS = S.copy()
#             scS = set(cS)
#             cS = list(scS - set(outList))
#             if len(outList) > 0 and outList[-1] + 1 in cS:
#                 cS.remove(outList[-1] + 1)
#             if len(cS) == 0:
#                 break
#             if len(cS) == 2 and (cS[0] + 1 == cS[1] or cS[1] + 1 == cS[0]):
#                 cS.sort(reverse=True)
#                 outList.append(cS[0])
#                 outList.append(cS[1])
#                 break
#
#             outList.append(min(cS))
#
#         # 중복된 수를 다시 채워주는 과정.
#         LastList = []
#         for i in outList:
#             quantity = L.count(i)
#             if quantity != 1:
#                 for j in range(quantity):
#                     LastList.append(i)
#             else:
#                 LastList.append(i)
#         print(*LastList)
# else:
#     print(*L)

# case input: 0 0 1 1 3 3에서 실패함...
# 이는 아까의 대전제 "같은 수는 모두 이어진다"가 틀렸음을 의미한다.
# idea: 굳이 중복수를 따로 분류해야할까? 그냥 한번에 정렬해!

# N = int(input())
# L = list(map(int, input().split()))
# S = list(set(L))
#
# if N != 1:  # N이 1이면 아래 판별식에서 IndexError가 나므로, 먼저 판별해주어야 한다.
#     if len(S) == 2 and (S[0] + 1 == S[1] or S[1] + 1 == S[0]):  # Case Alpha의 판별
#         L.sort(reverse=True)
#         print(*L)
#     else:  # 일반적인 상황의 방법
#         outList = []
#         while True:
#             cL = L.copy()
#             for i in outList:
#                 cL.remove(i)
#             if len(outList) > 0 and outList[-1] + 1 in cL:
#                 quantity = cL.count(outList[-1] + 1)
#                 for j in range(quantity):
#                     cL.remove(outList[-1] + 1)
#             # cS처럼 cL이 정의됨.
#             # cL이 0이거나 caseAlpha일 때 break
#             if len(cL) == 0:
#                 break
#             if len(cL) == 2 and (cL[0] + 1 == cL[1] or cL[1] + 1 == cL[0]):
#                 cL.sort(reverse=True)
#                 outList.append(cL[0])
#                 outList.append(cL[1])
#                 break
#
#
#             outList.append(min(cL))
#
#         print(*outList)
#
# else:
#     print(*L)
# 1 1 2 2 3 3에서 1 1 3 2 2로 가버리는 문제 발생. (왜냐하면, 1 1 3 이후 배열인 2 2 3은 case Alpha이기 때문!)

# N = int(input())
# L = list(map(int, input().split()))
# S = list(set(L))
#
# if N != 1:  # N이 1이면 아래 판별식에서 IndexError가 나므로, 먼저 판별해주어야 한다.
#     if len(S) == 2 and (S[0] + 1 == S[1] or S[1] + 1 == S[0]):  # Case Alpha의 판별
#         L.sort(reverse=True)
#         print(*L)
#     else:  # 일반적인 상황의 방법
#         outList = []
#         while True:
#             cL = L.copy()
#             for i in outList:
#                 cL.remove(i)
#             if len(outList) > 0 and outList[-1] + 1 in cL:
#                 quantity = cL.count(outList[-1] + 1)
#                 for j in range(quantity):
#                     cL.remove(outList[-1] + 1)
#             print(f"cL: {cL}")
#             # cS처럼 cL이 정의됨.
#             # cL이 0이거나 caseAlpha일 때 break
#             if len(cL) == 0:
#                 break
#
#             cS = list(set(cL))
#             if len(cS) == 2 and (cS[0] + 1 == cS[1] or cS[1] + 1 == cS[0]):
#                 cL.sort(reverse=True)
#                 outList += cL
#                 break
#
#
#             outList.append(min(cL))
#
#         print(*outList)
#
# else:
#     print(*L)
# Case input: 1 1 2 3 3 4 5에서 실패. (이유: 3이 연속될 수 없어서 잠시 cL에서 사라졌을때 Case Alpha라고 인식해버림.)
# 해결방안: Case Alpha의 판별을 연속된 수를 cL에서 잠시 제거하는 것보다 먼저 수행

N = int(input())
L = list(map(int, input().split()))
S = list(set(L))

if N != 1:  # N이 1이면 아래 판별식에서 IndexError가 나므로, 먼저 판별해주어야 한다.
    if len(S) == 2 and (S[0] + 1 == S[1] or S[1] + 1 == S[0]):  # Case Alpha의 판별
        L.sort(reverse=True)
        print(*L)
    else:  # 일반적인 상황의 방법
        outList = []
        while True:
            cL = L.copy()
            # 이미 outList에 들어간 수 지우기
            for i in outList:
                cL.remove(i)

            cS = list(set(cL))
            if len(cS) == 2 and (cS[0] + 1 == cS[1] or cS[1] + 1 == cS[0]):  # Case Alpha 판별
                cL.sort(reverse=True)
                outList += cL
                break

            # 연속되는 수 잠시 지우기
            if len(outList) > 0 and outList[-1] + 1 in cL:
                quantity = cL.count(outList[-1] + 1)
                for j in range(quantity):
                    cL.remove(outList[-1] + 1)
            # print(f"cL: {cL}") #디버깅용 코드
            # cS처럼 cL이 정의됨.
            # cL이 0이거나 caseAlpha일 때 break
            if len(cL) == 0:
                break


            outList.append(min(cL))

        print(*outList)

else:
    print(*L)
#성공!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!