# Solution-01
my_str = str(input())
if len(my_str)>2:
    print(my_str[:2] + my_str[-2:])
else:
    print("")

# Solution-02
my_str = str(input())
req_len = len(my_str)-1
print(my_str[0]+ req_len * '@')

#Solution-03
my_str = input()
len_my_str = len(my_str)

if len_my_str <=3:
    print(my_str)

elif my_str[-3:] == 'ing':
    print(my_str + 'ly')
else:
    print(my_str + 'ing')

#Solution-04
my_str = input()
new_str = my_str[-1] + my_str[1:-1] + my_str[0]
print(new_str)


#Solution-05
my_str = input()
if len(my_str) > 7 and len(my_str) % 2 != 0:
    mid_index = len(my_str) // 2
    print(my_str[mid_index - 1:mid_index + 2])

#solution-06
s1 = input()
s2 = input()
mid_index = len(s1) // 2
s3 = s1[:mid_index] + s2 + s1[mid_index:]
print(s3)

#solution-07
my_str = input()
rev_my_str = my_str[::-1]
print(rev_my_str)

#Solution-08
my_str = input()
new_str = my_str.split('-')
print(new_str)

#Solution-09
my_str = input()
is_binary = True

for char in my_str:
    if char != '0' and char != '1':
        is_binary = False
        break
if is_binary:
    print("Yes")
else:
    print("No")

#Solution-10
my_str = input()
print(my_str.lower())
