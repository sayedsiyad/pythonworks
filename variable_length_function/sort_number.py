
def sorted_number(*args,**kwargs):
    
    if kwargs.get("reverse")=="True":

        return sorted(args,reverse=True)
    
    if kwargs.get("reverse")=="False":

        return sorted(args,reverse=False)
    
print(sorted_number(1,2,6,4,15,11,reverse="True"))    