from math import sqrt, asin


def GetMBC(AB, BC):
    MC = 0.5 * sqrt(AB ** 2 + BC ** 2)
    return asin(MC / BC)


if '__name__' == '__main__':
    AB = int(input())
    BC = int(input())
    print(GetMBC(AB, BC))