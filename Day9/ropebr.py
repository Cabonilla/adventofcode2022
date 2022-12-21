# fileObj = open('example.txt', 'r')
fileObj = open('larger_example.txt', 'r')
# fileObj = open('input.txt', 'r')
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

# Answer Part I

# hx, hy = 0, 0
# tx, ty = 0, 0

# for dir in dirs:
# 	d, c = dir[0], int(dir[1])
# 	cx, cy = move_dict[d]
# 	for i in range(0, c):
# 		hx, hy = hx + cx, hy + cy
# 		if abs(hx - tx) > 1 or abs(hy - ty) > 1:
# 			if hx - tx == 2:
# 				tx, ty = hx - 1, hy
# 			elif hx - tx == -2:
# 				tx, ty = hx + 1, hy
# 			elif hy - ty == 2:
# 				tx, ty = hx, hy - 1
# 			elif hy - ty == -2:
# 				tx, ty = hx, hy + 1

# 			mvmts.add((tx, ty))

# print(mvmts)
# print(len(mvmts))

# print(dirs)

# Answer Part II

knot_arr = [[0,0]]

for i in range(9):
	knot_arr.append([0,0])

print(knot_arr)
for dir in dirs:
	d, c = dir[0], int(dir[1])
	cx, cy = move_dict[d]
	for i in range(0, c):
		knot_arr[0][0], knot_arr[0][1] = knot_arr[0][0] + cx, knot_arr[0][1] + cy
		# print(knot_arr[0][0])
		for j in range(9):
			mve = False
			hx, hy = knot_arr[j][0], knot_arr[j][1]
			tx, ty = knot_arr[j + 1][0], knot_arr[j + 1][1]
			abs_x = abs(hx - tx)
			abs_y = abs(hy - ty)
			if abs_x <= 1 and abs_y <= 1:
				pass
			elif abs_x == 2 and abs_y == 2:
				mve = True
				tx, ty = (hx + tx) // 2, (hy + ty) // 2
				knot_arr[j + 1][0], knot_arr[j + 1][1] = tx, ty
			else:
				mve = True
				if hx - tx == 2:
					tx, ty = hx - 1, hy
				elif hx - tx == -2:
					tx, ty = hx + 1, hy
				elif hy - ty == 2:
					tx, ty = hx, hy - 1
				elif hy - ty == -2:
					tx, ty = hx, hy + 1
				knot_arr[j + 1][0], knot_arr[j + 1][1] = tx, ty
			if not mve:
				break
		mvmts.add((knot_arr[-1][0], knot_arr[-1][1]))

print(len(mvmts))

