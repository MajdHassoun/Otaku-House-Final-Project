import random
import string


class UtileInfra:

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
    def pick_random_number_review_url():
        return random.randint(18, 25)

    @staticmethod
    def from_item_num_to_home_page_num(number):
        return number - 18

    @staticmethod
    def generate_random_string(length: int) -> str:
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))
