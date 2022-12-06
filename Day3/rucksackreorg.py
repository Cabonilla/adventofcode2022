# fileObj = open('example.txt', 'r')
fileObj = open('input.txt', 'r')
data = fileObj.read()
read_data = data.split('\n')

# Answer Part I

# char_sum = 0

# for i in read_data:
# 	sack_len = len(i)
# 	f_h = i[0:sack_len//2]
# 	s_h = i[sack_len//2: sack_len]
	
# 	c = [j for j in f_h if j in s_h][0]
# 	char_c = ord(c)
# 	if c.islower():
# 		char_sum += char_c - 96
# 	elif c.isupper():
# 		char_sum += char_c - 64 + 26

# print(char_sum)

# Answer Part II
char_sum = 0

sub_list = []

for i in range(0, len(read_data), 3):
	sub_list.append(read_data[i:i+3])

# print(l_t_sl)

for j in sub_list:
	c = [k for k in j[0] if k in j[1] and k in j[2]][0]
	char_c = ord(c)
	if c.islower():
		char_sum += char_c - 96
	elif c.isupper():
		char_sum += char_c - 64 + 26

print(char_sum)

