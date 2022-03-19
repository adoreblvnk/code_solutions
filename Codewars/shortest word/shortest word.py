find_short = lambda s: len(sorted(s.split(), key=lambda x: len(x))[0])


# solution
def find_short_soln(s):
    return min(len(x) for x in s.split())


print(find_short("bitcoin take over the world maybe who knows perhaps"))