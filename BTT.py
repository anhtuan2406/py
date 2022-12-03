# '''câu 1'''
# t=int(input('Nhập số dòng: '))
# if 0 < t <= 100:
#     for i in range(1,t+1):
#         x=input(f'Nhập test {i}: ')
#         print(f'Test {i}: ')
#         print(x.title())

# '''câu 3'''
# def dem():
#     n = input(f'Nhập test {i}: ')
#     b = n.split()
#     return len(b)
# t=int(input('Nhập số dòng: ', ))
# if 0 < t <= 100:
#     for i in range(1, t+1):
#            print(f'Test {i}: {dem()}', '\n')

# '''câu 4'''
# t = int(input("Nhập số dòng: "))
# if 0 < t <= 100:
#     for i in range(1, t + 1):
#         x= input("Nhập chữ: ")
#         print(f'Test {i}:')
#         print(x.replace("\t", " "))

# '''câu 5'''
# t = int(input("Nhập số dòng: "))
# if 0 < t <= 100:
#     for i in range(1, t+1):
#            x = input("Nhập chuỗi vào: ")
#            y = input("Nhập chuỗi cần tìm vào: ")
#            print (f'Test {i}: ', x.count(y))

# '''câu 6'''
# def str_thaytu(x1, x2, x3):
#     print(x1.replace(x2, x3))
#
# t = int(input("Nhập số dòng: "))
# if 0 < t <= 100:
#     for i in range(1, t+1):
#         x1 = input("Nhập chuỗi: ")
#         x2 = input("Nhập chuỗi thay thế cũ: ")
#         x3 = input("Nhập chuỗi thay thế mới: ")
#         print(f"test {i}:", end="\n")
#         str_thaytu(x1, x2, x3)

# '''câu 7'''
# t = int(input("Nhập số dòng: "))
# for i in range(1, t+1):
#     x= [x for x in input("Nhập chuỗi: ").split()]
#     y = set()
#     print(f"Test {i}: ")
#     for i in x :
#         if i not in m:
#             print(f'{i} ', end='')
#             y.add(i)
#     print()
