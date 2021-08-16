import numpy as np
def load_luna_park_data_to_lists(csv_file):
    with open(csv_file) as f: # "with" statement handles file opening and closing
        rides_list = f.readline().rstrip().split(',')[1:]
        data_table, names_list = [], []
        for line in f:
            line_tokens = line.rstrip().split(',')
            name = line_tokens[0]
            names_list.append(name)
            data_table.append([int(count) for count in line_tokens[1:]])  # add next table row
    return rides_list, names_list, data_table

#def load_luna_park_data_to_arrays(csv_file):
   # pass  # delete this pass command and write your code instead

x=load_luna_park_data_to_lists('luna_park1.cvs')
print (x)
