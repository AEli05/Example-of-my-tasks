import typing as tp
from math import *


def calc_two_numbers(num_1: float, num_2: float, command: str) -> tp.Union[float, str]:
    command_all = ["+", "-", "**", "/", "log", "ln", "sin", "cos", "tg"]
    if command == "+":
        result = num_1 + num_2
        return result
    if command == "-":
        result = num_1 - num_2
        return result
    if command == "/" and num_2 == 0:
        result = "you can't divide with 0"
        return result
    if command == "/" and num_2 != 0:
        result = num_1 / num_2
        return result
    if command == "*":
        result = num_1 * num_2
        return result
    if command == "**" and num_2 == 2:
        result = pow(num_1, 2)
        return result
    if command == "**" and num_2 >= 0 and num_2 != 2:
        result = pow(num_1, num_2)
        return result


def calc_one_number(num_1: float, command: str) -> tp.Union[float, str]:
    if command == "log" and num_1 > 0:
        result = log(num_1)
        return result
    if command == "log" or command == "log10()" and num_1 <= 0:
        result = "try again"
        return result
    if command == "log10()" and num_1 > 0:
        result = log10(num_1)
        return result
    if command == "sin":
        r = radians(num_1)
        result = sin(r)
        return result
    if command == "cos":
        r = radians(num_1)
        result = cos(r)
        return result
    if command == "tg":
        r = radians(num_1)
        result = tan(r)
        return result
    if command not in command_all:
        result = "try again"
        return result


if __name__ == "__main__":
    while True:
        command_all = ["+", "-", "**", "/", "log", "ln", "sin", "cos", "tg"]
        COMMAND = input("Введите операцию:")
        if COMMAND.isdigit() and int(COMMAND) == 0:
            break
        if COMMAND.isalpha() and COMMAND == "log" or COMMAND == "log10()" or COMMAND == "sin" or COMMAND == "cos" or COMMAND == "tg":
            NUM_1 = float(input("Первое число -> "))
            result_1 = calc_one_number(NUM_1, COMMAND)
            print(result_1)
        if COMMAND not in command_all:
            print("try again")
            continue
        if COMMAND.isalpha() and COMMAND == "+" or COMMAND == "-" or COMMAND == "*" or COMMAND == "**" or COMMAND == "/":
            NUM_1_1 = float(input("Первое число -> "))
            NUM_2_1 = float(input("Второе число -> "))
            result = calc_two_numbers(NUM_1_1, NUM_2_1, COMMAND)
            print(result)
