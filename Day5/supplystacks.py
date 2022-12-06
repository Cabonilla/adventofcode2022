fileObj = open('input.txt', 'r')
# fileObj = open('example.txt', 'r')
data = fileObj.read()
read_data = data.split('\n')

split_index = read_data.index('')
schematic = read_data[0:split_index]
movements = read_data[split_index + 1: len(read_data)]

schem_keys = schematic.pop().split()
schem_dict = dict.fromkeys(schem_keys)
schem_values = []

for i in range(len(schematic) - 1, -1, -1):
	schem_line = schematic[i].replace('    ', ' ').replace('[', '').replace(']', '').split(' ')
	schem_values += [schem_line]

schem_values_rows = len(schem_values)
schem_values_cols = len(schem_values[0])

for r in range(schem_values_rows):
	for c in range(schem_values_cols): 
		place = f'{c + 1}'
		if schem_values[r][c] != '':
			if schem_dict[place] == None:
				schem_dict[place] = [schem_values[r][c]]
			else:
				schem_dict[place].append(schem_values[r][c])

# Answer Part I
# def removeCargo(dict, place, amount, to):
# 	temp_cargo = dict[f'{place}'][len(dict[f'{place}']) - amount:]
# 	dict[f'{place}'] = dict[f'{place}'][:len(dict[f'{place}']) - amount]
# 	dict[f'{to}'].extend(temp_cargo[::-1])

# Answer Part II
def removeCargo(dict, place, amount, to):
	temp_cargo = dict[f'{place}'][len(dict[f'{place}']) - amount:]
	dict[f'{place}'] = dict[f'{place}'][:len(dict[f'{place}']) - amount]
	dict[f'{to}'].extend(temp_cargo)	

for m in movements:
	tasks = [int(i) for i in m.split(' ') if i.isdigit()]
	removeCargo(schem_dict, tasks[1], tasks[0], tasks[2])

last_crate = ''

for c in schem_dict.values():
	last_crate += c[-1]

print(last_crate)