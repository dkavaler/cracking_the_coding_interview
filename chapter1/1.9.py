TEST_INPUT = [('waterbottle', 'erbottlewat'),
              ('cat', 'atc'),
              ('dog', 'ogd'),
              ('racecar', 'cecarra'),
              ('asdf', 'hjkl')]

CORRECT_RESULT = [True, True, True, True, False]


def check_result(result):
    return all([result[i] == CORRECT_RESULT[i] for i in range(len(result))])


# Python "in" is a substring check
def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    return s2 in s1 + s1
    

if __name__ == '__main__':
    result = [string_rotation(s1, s2) for s1, s2 in TEST_INPUT]
    assert check_result(result)
