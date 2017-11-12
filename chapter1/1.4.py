from collections import defaultdict

TEST_STRINGS = ['Tact Coa', 'Racecar', 'carrace', 'ajddjj', 'dajddaj', 'dajad', 'raccar', 'abcde', 'adddddda']
CORRECT_RESULTS = [True, True, True, False, True, True, True, False, True]


def check_result(result):
    return all([result[i] == CORRECT_RESULTS[i] for i in range(len(result))])



# For a palindrome to be possible, there needs to be
# an equal number of all letters, with the exception of the "center" split,
# which can be related.
def palindrome_permutation(s):
	# Does not seem that spaces matter in this formulation, so strip.
	s = s.replace(' ', '')
	# Also does not seem that capitalization matters
	s = s.lower()
	seen_d = defaultdict(int)
	for c in s:
		if seen_d[c] > 0:
			seen_d[c] -= 1
		else:
			seen_d[c] += 1

	gt_zero_counter = 0
	for c, count in seen_d.items():
		if count > 0:
			gt_zero_counter += 1

	return gt_zero_counter <= 1


if __name__ == '__main__':
	result = [palindrome_permutation(s) for s in TEST_STRINGS]
	assert check_result(result)



