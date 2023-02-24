from os import path
from datetime import datetime
from numpy import random as r


def create_tennis_data(self):
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


# Main Method
if __name__ == '__main__':
    # Todo: Delete this
    # generate_random_ruleset(6, 50, 5)  # columns, rows, values_per_column

    # Werte -> Regeln -> Ergebnisse -> Zeilen
    # [cols]
    # { col: [values] }

    test_dict = {
        0: "medium",
        1: "rainy",
        2: "test"
        # 0: [1, 2, 3],
        # 1: ["Alpha", "Beta", "Gamma"],
        # 2: 0.15,
        # 3: "Mustang",
        # 4: False,
        # 5: 400
    }

    # print(test_dict)
    # print(test_dict["f"]*5)
    # test_dict.update({"key": "value"})
    # test_dict["b"].append("Delta")
    # print(r.choice(test_dict["b"]))
    # print(test_dict)

    test_cols = ["humidity", "sky"]
    # print("Column header: ", test_cols)
    line_1 = ["medium", "sunny", "test"]
    line_2 = ["high", "sunny"]
    # rules = [("humidity", "high"), ("sky", "sunny")]
    rules = [("humidity", "high")]
    # lines = [line_1, line_2]
    lines = [line_1]

    classification = True
    for k, v in test_dict.items():
        # print(k, v)
        if str(line_1[k]) == v:
            # print("yes")
            pass
        else:
            # print("no")
            classification = False
            break
    # return classification
