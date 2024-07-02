'''
def function():
  print("hello function)
'''

for ch in 'prashantjha': 
    print(ch)
    if ch== 'h'or ch=='j':
        break
print('Current Letter:',ch)

ch=ord(input("Enter any character "))
if ch>=65 and ch<=91:
    print("your entered character is in upper case")
elif ch>=97 and ch<=122:
    print("your entered character is in lower case")
elif ch>=48 and ch<=57:
      print("your entered character in digit")
else:
 print("your entered character is inspecial symbol")
