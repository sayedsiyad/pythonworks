
def second_max_number(*args):

     sorted_numbers=sorted(args,reverse=True) #[13,12,11,10]

     return sorted_numbers[1]


print(second_max_number(10,11,12,13))
print(second_max_number(10,11,12,13,14,15))

