class EulerProblem3:
    def __init__(self):
        pass

    def factorize(self, number):
        prime_factors = []
        factor = 2
        while factor*factor <= number:
            while (number % factor) == 0:
                prime_factors.append(factor)
                number = number / factor
            factor = factor + 1
        if number > 1:
            prime_factors.append(number)
        return prime_factors

    def largest_factor(self,number):
        factors = self.factorize(number)
        return factors[-1]
