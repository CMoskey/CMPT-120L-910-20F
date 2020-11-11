def prime_or_composite(number):

    from math import sqrt
    from itertools import count, islice
    
    
    if number < 2:
        return "neither"

    for i in islice(count(2), int(sqrt(number) - 1)):
        if number % i == 0:
            return "composite"

    return "prime"

if __name__ == "__main__":
    numbers = [-7, 1, 2, 10, 31, 47, 89, 101, 103, 97, 187, 981, 19201, 47055833459]


    answers = []
    for number in numbers:
        answers.append(prime_or_composite(number))
    
    print(answers)