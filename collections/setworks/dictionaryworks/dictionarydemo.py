

product={"id":100,"title":"domminar","price":4500,"brand":"bajaj"}


print(product["title"])

product["price"]=5000



product["use_by_date"]="23-06-2002"

#add offer 10

if "offer" in product:

    product["offer"]=10

else:

    product["offer"]=20

    print(product)    