#Ex-1
# mylist = ["apple", "banana", "cherry"]
#
# mylist_len = len(mylist)
#
# while mylist_len > 0:
#     print(mylist[mylist_len-1])
#     mylist_len -=1

#Ex-2
#
# list_1 = ["na", "de", "mon"]
# list_2 = ["me", "sh", "day"]
#
# listlen = len(list_1)
#
# for i in range(listlen):
#     print(list_1[i]+list_2[i])

# #EX-3
# mylist = ["1", "2", "3","4"]
# new_list = []
#
# for i in range (len(mylist)):
#     num = int(mylist[i]) * int(mylist[i])
#     new_list.append(num)
# print(*new_list)

# #Ex-4
# #
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# list3 = []
#
# listlen = len(list1)
#
# for i in  list1:
#     word = list1[i]+list2[i]
#     list3.append(word)
# print(list3)

# #Ex-5
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
#
# print(*list1)
# print(*list2[::-1])

# #Ex-6
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# list2 = []
#
# for item in list1:
#     if item != "":
#         list2.append(item)
# print(list2)

# #Ex-8
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub_list = ["h", "i", "j"]
#
# for item in list1:
#     print(*item)

# #Ex-9
# list1 = [5, 10, 15, 20, 25, 50, 20]
#
# index = list1.index(15)
# list1[index] = 150
# print(list1)

# #Ex-10
# list1 = [5, 20, 15, 20, 25, 50, 20]
#
# for item in list1:
#     if item == 20:
#         list1.remove(item)
# print(list1)







# https://pynative.com/python-list-exercise-with-solutions/#h-exercise-4-concatenate-two-lists-in-the-following-order