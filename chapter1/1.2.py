from collections import defaultdict

TEST_STRINGS = [('kjjkll', 'kkjjll'), ('dkaj', 'jkad',),
				('abcde', 'edcba'), ('eeaee', 'aaeaa'),
                ('defg', 'gfde'), ('akjd', 'buif')]
CORRECT_RESULTS = [True, True, True, False, True, False]


# O(len(string1) + len(string2)) using hash table
def is_permutation(string1, string2):
    if len(string1) != len(string2):
        return False

    seen_d = defaultdict(int)
    for c in string1:
        seen_d[c] += 1

    for c in string2:
        seen_d[c] -= 1

    for c, count in seen_d.items():
        if count != 0:
            return False

    return True


def check_result(result):
    return all([result[i] == CORRECT_RESULTS[i] for i in range(len(result))])


if __name__ == '__main__':
    result = [is_permutation(s1, s2) for s1, s2 in TEST_STRINGS]
    assert check_result(result)