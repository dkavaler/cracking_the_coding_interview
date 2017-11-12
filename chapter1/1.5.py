TEST_STRINGS = [('pale,', 'ple'), ('pale', 'pale'), ('pales,', 'pale'),
				('pale,', 'bale'), ('pale,', 'bake'), ('pael ', 'ajsd'),
                ('asdf', 'adsf'), ('alksdjflkasjdf', 'f'), ('pale', 'pael'),
                ('sapl', 'apl')]
CORRECT_RESULTS = [True, True, True,
				   True, False, False,
                   False, False, False,
                   True]


def check_result(result):
    return all([result[i] == CORRECT_RESULTS[i] for i in range(len(result))])



# Ignore all non-alphabetic characters (strip others).
# This is O(a + b) (where a is len(s1) and b is len(s2))
def one_away(s1, s2):
    # Get rid of non-alphabetic characters
    s1 = ''.join([c for c in s1 if c.isalpha()])
    s2 = ''.join([c for c in s2 if c.isalpha()])

    if abs(len(s1) - len(s2)) > 1:
        return False

    decision = False

    # Three cases: insert, remove, replace
    # Insert / remove case - insert on one side is the same as removal on other,
    # so only need logic for single case, with a swap:
    if len(s1) > len(s2):
        decision = handle_oneoff(s1, s2)
    elif len(s1) < len(s2):
        decision = handle_oneoff(s2, s1)
    # Lengths are equal, so it must be a replace
    else:
        decision = handle_replace(s1, s2)

    return decision


# len(s1) > len(s2)
def handle_oneoff(s1, s2):
    inserts_required = 0
    s1_l, s2_l = [], []
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            i += 1
        else:
            s1_l.append(s1[i])
            s2_l.append(s2[j])
            i += 1
            j += 1

    return ''.join(s1_l) == ''.join(s2_l)


def handle_replace(s1, s2):
    replace_count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            replace_count += 1

    return replace_count <= 1



if __name__ == '__main__':
    result = [one_away(s1, s2) for s1, s2 in TEST_STRINGS]
    assert check_result(result)

