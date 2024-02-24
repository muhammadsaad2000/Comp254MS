def is_palindrome(s):
    # Base case: an empty string or a string with a single character is a palindrome
    if len(s) <= 1:
        return True
    # Check if the first and last characters are equal
    if s[0] == s[-1]:
        # Recur with the substring excluding the first and last characters
        return is_palindrome(s[1:-1])
    else:
        return False

# Test the method
user_input = input("Enter a string to check if it's a palindrome: ")
result = is_palindrome(user_input)

if result:
    print(f"{user_input} is a palindrome!")
else:
    print(f"{user_input} is not a palindrome.")
