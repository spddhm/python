# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
# class Battery():
#     def __init__(self, battery_size=80):
#         self.battery_size = battery_size;
#
#     def describe_battery(self):
#         """ 打印一条描述电瓶容量的消息 """
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
# class ElectricCar(Car):
#     """ 电动汽车的独特之处 """
#     def __init__(self, make, model, year):
#         """ 初始化父类的属性 """
#         super().__init__(make, model, year)
#         self.battery = Battery()
#
#     def describe_battery(self):
#         """ 打印一条描述电瓶容量的消息 """
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# # my_tesla.describe_battery()
# my_tesla.battery.describe_battery()



# import class_test.dog
# # 练习1
# class IceCreamStand(class_test.dog.Restaurant):
#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type);
#         self.flavors = ['ice1', 'ice2', 'ice3'];
#     def showIces(self):
#         for row in self.flavors:
#             print(" -- " + row)
# newIce = IceCreamStand('aa','bb')
# newIce.showIces()

# 练习2
# import class_test.dog
# class Admin(class_test.dog.User):
from class_test.dog import User
class Admin(User):
    def __init__(self, first_name, last_name, addr, phone, login_attempts):
        super().__init__(first_name, last_name, addr, phone, login_attempts);
        # self.privileges = [ "can add post" , "can delete post" , "can ban user"];
        self.privileges = Privileges()
    # def show_privileges(self):
    #     print(self.privileges[0]);
# user = Admin('su', 'dongdong', 'shenzhen', '15512312344', 1)
# user.describe_user()
# user.show_privileges()

class Privileges():
    def __init__(self):
        self.privileges = [ "can add post" , "can delete post" , "can ban user"];
    def show_privileges(self):
        print(self.privileges[0]);
user = Admin('su', 'dongdong', 'shenzhen', '15512312344', 1)
user.describe_user()
user.privileges.show_privileges()









