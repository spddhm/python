
# filename = 'programming.txt';
# with open(filename, 'w') as file_object:
#     file_object.write("I'm study python programming.");


# filename = 'programming.txt';
# with open(filename, 'w') as file_object:
#     file_object.write("I'm study python programming.\n");
#     file_object.write("I'm working with java\n");


# filename = 'programming.txt';
# with open(filename, 'a') as file_object:
#     file_object.write("I also love finding meaning in large datasets.\n");
#     file_object.write("I love creating apps that can run in a browser.\n");


# 练习1
# filename = 'guest.txt'
# with open(filename, 'w') as file_object:
#     name = input("please input your name: ");
#     file_object.write(name+"\n");

# 练习2
filename = 'guest_book.txt'
with open(filename, 'a') as file_object:
    name = input("please input your name: ");
    while name!='exit':
        file_object.write(name+"\n");
        name = input("please input your name: ");














