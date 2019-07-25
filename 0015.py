import json
import xlwt

wb = xlwt.Workbook()
ws = wb.add_sheet('city')

with open(r'C:\Users\17156\Desktop\city.txt') as f:
    content = f.read()

json = json.loads(content)
i = 0
for con in json:
    ws.write(i, 0, con)
    ws.write(i, 1, json.get(con))
    i += 1
wb.save(r'C:\Users\17156\Desktop\city.xls')