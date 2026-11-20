# myList = [76,92.3,"hello",True,4,76]
# print(myList)
# myList.append("apple")
# myList.append(76)
# print(myList)
# myList.insert(3,"cat")
# print(myList)
# myList.insert(0,99)
# print(myList)
# print(myList.index("hello"))
# print(myList.count(76))
# myList.remove(76)
# print(myList)
# myList.pop(myList.index(True))
# print(myList)
#
# def sum_of_squares(x):
#     sum = 0;
#     for num in x:
#         sum += num**2
#     return sum
#
# my_list= [3,4,5]
# print(sum_of_squares(my_list))

# def sum_evens(num_list):
#     sum=0
#     for num in num_list:
#         if num%2==0:
#             sum+=num
#     return sum
# print(sum_evens([1,2,3,4,5,6,7,8,9,10]))

# def count_five_letter(words):
#     counter = 0
#     for word in words:
#         if len(word) == 5:
#             counter += 1
#     return counter
# print(count_five_letter(['hello', 'world', 'world', 'emre']))

# def sum_until_even(num_list):
#     total=0
#     for num in num_list:
#         if num%2==0:
#             break
#         total+=num
#     return total
# my_List=[1,2,3,5,7,9]
# print(sum_until_even(my_List))

# def count_sam(words):
#     count=0
#     for word in words:
#          count+=1
#          if word == 'sam':
#            break
#     return count
# my_list=["hello","world","my","emre","sam"]
# print(count_sam(my_list))

# def replace(s,old,new):
#     pieces=s.split(old)
#     print(pieces)
#     print(new.join(pieces))
#     return new.join(pieces)
#
# def test(actual,expected):
#     if actual==expected:
#       print("PASSED")
#     else:
#       print("FAILED")
#
# test(replace("Mississippi","i","I"),"MIssIssIppI")
#
# def myintList(num_list):
#     max_value=num_list[0]
#     for num in num_list:
#       if num > max_value:
#          max_value=num
#      return max_value
# my_list=[3,2,1,0,5,7,8,10,2]
# new_list=[-34,-48,-42,-43,-2]
# print(myintList(my_list))
# print(myintList(new_list))