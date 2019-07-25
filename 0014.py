import xlwt
import json


with open(r'C:\Users\17156\Desktop\students.txt') as f:
    content = f.read()

wb = xlwt.Workbook()
ws = wb.add_sheet('student')
json = json.loads(content)
i = 0
for con in json:
    values = json.get(con)
    ws.write(i, 0, con)
    j = 1
    for value in values:
        ws.write(i, j, value)
        j += 1
    i += 1

wb.save(r'C:\Users\17156\Desktop\stu.xls')