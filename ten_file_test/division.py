# try:
#     print(5 / 0)
# except ZeroDivisionError:
#     print("You can't divide by zero!");


# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ");
#     if first_number == "q":
#         break;
#     second_number = input("Second number: ");
#     if second_number == "q":
#         break;
#     try:
#         answer = int(first_number) / int(second_number);
#     except ZeroDivisionError:
#         print("You can't divide by 0!");
#     except ValueError:
#         print('ValueError.....')
#     else:
#         print(answer)



# 练习1
while True:
    try:
        num1 = input("first num: ");
        if num1 == "q":
            break;
        a = int(num1);
        num2 = input("second num: ");
        if num2 == "q":
            break;
        b = int(num2);
        res = a+b;
    except ValueError:
        # print('please input num');
        pass
    else:
        print(res);










