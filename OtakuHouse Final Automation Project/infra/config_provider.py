import json


class ConfigProvider:
    @staticmethod
    def load_config_json():
        try:
            with open(
                    'C:\\Users\\majdh\\OneDrive\\שולחן העבודה\\Otaku-House-Final-Project\\OtakuHouse Final Automation Project\\config.json',
                    'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File not found. Starting with an empty library.")

    @staticmethod
    def load_secret_json():
        try:
            with open(
                    'C:\\Users\\majdh\\OneDrive\\שולחן העבודה\\Otaku-House-Final-Project\\OtakuHouse Final Automation Project\\secert.json',
                    'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File not found. Starting with an empty library.")
