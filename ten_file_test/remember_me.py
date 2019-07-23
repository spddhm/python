# import json
# username = input("What is your name? ")
# filename = 'username.json'
# with open(filename, 'w') as f_obj:
#     # f_obj.write(username);
#     json.dump(username, f_obj)
#     print("We'll remember you when you come back, " + username + "!")


# import json
# filename = 'username.json'
# try:
#     with open(filename) as f_obj:
#         username = json.load(f_obj);
# except FileNotFoundError:
#     username = input("What is your name? ")
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj);
#         print("We'll remember you when you come back, " + username + "!")
# else:
#     print("Welcome back, " + username + "!")


# import json
# def greet_user():
#     filename = 'username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj);
#     except FileNotFoundError:
#         username = input("What is your name? ")
#         with open(filename, 'w') as f_obj:
#             json.dump(username, f_obj);
#             print("We'll remember you when you come back, " + username + "!")
#     else:
#         print("Welcome back, " + username + "!")
#
# greet_user()


# import json
# def get_stored_username():
#     filename = 'username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj);
#     except FileNotFoundError:
#         return None;
#     else:
#         return username;
# def greet_user():
#     username = get_stored_username();
#     if username:
#         print("Welcome back, " + username + "!")
#     else:
#         username = input("What is your name? ")
#         filename = 'username.json'
#         with open(filename, 'w') as f_obj:
#             json.dump(username, f_obj);
#             print("We'll remember you when you come back, " + username + "!")
#
# greet_user();


# import json
# def get_stored_username():
#     filename = 'username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj);
#     except FileNotFoundError:
#         return None;
#     else:
#         return username;
# def get_new_username():
#     username = input("What is your name? ")
#     filename = 'username.json'
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj);
#     return username;
#
# def greet_user():
#     username = get_stored_username();
#     if username:
#         print("Welcome back, " + username + "!")
#     else:
#         username = get_stored_username();
#         print("We'll remember you when you come back, " + username + "!")
#
# greet_user();



# 练习1
import json
def input_favorite_num():
    filename = 'favoriteNum.json'
    num = input(" input favorite num is : ");
    with open(filename, 'w') as f_obj:
        json.dump(num, f_obj);
    return num;
def load_favorite_num():
    filename = 'favoriteNum.json';
    try:
        with open(filename) as f_obj:
            num = json.load(f_obj);
    except FileNotFoundError:
        return None;
    else:
        return num;
def favoriteNum():
    num = load_favorite_num();
    if num:
        isRight = input("username is right? ");
        if isRight.upper() == "Y":
            print("load favorite num is: " + str(num));
        else:
            num = input_favorite_num();
            print("rename favorite num is: " + str(num));
    else:
        num = input_favorite_num();
        print("get favorite num is: " + str(num));
favoriteNum();





















