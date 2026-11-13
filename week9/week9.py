# def odd(n):
#     if n % 2 == 0:
#         return False
#     else:
#         return True

# def leapYear(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 ==0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else :
#         return False
# print(leapYear(2024))

# def print_triangular_number(n):
#     total = 0
#     for i in range(1,n+1):
#         total += i
#         print(i,total)
# print_triangular_number(5)
# def is_prime(n):
#     if n < 2 :
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True
# print(is_prime(11))

# def reverse(s):
#     result = ""
#     for ch in s:
#       result = ch + result
#     return result
# print(reverse("hello"))

# def remove_all(sub, s):
#     return s.replace(sub, "")
#
#
# print(remove_all("l","hello world"))

# def substitute(message,key):
#     alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
#     result=""
#     for ch in message:
#       index = alphabet.find(ch.lower())
#       if index == -1:
#         result = result + ch
#       elif ch.isupper():
#         result = result + key[index].upper()
#       else:
#         result = result + key[index].lower()
#     return result
# key="zyvüutşsrpöonmlkjiıhgğfedabcç"
# print(substitute("Hello world",key))

# def remove_dups(s):
#     result = ""
#     for ch in s:
#       if ch not in result:
#           result += ch
#     return result
# print(remove_dups("annen"))