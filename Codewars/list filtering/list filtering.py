filter_list = lambda l: [i for i in l if type(i) is not str]

print(filter_list([1,2,'a','b']))