class EulerProblem2:
   def __init__(self):
       pass

   def generate(self, max_of_terms):
       sequence = [1, 2]
       iter = 0
       while sequence[-1] < max_of_terms:
           next_item = sequence[iter] + sequence[iter + 1]
           sequence.append(next_item)
           iter = iter + 1
       sequence.pop()
       return sequence

   def sum_even_terms(self, max_of_terms):
       sequence = self.generate(max_of_terms)
       sum = 0
       for item in sequence:
           if item % 2 == 0:
               sum = sum + item
       return sum
