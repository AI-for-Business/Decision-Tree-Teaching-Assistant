from datetime import datetime
from itertools import chain
from os import path
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
    # TODO: Create rule {int : str} as {index: column_value} (can be multiple in one dictionary for AND rules)
    # TODO: Combine rules to ruleset as [rule], that is an array of dictionaries, each containing
    #  one or multiple entries.
    # Create (rows) amount of lines with random values in each columns (create_tennis_data)
    # Pass each individual line to rules-checker to classify as yes/no (main)
    # Save the classified line to file (create_tennis_data)
    # Close file (create_tennis_data)
    pass


def create_file(data_path: str) -> str:
    # Create file name from current timestamp
    d1: datetime = datetime.now()
    y: str = str(d1.year)
    mo: str = str(d1.month)
    d: str = str(d1.day)
    h: str = str(d1.hour)
    mi: str = str(d1.minute)
    s: str = str(d1.second)

    # File name
    file_name: str = "Data_" + y + "." + mo + "." + d + "-" + h + "." + mi + "." + s + ".csv"

    # Create file
    fn: str = path.join(data_path, file_name)  # Create file handler
    output_file = open(fn, "w")
    output_file.close()

    return fn


def create_columns(amount_of_cols: int) -> list[str]:
    cols: [str] = []
    for i in range(amount_of_cols):
        col_name = "col" + str(i + 1)
        cols.append(col_name)
    return cols


def create_column_values(cols: list[str], values_per_column: int) -> {str: [str]}:
    vals: {str: [str]} = {}
    for col in cols:
        vals_for_col: [str] = []
        for i in range(values_per_column):
            val: str = col + "_val" + str(i+1)
            vals_for_col.append(val)
        vals.update({col: vals_for_col})
    return vals


def create_rules(amount_of_cols: int, values_per_col: int, cols: [str], cols_vals: {str:  [str]}) -> [{str: str}]:
    # parameters
    amount_of_rules: int = int((amount_of_cols * values_per_col) / 2)
    mean = amount_of_cols / 2
    std = mean / 2

    # rule lengths
    rule_lengths = []
    for i in range(amount_of_cols+1):
        rule_lengths.append(0)
    for i in range(amount_of_rules):
        rule_length = round(r.normal(mean, std))
        if rule_length < 1:
            rule_length = 1
        if rule_length > amount_of_cols:
            rule_length = amount_of_cols
        rule_lengths[rule_length] += 1

    rules = [[]]
    for i in range(1, amount_of_cols+1):
        rules.append([])
        for j in range(rule_lengths[i]):
            curr_rule = {}
            while len(curr_rule) < i:
                random_col = cols[r.randint(0, amount_of_cols)]
                while random_col in curr_rule:
                    random_col = cols[r.randint(0, amount_of_cols)]
                random_val = r.choice(cols_vals[random_col])
                curr_rule.update({random_col: random_val})
                unique_rule = True
                curr_rule_items = curr_rule.items()
                for k in range(1, len(curr_rule)+1):
                    for rule in rules[k]:
                        if rule.items() <= curr_rule_items:
                            curr_rule = {}
                            unique_rule = False
                            break
                    if not unique_rule:
                        break
            rules[i].append(curr_rule)
    return list(chain.from_iterable(rules))


def create_rows(number_of_rows: int, cols: [str], cols_vals: {str: [str]}) -> [[]]:
    rows = [cols]
    for i in range(number_of_rows):
        row = []
        for col in cols:
            val = r.choice(cols_vals[col])
            row.append(val)
        rows.append(row)
    return rows

def classify_rows(rows: [[]], rules: [{str: str}]) -> [[]]:
    rows[0].append("Yes/No")
    for i in range(1, len(rows)):
        for rule in rules:
            if set(rule.values()) <= set(rows[i]):
                rows[i].append("Yes")
                break
        if len(rows[i]) == (len(rows[0]) - 1):
            rows[i].append("No")
    return rows


def save_file(fn: str, rows: [[]]) -> None:
    output_file = open(fn, "w")
    for row in rows:
        for i in range(len(row)-1):
            output_file.write(row[i] + ";")
        output_file.write(row[len(row)-1] + "\n")
    output_file.close()


# # Main Method
# if __name__ == '__main__':
#     # Todo: Delete this
#     # generate_random_ruleset(6, 50, 5)  # columns, rows, values_per_columnxc
#
#     test_dict = {
#         0: "medium",
#         1: "rainy",
#         2: "test"
#     }
#     dict2 = {
#         2: "sunny"
#     }
#     rules = [test_dict, dict2]
#
#     line_1 = ["medium", "sunny", "test"]
#     line_2 = ["high", "sunny"]
#
#     for r in rules:
#         classification = True
#         for k, v in r.items():
#             print(k, v)
#
#             if classification:
#                 if str(line_1[k]) == v:
#                     pass
#                 else:
#                     classification = False
#         print(classification)


file_path = create_file("")
columns = create_columns(10)
vals_columns = create_column_values(columns, 10)
created_rules = create_rules(10, 10, columns, vals_columns)
created_rows = create_rows(100, columns, vals_columns)
classified_rows = classify_rows(created_rows, created_rules)
save_file(file_path, classified_rows)
