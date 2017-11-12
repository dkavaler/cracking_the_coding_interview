TEST_STRINGS = ['Mr John Smith', 'Test String Please Ignore']
CORRECT_RESULTS = ['Mr%20John%20Smith', 'Test%20String%20Please%20Ignore']


def check_result(result):
    return all([result[i] == CORRECT_RESULTS[i] for i in range(len(result))])


# A little hard to replicate the point of this in Python.
# The point is that copying strings using concatenation (+) can be slow depending
# on the implementation. In Python, like Java, the concatenation will be polynomial
# time (order ~ 2) due to copying of characters for each concatenation.
# The other point is the limited string size. In Python, strings can be appended
# to without (really) worrying about size.
# This is polynomial (order ~ 2)
def URLify(s):
	news = ''
	for c in s:
		if c == ' ':
			news += '%20'
		else:
			news += c

	return news


# This should be O(N).
def URLify_fast(s):
	# O(N) operation
	s_split = s.split(' ')
	# Also O(N) operation

	return '%20'.join(s_split)


if __name__ == '__main__':
	result = [URLify(s) for s in TEST_STRINGS]
	assert check_result(result)

	result = [URLify_fast(s) for s in TEST_STRINGS]
	assert check_result(result)



