
arr=[10,13,15,20,21,22,23]


search_element=int(input("enter the number"))

arr.sort()

low=0

upp=len(arr)-1

is_present=False

while(low<=upp):

    #find  mid

    mid=(low+upp)//2

    #case1

    if search_element==arr[mid]:

        is_present=True
        break

    elif search_element<arr[mid]:

        upp=mid-1

    elif search_element>arr[mid]:

        low=mid+1 

print(is_present)  



