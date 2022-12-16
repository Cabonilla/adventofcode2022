fileObj = open('input.txt', 'r')
# fileObj = open('example.txt', 'r')
data = fileObj.read()

head, tail = 0, 0

id = ''
id_len = 0

# Answer Part I

# id_four = ''
# id_four_pos = 0

# while tail < len(data):
# 	if data[tail] not in id:
# 		id += data[tail]
# 		tail += 1
# 		id_len = max(id_len, len(id))
# 		if id_len == 4:
# 			id_four = id
# 			id_four_pos = tail
# 			break
# 	else:
# 		head += 1
# 		maxLen = max(id_len, len(id))
# 		id = id[1:]

# print(id_four)
# print(id_four_pos)

# Answer Part II

id_fourteen = ''
id_fourteen_pos = 0

while tail < len(data):
	if data[tail] not in id:
		id += data[tail]
		tail += 1
		id_len = max(id_len, len(id))
		if id_len == 14:
			id_fourteen = id
			id_fourteen_pos = tail
			break
	else:
		head += 1
		maxLen = max(id_len, len(id))
		id = id[1:]

print(id_fourteen)
print(id_fourteen_pos)