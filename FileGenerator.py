from contextlib import redirect_stdout

def generate_shift_load_data(start_row, end_row, output_filename="ShiftLoad.csv"):
    cell_list1 = ['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'ag', 'ah', 'ai', 'aj', 'ak', 'al']
    cell_list2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    
    with open(output_filename, 'a') as f:
        with redirect_stdout(f):
            for i in range(start_row, end_row + 1):
                for x in cell_list1:
                    for y in cell_list2:
                        print(f"=EmployeeShiftImport.xlsx!{x}{i},=Oncall!{x}{i},=Oncall!F{i},=Oncall!D{i},=Oncall!B{i},{y}/01/2021", sep='')

generate_shift_load_data(6, 76)
