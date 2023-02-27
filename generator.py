from os import path
from datetime import datetime
from numpy import random as r


def create_tennis_data(self):
    """
    This method was just for testing.
    :param self:
    :return:
    """
    save_path: str = "C:/Users/Yorck Zisgen/Downloads"  # Get file path from user input via configuration manager

    # Create file name from current timestamp
    d1: datetime = datetime.now()
    y: str = str(d1.year)
    mo: str = self.convert(d1.month)
    d: str = self.convert(d1.day)
    h: str = self.convert(d1.hour)
    mi: str = self.convert(d1.minute)
    s: str = self.convert(d1.second)

    # File name
    file_name: str = "Data_" + y + "." + mo + "." + d + "-" + h + "." + mi + "." + s + ".csv"

    # Creating file names for valid and noisy sensor logs and trace log
    fn: str = path.join(save_path, file_name)  # Create file handler
    self.output_file = open(fn, "w")

    outlook = ["Sunny", "Overcast", "Rainy"]
    temp = ["Hot", "Mild", "Cool"]
    humidity = ["High", "Normal"]
    windy = ["True", "False"]
    s: str = "Outlook;Temp;Humidity;Windy;Play;\n"
    self.output_file.write(s)

    for i in range(30):
        o = outlook[r.randint(0, len(outlook))]
        t = temp[r.randint(0, len(temp))]
        h = humidity[r.randint(0, len(humidity))]
        w = windy[r.randint(0, len(windy))]

        if o == "Overcast":
            p = "Yes"
        elif o == "Rainy" and w == "False":
            p = "Yes"
        elif o == "Sunny" and h == "Normal":
            p = "Yes"
        else:
            p = "No"

        # p = self.tree1(o, t, h, w)

        s: str = o + ";" + t + ";" + h + ";" + w + ";" + p + "\n"
        self.output_file.write(s)

    self.output_file.close()
    self.set_input_file(self.output_file.name)


def generate_random_ruleset(columns: int, rows: int, values_per_column: int):
    """
    This method was just for testing.
    :param columns:
    :param rows:
    :param values_per_column:
    :return:
    """
    # Step 1: Generate columns and value expressions
    # Step 2: Generate decision rules from step 1
    # Step 3: Randomize value expressions and calculate results from step 2

    cols = []  # List of all column headers
    col2val = {}  # Dictionary of column header -> list of different values in that column

    for i in range(columns):
        key = "col_" + str(i+1)
        cols.append(key)
        col2val.update({key: "[]"})
    # print(cols)

    for idx, c in enumerate(cols):
        val_list = []
        for i in range(values_per_column):
            val_list.append(str(c) + '-' + str(i+1))
        # print(val_list)
        col2val.update({c: val_list})
    # print(col2val)


def create_data(columns: int, values: int, rows: int, data_path: str, cb: int) -> None:
    """
    This method gets called from the GUI, receives all user input, and starts to create synthetic data.
    :param columns: Amount of columns to be created
    :param values: Amount of different values in each column
    :param rows: Amount of rows/lines to be randomly created
    :param data_path: Output path, where the file is to be stored
    :param cb: Checkbox. Integer 0/1. Denominates whether the output directory shall be opened in Explorer after file
    has been created
    :return: None
    """

    # LEGEND: Step description -> return type (where can the code snippet be found)
    # Create file (create_tennis_data)
    # Create column headers -> [str] (generate_random_ruleset)
    # Create list of values in each column -> [[value]] & {str:[value]} (generate_random_ruleset)
    # TODO: Define how many rules we need
    # TODO: Create rule {int : str} as {index: column_value} (can be multiple in one dictionary) for AND rules
    # TODO: Combine rules to ruleset as [rule], that is an array of dictionaries, each containing
    #  one or multiple entries.
    # Create (rows) amount of lines with random values in each columns (create_tennis_data)
    # Pass each individual line to rules-checker to classify as yes/no (main)
    # Save the classified line to file (create_tennis_data)
    # Close file (create_tennis_data)
    pass


def create_file(data_path: str) -> None:
    pass


def create_columns(columns: int) -> list[str]:
    pass


def create_column_values(cols: list[str], values_per_column: int) -> list[list[str]]:
    pass


def close_file(data_path: str, cb: int) -> None:
    pass


# Main Method
if __name__ == '__main__':
    # Todo: Delete this
    # generate_random_ruleset(6, 50, 5)  # columns, rows, values_per_column

    test_dict = {
        0: "medium",
        1: "rainy",
        2: "test"
    }
    dict2 = {
        2: "sunny"
    }
    rules = [test_dict, dict2]

    line_1 = ["medium", "sunny", "test"]
    line_2 = ["high", "sunny"]

    for r in rules:
        classification = True
        for k, v in r.items():
            # print(k, v)
            if classification:
                if str(line_1[k]) == v:
                    pass
                else:
                    classification = False
        print(classification)
