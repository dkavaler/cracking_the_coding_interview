TEST_STRINGS = ['aaaa', 'aaba', 'abcdefa', 'ajdlke', 'elajeda']
CORRECT_RESULTS = [False, False, False, True, False]

# O(N^2)
def is_unique_slow(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True


# O(N^2), O(1) extra space (no data structure)
# ASSUMES ONLY ALPHABETIC CHARACTERS
def is_unique(s):
    flag = 0
    for c in s:
        c_i = ord(c) - ord('a') 
        if (1 << c_i) & flag >= 1:
            return False
        flag |= (1 << c_i)
    return True


# O(N^2)
# Have to check all of seen_c each time
def is_unique_slow_wcounter(s):
    seen_c = []
    for c in s:
        if c in seen_c:
            return False
        seen_c.append(c)
    return True


# O(N)
# Uses a hash table (dict) for O(1) insert / lookup
# O(c) space, where c is the number of characters. If the number of characters
# is fixed (which it is if we're using a standard character set), the space
# can be argued as O(1)
def is_unique_fast_wcounter(s):
    seen_c = {}
    for c in s:
        if c in seen_c:
            return False
        seen_c[c] = True
    return True


def check_result(result):
    return all([result[i] == CORRECT_RESULTS[i] for i in range(len(result))])


if __name__ == '__main__':
    result = [is_unique_slow(s) for s in TEST_STRINGS]
    assert check_result(result)

    result = [is_unique(s) for s in TEST_STRINGS]
    assert check_result(result)


    result = [is_unique_slow_wcounter(s) for s in TEST_STRINGS]
    assert check_result(result)

    result = [is_unique_fast_wcounter(s) for s in TEST_STRINGS]
    assert check_result(result)



