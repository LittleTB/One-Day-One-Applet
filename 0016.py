import json
import xlwt


wb = xlwt.Workbook()
ws = wb.add_sheet('numbers')

with open(r'C:\Users\17156\Desktop\numbers.txt') as f:
    content = f.read()
json = json.loads(content)
i = 0
for con in json:
    j = 0
    for item in con:
        print(item)
        ws.write(i, j, item)
        j += 1
    i += 1
wb.save(r'C:\Users\17156\Desktop\num.xls')