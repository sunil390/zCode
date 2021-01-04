# SKS 12/31/2020 Created output in multiple files
# SKS 01/01/2021 Created a single csv file
# SKS 04/01/2021 65000 rows created in windows
# https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file-using-python 
from contextlib import redirect_stdout
# https://www.w3schools.com/python/python_lists.asp
CellList1 = ['h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','aa','ab','ac','ad','ae','af','ag','ah','ai','aj','ak','al']
CellList2 = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
# https://www.w3schools.com/python/python_while_loops.asp
i = 6
while i < 76:
# https://www.w3schools.com/python/python_for_loops.asp
    for x in CellList1 :
        for y in CellList2 :
            with open('ShiftLoad.csv', 'a') as f:
                with redirect_stdout(f):
# https://www.geeksforgeeks.org/python-sep-parameter-print/ removing spaces between arguments.
                    print('=EmployeeShiftImport.xlsx!',x,i,',','=Oncall!',x,i,',','=Oncall!F',i,',','=Oncall!D',i,',','=Oncall!B',i,',',y,'/01/2021', sep='')
    i += 1
