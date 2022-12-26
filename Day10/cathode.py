# fileObj = open('example.txt', 'r')
# fileObj = open('larger_example.txt', 'r')
fileObj = open('input.txt', 'r')
data = fileObj.read()
read_data = data.split('\n')

cycle_arr = []
X = 1
sig_sum = 0

sig_str = [20, 60, 100, 140, 180, 220]

# Answer Part I

# curr_cyc = 1

# for line in range(1, len(read_data) + 1):
# 	cmd = read_data[line - 1].split(' ')
# 	if cmd[0] == 'noop':
# 		curr_cyc += 1
# 		cycle_arr.append([curr_cyc, X])
# 	elif cmd[0] == 'addx':
# 		curr_cyc += 1
# 		cycle_arr.append([curr_cyc, X])
# 		curr_cyc += 1
# 		X += int(cmd[1])
# 		cycle_arr.append([curr_cyc, X])

# for i in cycle_arr:
# 	if i[0] in sig_str:
# 		sig_sum += i[0] * i[1]

# print(sig_sum)

pic_lns = ''
pic_arr = []
curr_cyc = 0

for line in range(1, len(read_data) + 1):
	cmd = read_data[line - 1].split(' ')
	if cmd[0] == 'noop':
		if curr_cyc % 40 in [X - 1, X, X + 1]:
			pic_lns += "#"
		else:
			pic_lns += "."
		curr_cyc += 1
	elif cmd[0] == 'addx':
		if curr_cyc % 40 in [X - 1, X, X + 1]:
			pic_lns += "#"
		else:
			pic_lns += "."
		curr_cyc += 1
		if curr_cyc % 40 in [X - 1, X, X + 1]:
			pic_lns += "#"
		else:
			pic_lns += "."
		curr_cyc += 1
		X += int(cmd[1])

ln_size = 40

pic_screen = [pic_lns[i:i + ln_size] for i in range(0, len(pic_lns), ln_size)]

for i in pic_screen:
	print(i)