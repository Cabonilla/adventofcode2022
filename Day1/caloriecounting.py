fileObj = open('input.txt', 'r')
data = fileObj.read()
read_data = data.split('\n') 

big_dump = {}
curr_ent = 1

# for i in read_data:
# 	if i:
# 		print(i)

# For the entire array.
# for i in read_data:
# 	if i != '':
# 		if curr_ent not in big_dump:
# 			big_dump[curr_ent] = [int(i)]
# 		else:
# 			big_dump[curr_ent].append(int(i))
# 	else:
# 		curr_ent += 1

# For only running sums.
for i in read_data:
	if i != '':
		if curr_ent not in big_dump:
			big_dump[curr_ent] = int(i)
		else:
			big_dump[curr_ent] += int(i)
	else:
		curr_ent += 1

# Part 1 Answer
# max_index = max(big_dump, key=big_dump.get)
# print(big_dump[max_index])

top_three = []

for j in range(3):
	max_index = max(big_dump, key=big_dump.get)
	top_three.append(big_dump[max_index])
	del big_dump[max_index]

# Part 2 Answer
print(sum(top_three))
