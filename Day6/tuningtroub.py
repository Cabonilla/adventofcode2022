fileObj = open('input.txt', 'r')
# fileObj = open('example.txt', 'r')
data = fileObj.read()

head, tail = 0, 0

id = ''
id_len = 0

id_four = ''
id_four_pos = 0

# Answer Part I

# while tail < len(data):
# 	if data[tail] not in id:
# 		id += data[tail]
# 		tail += 1
# 		id_len = max(id_len, len(id))
# 		if id_len == 4:
# 			id_four = id
# 			id_four_pos = head
# 			break
# 	else:
# 		head += 1
# 		maxLen = max(id_len, len(id))
# 		id = id[1:]

# Answer Part II

while tail < len(data):
	if data[tail] not in id:
		id += data[tail]
		tail += 1
		id_len = max(id_len, len(id))
		if id_len == 14:
			id_four = id
			id_four_pos = head
			break
	else:
		head += 1
		maxLen = max(id_len, len(id))
		id = id[1:]

print(id_four)
print(id_four_pos + 14)