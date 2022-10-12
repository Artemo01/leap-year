# -*- coding: utf-8 -*-

class CheckLeapYear:
    def __init__(self, years_list: list):
        self.years_list = years_list

    def check_is_leap(self) -> list:
        leap_years_list = []
        for R in self.years_list:
            if R % 4 == 0 and R % 100 != 0:
                leap_years_list.append("{} is leap year".format(R))
            elif R % 100 == 0 and R & 400 == 0:
                leap_years_list.append("{} is leap year".format(R))
            else:
                leap_years_list.append("{} is not leap year".format(R))
        return leap_years_list


if __name__ == '__main__':
    check_year = CheckLeapYear(years_list=[1900, 1904, 1905, 1960])
    checker = check_year.check_is_leap()
    for element in checker:
        print(element)
