import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/navarre_weather_2017-2022.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print (index, column_header)
    # # Get precipitation from this file.
    # dates, highs = [], []
    # for row in reader:
    #     current_date = datetime.strptime(row[5], '%Y-%m-%d')
    #     dates.append(current_date)
    #     high = int(row[10])
    #     highs.append
        

# # Plot the high temperatures.
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(dates, prcps, c='red')

# # Format plot.
# ax.set_title("Daily precipitation - 2017-2022", fontsize=24)
# ax.set_xlabel('', fontsize=16)
# fig.autofmt_xdate()
# ax.set_ylabel("Precipitation (in inches)", fontsize=16)
# ax.tick_params(axis='both', which='major', labelsize=16)

# plt.show()