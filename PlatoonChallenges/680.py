## Given a string s, return true if the s can be palindrome after deleting at most one character from it.

def validPalindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # Check by removing either left or right character
            skip_left = s[left + 1:right + 1]
            skip_right = s[left:right]
            return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
        left += 1
        right -= 1
    
    return True  # Return True if the loop completes without finding a mismatch

print(validPalindrome("abca"))