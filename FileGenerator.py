# SKS 12/31/2020
# https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file-using-python 
# Since Python 3.4 there's a simple context manager available to redirect print stdout to file in standard library:
from contextlib import redirect_stdout
# https://www.w3schools.com/python/python_lists.asp
CellList1 = ['h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','aa','ab','ac','ad','ae','af','ag','ah','ai','aj','ak','al']
CellList2 = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
# https://www.w3schools.com/python/python_while_loops.asp
i = 6
while i < 76:
# https://www.w3schools.com/python/python_for_loops.asp
    for x in CellList1:
# https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file-using-python
        with open('FShiftCode.txt', 'a') as f:
            with redirect_stdout(f):
# https://www.geeksforgeeks.org/python-sep-parameter-print/ removing spaces between arguments.
                print('=EmployeeShiftImport.xlsx!',x,i, sep='')
        with open('FOnCallCode.txt', 'a') as f:
            with redirect_stdout(f):
                print('=Oncall!',x,i, sep='')
        with open('FMember.txt', 'a') as f:
            with redirect_stdout(f):
                print('=Oncall!F',i, sep='')
        with open('FEmail.txt', 'a') as f:
            with redirect_stdout(f):
                print('=Oncall!D',i, sep='')
        with open('FGroup.txt', 'a') as f:
            with redirect_stdout(f):
                print('=Oncall!B',i, sep='')
    i += 1
i = 6
while i < 76:
    for y in CellList2:
        with open('FShiftDate.txt', 'a') as f:
            with redirect_stdout(f):
                print(y,'/01/2021', sep='')
    i += 1