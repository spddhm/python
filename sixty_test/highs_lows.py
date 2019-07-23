# import csv
# filename = 'Beijing_2014.csv'
# with open(filename, 'r', encoding='UTF-8') as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     print(header_row)

# import csv
# filename = 'Beijing_2014.csv'
# with open(filename, 'r', encoding='UTF-8') as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     for index, column_header in enumerate(header_row):
#         print(index, column_header)


# import csv
# filename = 'Beijing_2014.csv'
# with open(filename, 'r', encoding='UTF-8') as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     highs = []
#     for row in reader:
#         highs.append(int(row[1]))
#
#     print(highs)


# import csv
# from matplotlib import pyplot as plt
# from datetime import datetime
# filename = 'Beijing_2014.csv'
# with open(filename, 'r', encoding='UTF-8') as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     dates, highs = [], []
#     for row in reader:
#         dates.append(datetime.strptime(row[0], "%Y-%m-%d"))
#         highs.append(int(row[1]))
#
#     # 根据数据绘制图形
#     fig = plt.figure(dpi=128, figsize=(10, 6))
#     plt.plot(dates, highs, c='red')
#
#     # 设置图形的格式
#     plt.title("Temperature(Celsius)(high), July 2014", fontsize=24)
#     plt.xlabel('', fontsize=16)
#     fig.autofmt_xdate()
#     plt.ylabel("Temperature(F)", fontsize=16)
#     plt.tick_params(axis='both', which='major', labelsize=16)
#
#     plt.show()


import csv
from matplotlib import pyplot as plt
from datetime import datetime
filename = 'Beijing_2014.csv'
with open(filename, 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)

















