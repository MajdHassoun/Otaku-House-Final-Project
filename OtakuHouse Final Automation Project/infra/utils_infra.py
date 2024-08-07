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
        return random.randint(18, 25)

    @staticmethod
    def from_item_num_to_home_page_num(number):
        return number - 18

    # @staticmethod
    # def get_random_big_number():
    #     return random.randint(1000, 2000)

    # @staticmethod
    # def get_random_number_second_home_page():
    #     return random.randint(10, 17)

    @staticmethod
    def generate_random_string(length: int) -> str:
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
