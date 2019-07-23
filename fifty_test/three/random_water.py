from random import choice
class RandomWater():
    def __init__(self, num=5000):
        self.num = num
        self.x_values = [0]
        self.y_values = [0]
    def fill_water(self):
        while len(self.x_values) < self.num:
            x_dir = choice([-1, 1])
            y_dir = choice([-1, 1])
            x_distance = choice([1,2,3,4,5])
            y_distance = choice([1,2,3,4,5])
            if x_dir==0 and y_dir == 0:
                continue
            x_speed = x_dir * x_distance
            y_speed = y_dir * y_distance
            # 计算下一个点的位置
            next_x = self.x_values[-1] + x_speed
            next_y = self.y_values[-1] + y_speed
            self.x_values.append(next_x)
            self.y_values.append(next_y)

