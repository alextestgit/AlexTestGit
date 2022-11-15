# def revert_num(num):
#     dig = 0
#     while num > 0:
#         dig = dig * 10 + num % 10
#         num = num // 10
#     return dig
#
# numberes = (12, 120, 80,185)
# for number in numberes:
#     print(number, "Revert number : ", revert_num(number))

#
# a=[1,2,3,4,5,6]
# print((a))
# b=a[-1],a[0]
# a[0],a[-1]=b
# print (a)
#
# c,*d,e=a
# print(d)


# def isPerfectNumber (num):
#     sum =0
#     for i in range(1,num-1):
#         if num % i == 0:
#             sum += i
#     return sum == num
#
#
# my_test = {6:True,28:True,496:True,8128:True, 17:False}
# for num, expect in my_test.items():
#     print("Is ", num , "Perfect Number ? ",isPerfectNumber(num) )

# ------------------- print prime numbers from 1 to N

# prime_num ={2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
# test = (8, 100)
#
# def prime_numbers(num):
#     rez = set()
#     for test_num in range(2,num):
#         prime = True
#         for i in range(2,test_num):
#             if test_num % i == 0:
#                 prime= False
#                 break
#         if prime :
#             # print(test_num)
#             rez.add(test_num)
#     return rez
#
#
# for i in test:
#     msg = f'Wotng rezault of  prime_numbers nethod where number is {i}'
#     assert  set (prime_numbers(i)) .issubset(prime_num) , msg
#     print(prime_numbers(i))


# ---------------------- Fibonacci number ----------------


fibonacci_number = {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 9: 34}


def fibonacci(num):
    if num == 0: return 0
    if num == 1: return 1
    curent = 1
    last = 1
    beforeLast = 1
    for i in range(num - 2):
        curent = last + beforeLast
        beforeLast = last
        last = curent
    return curent


print("Num\tResult\tExpect")
for num, expect in fibonacci_number.items():
    print(f'{num}\t{fibonacci(num)}\t{expect} ')
    msg = f'{num} function result {fibonacci(num)} expect {expect}'
    assert fibonacci(num) == expect, msg


