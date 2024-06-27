# def is_Palindrome(num):
#     string=str(num)
#     if string==string[::-1]:
#         return True
#     else:
#         return False

# num=int(input("enter a number"))
# if is_Palindrome(num):
#     print(f"{num} is palindrome")
# else:
#     print(f"{num} is not palindrome")

a=input("Enter a number")
if str(a)==a[::-1]:
    print("palindrome")
else:
    print("not")
