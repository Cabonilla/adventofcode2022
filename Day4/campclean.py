fileObj = open('input.txt', 'r')
# fileObj = open('example.txt', 'r')
data = fileObj.read()
read_data = data.split('\n')

range_list = []

for i in read_data:
	prs = i.split(',')
	frst = prs[0].split('-')
	scnd = prs[1].split('-')

	frst_rng = [j for j in range(int(frst[0]), int(frst[1]) + 1)]
	scnd_rng = [k for k in range(int(scnd[0]), int(scnd[1]) + 1)]

	if len(frst_rng) > len(scnd_rng) or len(frst_rng) < len(scnd_rng):
		sub_lst = min(frst_rng, scnd_rng, key=len)
		big_lst = max(frst_rng, scnd_rng, key=len)
	else:
		sub_lst = min(frst_rng, scnd_rng)
		big_lst = max(frst_rng, scnd_rng)

	range_list.append([sub_lst, big_lst])

# Answer Part I

# enclosed_tally = 0

# for sub, big in range_list:
# 	if sub[0] in big and sub[-1] in big:
# 		enclosed_tally += 1

# print(enclosed_tally)

# Answer Part I Version 2

# enclosed_tally = 0

# for sub, big in range_list:
# 	sub_first = sub[0]
# 	sub_last = sub[-1]

# 	big_first = big[0]
# 	big_last = big[-1]

# 	if sub_first >= big_first and sub_last <= big_last:
# 		enclosed_tally += 1

# print(enclosed_tally)

# Answer Part II

overlap_tally = 0

for sub, big in range_list:
	sub_first = sub[0]
	sub_last = sub[-1]

	big_first = big[0]
	big_last = big[-1]

	if sub_first <= big_first and sub_last >= big_last or sub_first >= big_first and sub_last <= big_last:
		overlap_tally += 1
	elif big_first <= sub_first <= big_last or sub_first <= big_first <= sub_last:
		overlap_tally += 1
	
print(overlap_tally)