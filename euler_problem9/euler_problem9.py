class EulerProblem9:
    def __init__(self):
        pass

    def find_triplet(self):
        for a in range(0, 500):
            for b in range(a, 500):
                for c in range(b, 500):
                    if a+b+c == 1000:
                        if a*a+b*b == c*c:
                            print a,b,c

if __name__ == "__main__":
    e = EulerProblem9()
    e.find_triplet()
