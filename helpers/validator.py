import os
from helpers.logger import Logger

class Validator:

    @staticmethod
    def check_valid_file_path(file_path):
        if file_path[0] == '/':
            message = f"ERROR: The file path '{file_path}' can not start with a forward slash."
            print(message)
            Logger.error(message)
            exit()

        if not os.path.exists(file_path):
            message = f"ERROR: The file at path '{file_path}' does not exist."
            print(message)
            Logger.error(message)
            exit()


    @staticmethod
    def check_file_is_csv(file_path):
        if not file_path.endswith('.csv'):
            print("ERROR: Invalid file format. Please provide a CSV file.")
            Logger.error("ERROR: Invalid file format. Please provide a CSV file.")
            exit()
