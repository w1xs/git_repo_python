import pytest
def count_repeated_chars(s):
    if not isinstance(s, str):
        raise ValueError("Входной параметр должен быть строкой")

    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    res = 0
    for count in char_counts.values():
        if count > 1:
            res += 1

    return res

def test_count_repeated_chars():
    assert count_repeated_chars("") == 0
    assert count_repeated_chars("a") == 0
    assert count_repeated_chars("abc") == 0
    assert count_repeated_chars("aab") == 1
    assert count_repeated_chars("aabb") == 2
    assert count_repeated_chars("abab") == 2
    assert count_repeated_chars("abcabc") == 3
    assert count_repeated_chars("aaa") == 1
    assert count_repeated_chars("aabbccddeeff") == 6

def test_count_repeated_chars_non_string():
    with pytest.raises(ValueError):
        count_repeated_chars(123)
    with pytest.raises(ValueError):
        count_repeated_chars([1, 2, 2, 3])
    with pytest.raises(ValueError):
        count_repeated_chars({"a", "b", "c"})