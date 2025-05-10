import pytest
def is_palindrome(s):
    if not isinstance(s, str):
        raise ValueError("Входной параметр должен быть строкой")
    if len(s) < 3:
        raise ValueError("Строка должна содержать минимум 3 символа")
    return s == s[::-1]

def test_palindrome_valid():
    assert is_palindrome("aba") == True
    assert is_palindrome("abba") == True
    assert is_palindrome("abcba") == True
    assert is_palindrome("AbBa") == False
    assert is_palindrome("abc") == False
    assert is_palindrome("abca") == False

def test_palindrome_short_string():
    with pytest.raises(ValueError):
        is_palindrome("")
    with pytest.raises(ValueError):
        is_palindrome("a")
    with pytest.raises(ValueError):
        is_palindrome("aa")

def test_palindrome_non_string():
    with pytest.raises(ValueError):
        is_palindrome(123)
    with pytest.raises(ValueError):
        is_palindrome([1, 2, 3, 2, 1])
    with pytest.raises(ValueError):
        is_palindrome({"a", "b", "c"})