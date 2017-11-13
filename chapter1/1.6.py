TEST_STRINGS = ['aabbccdd', 'abcdefg', 'abbcddeef',
			    'aaaaaaaabcdeeeeeef', 'aabcccccaaa']
CORRECT_RESULTS = ['aabbccdd', 'abcdefg', 'abbcddeef',
                   'a8b1c1d1e6f1', 'a2b1c5a3']


def check_result(result):
    return all([result[i] == CORRECT_RESULTS[i] for i in range(len(result))])


# Should be O(N) since the appends are amortized O(1) and join is O(N)
def string_compress(s):
	s_build_l = []
	cur_c, counter = s[0], 0
	for c in s:
		if c != cur_c:
			s_build_l.append(cur_c)
			s_build_l.append(str(counter))
			counter = 0

		counter += 1
		cur_c = c

	s_build_l.append(cur_c)
	s_build_l.append(str(counter))

	news = ''.join(s_build_l)

	if len(news) >= len(s):
		return s

	return news


if __name__ == '__main__':
	result = [string_compress(s) for s in TEST_STRINGS]
	print(result)
	assert check_result(result)