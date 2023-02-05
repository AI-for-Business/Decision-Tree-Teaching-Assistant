def act_sens_0():
    print("function 0")


def act_sens_1():
    print("function 1")


def act_sens_2():
    print("function 2")


def act_sens_3():
    print("function 3")


def act_sens_4():
    pass


def act_sens_5():
    pass


def act_sens_6():
    pass


def act_sens_7():
    pass


dict_spread = {
    0: act_sens_0,
    1: act_sens_1,
    2: act_sens_2,
    3: act_sens_3,
    4: act_sens_4,
    5: act_sens_5,
    6: act_sens_6,
    7: act_sens_7,
}

key_value = 7
dict_spread.get(key_value, "no_value_to_key")()
