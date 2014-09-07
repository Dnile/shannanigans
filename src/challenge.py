__author__ = 'danielby'
from random import randrange

class Challange:

    def __init__(self):
        self.numbers = list()
        self.random_vals = dict()

    def do_things(self):

        randomized = 0
        rand_count = 0

        for i in range(0,99+1):
            randomized = randrange(1,99+1)
            while self.random_vals.has_key(randomized):

                randomized = randrange(0, 100)
                rand_count += 1

            self.random_vals[randomized] = True
            self.numbers.append(randomized)


        self.numbers.pop(randomized - 1)
        print len(self.numbers)
        print rand_count

    def find_missing_number(self):

        """
        as the sum of all natural numbers from 1 to N can be expressed as Nx(N+1)/2,
        we can subtract the sum of the array from Nx(N+1)/2, and this is how we get our missing number.
        """""
        sum = 0

        arr_length = len(self.numbers)


        for i in range (0, arr_length):
            sum += self.numbers[i]

        total = (arr_length + 1) * arr_length / 2

        missing_num = total - sum

        print missing_num



# the total sum of numbers between 1 and arr.length.



etgar = Challange()

etgar.do_things()

etgar.find_missing_number()





