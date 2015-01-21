class EulerProblem4:
    def __init__(self):
        pass

    def is_palindrome(self, number):
        return str(number) == str(number)[::-1]

    def product_palindromes(self, max_first, max_second):
        max_palindrome = 0
        products = []
        for i in range(0, max_first + 1):
            for j in range(0, max_second + 1):
                product = i*j
                if self.is_palindrome(product) and product >= max_palindrome:
                    max_palindrome = product
        return max_palindrome


