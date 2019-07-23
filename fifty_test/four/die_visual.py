from fifty_test.four.die import Die
import pygal

die_1 = Die()
die_2 = Die(10)

results = []
for i in range(1, 50000):
    results.append(die_1.roll()+die_2.roll())

frequencies = []
for value in range(2, die_1.num+die_2.num+1):
    frequencies.append(results.count(value))

# print(frequencies)
# print(results)

hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = [str(i) for i in list(range(2, 17))]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual_6_10.svg')





