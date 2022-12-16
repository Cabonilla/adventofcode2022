# fileObj = open('example.txt', 'r')
fileObj = open('input.txt', 'r')
data = fileObj.read()
read_data = data.split('\n')

move_dict = {
	"R": [1,0],
	"L": [-1,0],
	"U": [0,-1],
	"D": [0,1]
}

dirs = [i.split() for i in read_data]
origin = (0, 0)
mvmts = set()
mvmts.add(origin)

hx, hy = 0, 0
tx, ty = 0, 0

for dir in dirs:
	d, c = dir[0], int(dir[1])
	cx, cy = move_dict[d]
	for i in range(0, c):
		hx, hy = hx + cx, hy + cy
		if abs(hx - tx) > 1 or abs(hy - ty) > 1:
			if hx - tx == 2:
				tx, ty = hx - 1, hy
			elif hx - tx == -2:
				tx, ty = hx + 1, hy
			elif hy - ty == 2:
				tx, ty = hx, hy - 1
			elif hy - ty == -2:
				tx, ty = hx, hy + 1

			mvmts.add((tx, ty))

print(mvmts)
print(len(mvmts))

# print(dirs)