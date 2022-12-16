# fileObj = open('example.txt')
fileObj = open('input.txt')
data = fileObj.read()
read_data = data.split('\n')

# print(read_data)

tree_matrix = [[int(i) for i in j] for j in read_data]
print(tree_matrix)

tree_rows = len(tree_matrix)
tree_cols = len(tree_matrix[0])

# Answer Part I

# vis_cnt = 0

# for r in range(1, tree_rows - 1):
# 	for c in range(1, tree_cols - 1):
# 		sngl_tree = tree_matrix[r][c]
# 		is_blocked = False
# 		for ii in range(r - 1, -1, -1):
# 			if tree_matrix[ii][c] >= sngl_tree:
# 				is_blocked = True
# 				break
# 		if not is_blocked:
# 			vis_cnt += 1
# 			continue
# 		is_blocked = False
# 		for ii in range(r + 1, tree_rows):
# 			if tree_matrix[ii][c] >= sngl_tree:
# 				is_blocked = True
# 				break
# 		if not is_blocked:
# 			vis_cnt += 1
# 			continue
# 		is_blocked = False
# 		for jj in range(c - 1, -1, -1):
# 			if tree_matrix[r][jj] >= sngl_tree:
# 				is_blocked = True
# 				break
# 		if not is_blocked:
# 			vis_cnt += 1
# 			continue
# 		is_blocked = False
# 		for jj in range(c + 1, tree_cols):
# 			if tree_matrix[r][jj] >= sngl_tree:
# 				is_blocked = True
# 				break
# 		if not is_blocked:
# 			vis_cnt += 1
# 			continue

# Answer Part II

scen_cnt = 0

for r in range(tree_rows):
	for c in range(tree_cols):
		sngl_tree = tree_matrix[r][c]
		scen_prev = scen_forw = scen_down = scen_up = 0
		for ii in range(r - 1, -1, -1):
			scen_prev += 1
			if tree_matrix[ii][c] >= sngl_tree:
				break
		if scen_prev <= 1:
			scen_prev = 1
		for ii in range(r + 1, tree_rows):
			scen_forw += 1
			if tree_matrix[ii][c] >= sngl_tree:
				break
		if scen_forw <= 1:
			scen_forw = 1
		for jj in range(c - 1, -1, -1):
			scen_down += 1
			if tree_matrix[r][jj] >= sngl_tree:
				break
		if scen_down <= 1:
			scen_down = 1
		for jj in range(c + 1, tree_cols):
			scen_up += 1
			if tree_matrix[r][jj] >= sngl_tree:
				break
		if scen_up <= 1:
			scen_up = 1

		scen_cnt = max(scen_cnt, scen_prev * scen_forw * scen_down * scen_up)

print(scen_cnt)

		
