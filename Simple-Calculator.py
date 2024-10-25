print("simple calculator")
print("-"*30)
first_num=int(input("enter the first value :"))
second_num=int(input("enter the second value :"))
print("*"*30)
print("choose one from below choices")
print("*"*30)
print("1 for addition\n2 for subtraction\n3 for multiplecation\n4 for division")
print("*"*30)
choice=int(input("enter your choice :"))
if choice==1:
    print(f"Result of {first_num} + {second_num} = {first_num + second_num}")
elif choice==2:
    print(f"Result of {first_num} - {second_num} = {first_num - second_num}")
elif choice==3:
    print(f"Result of {first_num} * {second_num} = {first_num * second_num}")
else:
    print(f"Result of {first_num} / {second_num} = {first_num / second_num}")