values_list = [33, 497.54, "stop"]
values_dict = {'a': "rep", 'b': False, 'c': 69}
def print_params(a = 1, b = str, c = True):
    print(a, b, c)

values_list_2 = ["nonstop", 76.3]

print_params(4, 44, 4)
print_params(False, False, False)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)