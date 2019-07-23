
# class Dog():
#     """一次模拟小狗的简单尝试"""
#     def __init__(self, name, age):
#         """ 初始化属性 name 和 age"""
#         self.name = name
#         self.age = age
#     def sit(self):
#         """ 模拟小狗被命令时蹲下 """
#         print(self.name.title() + " is now sitting.")
#     def roll_over(self):
#         """ 模拟小狗被命令时打滚 """
#         print(self.name.title() + " rolled over!")
#
# my_dog = Dog('xiaohei', 3)
# print(my_dog.name)
# print(my_dog.age)
# my_dog.sit()
# my_dog.roll_over()


#
# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name;
#         self.cuisine_type = cuisine_type;
#         self.number_served = 13;
#     def describe_restaurant(self):
#         print(self.restaurant_name);
#         print(self.cuisine_type);
#         print(self.number_served);
#     def open_restaurant(self):
#         print("working....");
#     def set_number_served(self, update_num):
#         self.number_served = update_num;
#     def increment_number_served(self, dizeng):
#         self.number_served += dizeng;

# rest = Restaurant('参订', '666')
# rest.set_number_served(44)
# rest.increment_number_served(10)
# rest.describe_restaurant()
# rest.open_restaurant()



class User():
    def __init__(self, first_name, last_name, addr, phone, login_attempts):
        self.first_name = first_name;
        self.last_name = last_name;
        self.addr = addr;
        self.phone = phone;
        self.login_attempts = login_attempts;
    def describe_user(self):
        print(self.first_name + "-" + self.last_name);
        print(self.addr + "-" + self.phone);
    def greet_user(self):
        print("42213213");
    def increment_login_attempts(self):
        self.login_attempts += 1;
        print(self.login_attempts);
    def reset_login_attempts(self):
        self.login_attempts = 0;
        print(self.login_attempts);
#
# user = User("su", 'dong', '深圳', '15512332123', 5)
# user.describe_user()
# user.greet_user()
# user.increment_login_attempts();
# user.increment_login_attempts();
# user.increment_login_attempts();
# user.increment_login_attempts();
# user.reset_login_attempts()







