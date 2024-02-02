import openpyxl
book = openpyxl.load_workbook('Attendance\Attendance.xlsx')
sheet = book.active
L = []
for i in range(1,10):
    x = '2022500'+str(i)
    L.append(x)
for i in range(10,100):
    x = '202250'+str(i)
    L.append(x)
for j in range(len(L)):
    sheet.cell(row=j+1,column = 1).value = int(L[j])
    book.save('Attendance\Attendance.xlsx')

