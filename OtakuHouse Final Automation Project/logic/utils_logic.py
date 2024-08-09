import time


class UtilsLogic:

    @staticmethod
    def split_url_return_item_id(driver_current_url):
        split_url = driver_current_url.split("product/")
        item_url_id = split_url[1]
        return item_url_id
