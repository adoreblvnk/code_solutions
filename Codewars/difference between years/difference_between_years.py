def how_many_years(date1, date2):
    return abs(int(date1[:4]) - int(date2[:4]))

# solution
def how_many_years_solution(date1,date2):
    return abs(int(date1.split('/')[0]) - int(date2.split('/')[0]))

print(how_many_years('1997/10/10', '2015/10/10'))