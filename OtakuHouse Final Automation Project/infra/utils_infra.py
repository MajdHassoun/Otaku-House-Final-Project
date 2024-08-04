import random


class UtileInfra:

    @staticmethod
    def pick_random_number_one_to_ten():
        return random.randint(1, 10)

    @staticmethod
    def pick_random_number_one_to_five():
        return random.randint(1, 5)

    @staticmethod
    def pick_random_number_one_to_eight():
        return random.randint(1, 8)
