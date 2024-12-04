
from json import load

f=open("C:\\Users\\siyadzyd\\Desktop\\pythonworks\\datasets\\countries.json",encoding="utf-8")

data=load(f)


#number of coutries
#print(len(data))


#all country names
#all_country_names=[country.get("name")for country in data]
#print(all_country_names)

#print all regions
all_regions=[country.get("region")for country in data]
print(set(all_regions))

#antartica ocean countries
region_count={region:all_regions.count(region)for region in all_regions}
#print(region_count)

max_region_count=max(region_count,key=lambda k:region_count.get(k))
#print(max_region_count,region_count.get(max_region_count))

#capital of a specific country
country_capital=[country.get("capital")for country in data if country.get("name")=="India"]
#print(country_capital)

#countries with most number of borders
country_border_count={country.get("name"):len(country.get("borders",[]))for country in data}
#print(country_border_count)

max_border_count=max(data,key=lambda country:len(country.get("borders",[]))).get("name")
#print(max_border_count)

#most populated country
most_populated_country=max(data,key=lambda country:country.get("population")).get("name")
#print(most_populated_country)

#border sharing with india

alpha_three_codes=[country.get("borders")for country in data if country.get("name")=="India"][0]

for code in alpha_three_codes:

    for country in data:

       if country.get("alpha3Code")==code:

           print(country.get("name"))

             


    