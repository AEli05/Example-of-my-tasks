from math import *


def calc_two_numbers(num_1: float, num_2: float, command: str) -> tp.Union[float, str]:
    command_all = ["+", "-", "**", "/", "log", "ln", "sin", "cos", "tg"]
    if command == "+":
        result = num_1 + num_2
        return result
    if command == "-":
        result = num_1 - num_2
        return result



if __name__ == "__main__":
    while True:
        COMMAND = input("Введите операцию:")
        if COMMAND.isdigit() and int(COMMAND) == 0:
            break
        if COMMAND.isalpha() and COMMAND == "+" or COMMAND == "-" or COMMAND == "*" or COMMAND == "**" or COMMAND == "/":
            NUM_1_1 = float(input("Первое число -> "))
            NUM_2_1 = float(input("Второе число -> "))
            result = calc_two_numbers(NUM_1_1, NUM_2_1, COMMAND)
            print(result)
