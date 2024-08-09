import random
import string


class UtilsInfra:

    @staticmethod
    def pick_random_number_one_to_ten():
        return random.randint(0, 9)

    @staticmethod
    def pick_random_number_one_to_five():
        return random.randint(0, 4)

    @staticmethod
    def pick_random_number_one_to_eight():
        return random.randint(0, 7)

    @staticmethod
    def pick_random_number_url():
        return random.randint(19, 26)

    @staticmethod
    def from_item_num_to_home_page_num(number):
        return 27 - number
    # 26=1 , 25=2, 24=3, 23=4, 22=5, 21=6, 20=7, 19=8

    @staticmethod
    def generate_random_string(length: int) -> str:
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
