import matplotlib.pyplot as plt
from fifty_test.three.random_water import RandomWater

water = RandomWater(5000)
water.fill_water()

point_numbers = list(range(water.num))
plt.plot(water.x_values, water.y_values,  linewidth=3)
# plt.title("ddd", fontsize=24)
# plt.xlabel("xxx", fontsize=18)
# plt.ylabel("yyyyy", fontsize=18)

# plt.plot(0, 0, 'ro', linewidth=1)
# plt.plot(water.x_values[-1], water.y_values[-1], 'ro', linewidth=1)

# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)


plt.show()

