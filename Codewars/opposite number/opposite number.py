def opposite(number):
    if number > 0:
        return float(f"-{number}")
    elif number < 0:
        return float(str(number)[1:])
    return 0


opposite_soln = lambda x: -x


print(opposite_soln(-34))