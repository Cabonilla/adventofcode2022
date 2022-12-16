fileObj = open('example.txt', 'r')
data = fileObj.read()
read_data = data.split('\n')

# print(read_data)

# move_dict = {
# 	"R": col + 1,
# 	"L": col - 1,
# 	"U": row + 1,
# 	"D": row - 1
# }

seen = []

dirs = [i.split() for i in read_data]
origin = [0, 0]
mvmts = [origin]

for dir in dirs:
	print(dir)
	place = origin
	d, c = dir[0], int(dir[1])
	if d == 'R':
		# origin[0] += int(dir[1])
		for i in range(0, c):
			place[0] += 1
			mvmts += place
			print(place)
	if d == 'L':
		# origin[0] += int(dir[1])
		for i in range(0, c):
			place[0] -= 1
			mvmts += place
			print(place)
	if d == 'U':
		# origin[0] += int(dir[1])
		for i in range(0, c):
			place[1] += 1
			mvmts += place
			print(place)
	if d == 'D':
		# origin[0] += int(dir[1])
		for i in range(0, c):
			place[1] -= 1
			mvmts += place
			print(place)

print(mvmts)
# print(dirs)