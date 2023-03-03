from datetime import datetime
from itertools import chain
from os import path
from numpy import random as r


def create_data(columns: int, values: int, rows: int, data_path: str) -> None:
    """
    This method gets called from the GUI, receives all user input, and starts to create synthetic data.
    Nothing happens when invalid arguments are given.
    :param columns: Amount of columns to be created
    :param values: Amount of different values in each column
    :param rows: Amount of rows/lines to be randomly created
    :param data_path: Output path, where the file is to be stored
    :return: None
    """

    # invalid parameters
    if columns <= 0 or values <= 0 or rows <= 0 or data_path == "":
        return

    file_path = create_file(data_path)
    cols = create_columns(columns)
    vals_columns = create_column_values(cols, values)
    rules = create_rules(cols, vals_columns)
    created_rows = create_rows(rows, cols, vals_columns)
    classified_rows = classify_rows(created_rows, rules)
    save_file(file_path, classified_rows)


# Creates an empty csv file. Returns the file path.
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


# Creates the columns.
def create_columns(amount_of_cols: int) -> list[str]:
    cols: [str] = []
    for i in range(amount_of_cols):
        col_name = "col" + str(i + 1)
        cols.append(col_name)
    return cols


# Creates the values for each column.
def create_column_values(cols: list[str], values_per_column: int) -> {str: [str]}:
    vals: {str: [str]} = {}
    for col in cols:
        vals_for_col: [str] = []
        for i in range(values_per_column):
            val: str = col + "_val" + str(i+1)
            vals_for_col.append(val)
        vals.update({col: vals_for_col})
    return vals


# Creates the rules based on which the data will be classified.
def create_rules(cols: [str], cols_vals: {str:  [str]}) -> [{str: str}]:
    values_per_col = len(cols_vals[cols[0]])

    # parameters
    amount_of_rules: int = int((len(cols) * values_per_col) / 2)
    mean = len(cols) / 2
    std = mean / 2

    # amount of rules for every rule length
    rule_lengths = []
    for i in range(len(cols)+1):
        rule_lengths.append(0)
    for i in range(amount_of_rules):
        rule_length = round(r.normal(mean, std))
        if rule_length < 1:
            rule_length = 1
        if rule_length > len(cols):
            rule_length = len(cols)
        rule_lengths[rule_length] += 1

    # create the rules
    rules = [[]]
    for i in range(1, len(cols)+1):
        rules.append([])
        for j in range(rule_lengths[i]):
            curr_rule = {}
            while len(curr_rule) < i:
                random_col = cols[r.randint(0, len(cols))]
                while random_col in curr_rule:
                    random_col = cols[r.randint(0, len(cols))]
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


# Create the rows without the target attribute.
def create_rows(number_of_rows: int, cols: [str], cols_vals: {str: [str]}) -> [[]]:
    rows = [cols]
    for i in range(number_of_rows):
        row = []
        for col in cols:
            val = r.choice(cols_vals[col])
            row.append(val)
        rows.append(row)
    return rows


# Create the rows with the target attribute.
def classify_rows(rows: [[]], rules: [{str: str}]) -> [[]]:
    rows[0].append("classification")
    for i in range(1, len(rows)):
        for rule in rules:
            if set(rule.values()) <= set(rows[i]):
                rows[i].append("Yes")
                break
        if len(rows[i]) == (len(rows[0]) - 1):
            rows[i].append("No")
    return rows


# Save the rows.
def save_file(fn: str, rows: [[]]) -> None:
    output_file = open(fn, "w")
    for row in rows:
        for i in range(len(row)-1):
            output_file.write(row[i] + ";")
        output_file.write(row[len(row)-1] + "\n")
    output_file.close()
