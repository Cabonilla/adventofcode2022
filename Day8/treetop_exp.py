fileObj = open('input.txt')
data = fileObj.read()
read_data = data.split('\n')

# print(read_data)

tree_matrix = [[int(i) for i in j] for j in read_data]
print(tree_matrix)

tree_rows = len(tree_matrix)
tree_cols = len(tree_matrix[0])

vis_cnt = 0

# Definition approach, did not work.
def prv_chk(i, j, opt, curr, matrix):
	global vis_cnt
	is_blocked = False
	if opt == "back":
		for ii in range(i - 1, -1, -1):
			if matrix[ii][j] >= curr:
				is_blocked = True
				break
		if not is_blocked:
			vis_cnt += 1
	if opt == 'down':
		for jj in range(j - 1, -1, -1):
			if matrix[i][jj] >= curr:
				is_blocked = True
				break
		if not is_blocked:
			vis_cnt += 1

def nxt_chk(i, j, opt, curr, matrix):
	global vis_cnt
	is_blocked = False
	if opt == 'forw':
		for ii in range(i + 1, tree_rows):
			if matrix[ii][j] >= curr:
				is_blocked = True
				break
		if not is_blocked:
			vis_cnt += 1
	if opt == 'upw':
		for jj in range(j + 1, tree_cols):
			if matrix[i][jj] >= curr:
				is_blocked = True
				break
		if not is_blocked:
			vis_cnt += 1

for r in range(1, tree_rows - 1):
	for c in range(1, tree_cols - 1):
		sngl_tree = tree_matrix[r][c]
		is_blocked = False

		prv_chk(r, c, 'back', sngl_tree, tree_matrix)
		nxt_chk(r, c, 'forw', sngl_tree, tree_matrix)
		prv_chk(r, c, 'down', sngl_tree, tree_matrix)
		nxt_chk(r, c, 'up', sngl_tree, tree_matrix)

print(2 * tree_rows + 2 * tree_cols - 4 + vis_cnt)
print(2 * tree_rows)
print(2 * tree_cols)
print(vis_cnt)
