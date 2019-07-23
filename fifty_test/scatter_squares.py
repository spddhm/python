# import matplotlib.pyplot as plt
# plt.scatter(2, 4, s=200)
# # 设置图表标题并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square")
# plt.show()

# import matplotlib.pyplot as plt
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.scatter(x_values, y_values, s=200)
# plt.show()

# import matplotlib.pyplot as plt
# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]
# plt.scatter(x_values, y_values, s=40, edgecolors='none', c=(0, 0.8, 0))
# # 设置图表标题并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square")
#
# plt.axis([0, 1100, 0, 1100000])
# plt.show()

# import matplotlib.pyplot as plt
# x_values = list(range(1001))
# y_values = [x**2 for x in x_values]
# plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)
# # plt.show()
# plt.savefig('squares_plot.png', bbox_inches='tight')



# 练习 1
# import matplotlib.pyplot as plt
# x_values = list(range(5))
# y_values = [x**3 for x in x_values]
# plt.scatter(x_values, y_values, s=40)
# plt.title("dong", fontsize=24)
# plt.xlabel('x轴', fontsize=16)
# plt.ylabel('y轴', fontsize=16)
# plt.show()

# 练习 2
import matplotlib.pyplot as plt
x_label = list(range(5000))
y_label = [x**3 for x in x_label]
plt.scatter(x_label, y_label, c=y_label, edgecolors='none', s=40)
plt.title('dong', fontsize=24)
plt.xlabel('xxx', fontsize=16)
plt.ylabel('yyy', fontsize=16)
plt.axis([0, 1100, 0, 999900000])
plt.show()












