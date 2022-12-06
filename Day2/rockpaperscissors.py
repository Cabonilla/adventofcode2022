# fileObj = open('example.txt', 'r')
fileObj = open('input.txt', 'r')
data = fileObj.read()
read_data = data.split('\n')
# Value split, forgot I added it. Replaced w/ `m = i.split()`.
# read_arr = [i.split() for i in read_data]

# play_dict_opponent = {
# 	"A": "Rock",
# 	"B": "Paper",
# 	"C": "Scissors"
# }

# play_dict_player = {
# 	"X": "Rock",
# 	"Y": "Paper",
# 	"Z": "Scissors"
# }

score_dict_opponent = {
	"A": 1,
	"B": 2,
	"C": 3
}

score_dict_player = {
	"X": 1,
	"Y": 2,
	"Z": 3
}

outcome_dict = {
	"L": 0,
	"D": 3, 
	"W": 6
}

# Round Score = score_dict + outcome_dict

# Strategy Part I
example_strat = {
	"A": "Y", # Part 1: W | Part 2: D
	"B": "X", # Part 1: L | Part 2: L
	"C": "Z"  # Part 1: D | Part 2: W
}

# Answer Part I

# final_score = 0

# for i in read_data:
# 	m = i.split()
# 	o_m, p_m = score_dict_opponent[m[0]], score_dict_player[m[1]]
# 	final_score += p_m
# 	if p_m - o_m == 1 or (p_m == 1 and o_m == 3):
# 		final_score += outcome_dict["W"]
# 	elif p_m == o_m:
# 		final_score += outcome_dict["D"]
	
# print(final_score)

# Answer Part II

meta_strat = {
	"X": "L",
	"Y": "D",
	"Z": "W"
}

final_score = 0

for i in read_data:
	m = i.split()
	o_m, m_o = score_dict_opponent[m[0]], meta_strat[m[1]]
	final_score += outcome_dict[m_o]
	if outcome_dict[m_o] == outcome_dict["D"]:
		final_score += o_m
	elif outcome_dict[m_o] == outcome_dict["W"]:
		if o_m == 3:
			final_score += 1
		else:
			final_score += o_m + 1
	elif outcome_dict[m_o] == outcome_dict["L"]:
		if o_m == 1:
			final_score += 3
		else:
			final_score += o_m - 1
	
print(final_score)