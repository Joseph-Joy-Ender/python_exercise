def is_palindrome(number):
    reverse = 0
    temporary = number
    remainder = 0
    while temporary > 0:
        remainder = temporary % 10
        reverse = reverse * 10 + remainder
        temporary /= 10
        if reverse == number:
            return True
        else:
            return False


print(is_palindrome(101))
