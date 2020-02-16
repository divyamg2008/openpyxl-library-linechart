import csv
#from matplotlib import pyplot as plt
import openpyxl
from openpyxl.chart import LineChart,Reference
fo = open("input.csv", "r")
#reader = csv.Reader(fo)
a = []

for row in fo:
    a.append(row)

#     c.append(row['height'])
# plt.plot(a, b, color='green')
# plt.ylabel('Total %')
# plt.xlabel('Sl.No', color='red')
# plt.title('my plot')

# plt.plot(a, c, color='yellow')
# plt.ylabel('Total %')
# plt.xlabel('Sl.No', color='red')
# plt.title('2nd plot')
# plt.savefig('lineplot.pdf')

wb = openpyxl.Workbook() 
sheet = wb.active
count = 0
for i in a:  
    x = i.split(',')
    count+=1
    if count ==1:
    #    x=i.split(',')
        sheet.append([x[0],x[1],x[2],x[3]])
    else:
        sheet.append([int(x[0]),int(x[1]),int(x[2]),int(x[3])])

values = Reference(sheet, min_col = 2, min_row = 1, 
                          max_row = 10,max_col = 4) 

chart = LineChart() 
  
chart.add_data(values, titles_from_data=True) 

chart.title = " LINE-CHART "
  
# set the title of the x-axis 
chart.x_axis.title = " no. "
  
# set the title of the y-axis 
chart.y_axis.title = " total "
  
# add chart to the sheet 
# the top-left corner of a chart 
# is anchored to cell E2 . 

sheet.add_chart(chart, "E2") 

# save the file 

wb.save("output.xlsx") 