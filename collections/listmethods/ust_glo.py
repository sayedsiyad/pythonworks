
#sample input

arr=[100,200,300,400,500,600,700,800]
#     0   1   2   3   4   5   6   7

#output

#result=[100,800,300,600,500,400,700,200]

#sample input2

arr=[10,20,30,40,50,60]
#     0  1  2  3  4  5

#result=[10,20,30,40,50,20]

arr=[100,200,300,400,500,600,700,800]

arr=[10,20,30,40,50,60]

odd_position_number=[num for index,num in enumerate(arr) if index%2!=0]

odd_position_number.reverse()

print(odd_position_number)

for index,num in enumerate(odd_position_number):

    arr[index+1]=num

print(arr)    