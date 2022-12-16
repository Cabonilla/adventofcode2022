from collections import defaultdict

fileObj = open('input.txt', 'r')
# fileObj = open('input.txt', 'r')
data = fileObj.read()
read_data = data.split('\n')

path = []
sz_dir = defaultdict(int)

for line in read_data:
	entry = line.split(' ')
	print(entry)
	if entry[1] == 'cd':
		if entry[2] == '..':
			path.pop()
		else:
			path.append(entry[2])

	elif entry[1] == 'ls':
		continue
	elif entry[0] == 'dir':
		continue

	else:
		sz = int(entry[0])
		for i in range(1, len(path) + 1):
			sz_dir['/'.join(path[:i])] += sz
			
print(sz_dir)

# Answer Part I

# vld_sz = 0

# for k, v in sz_dir.items():
# 	if v <= 100000:
# 		vld_sz += v

# print(vld_sz)

# Answer Part II

mx_avail = 70000000 - 30000000
mx_used = sz_dir['/']

mx_freed = mx_used - mx_avail

least_sz = float('inf')

for k, v in sz_dir.items():
	if v >= mx_freed:
		least_sz = min(least_sz, v)

print(least_sz)
