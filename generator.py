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
