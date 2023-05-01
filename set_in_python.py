#set 
#create a set 
city= {"Rabat", "Paris", "Madrid"}
city.add("London")
print(city)
city_2={"Berlin", "Tokyo"}
city.update(city_2)
print(city)
#join sets 
#union() method to join sets
city= {"Rabat", "Paris", "Madrid"}
city_2={"Berlin", "Tokyo"}
city.union(city_2)
print("this is join of two sets: ", city)
#intersection of two sets
city= {"Rabat", "Paris", "Madrid"}
city_2={"Rabat","Berlin", "Tokyo"}
city.intersection_update(city_2) # intersection_update will make change in set city
print("this is intersection of two sets:", city)
#update() method to join two sets
city= {"Rabat", "Paris", "Madrid"}
city_2={"Berlin", "Tokyo"}
city.update(city_2)
print("join two sets result using update() method : ", city)
#using symmetric_difference_update()
city= {"Rabat", "Paris", "Madrid"}
city_2={"Berlin", "Tokyo"}
city.symmetric_difference_update(city_2)# will make changes in set
print(city)
#join two set without changing the original 
#using intersection() methodd
city= {"Rabat", "Paris", "Madrid"}
city_2={"rabat", "Berlin", "Tokyo"}
new_city = city.intersection(city_2) # intersection will send new set
print("the original set : ", city)
print("the set after intersetion : ", new_city)
#using symmetric_difference() method 
city= {"Rabat", "Paris", "Madrid"}
city_2={"Berlin", "Tokyo"}
city.symmetric_difference(city_2) # will return new set
print(city)
lost_city = city.symmetric_difference(city_2)
print(lost_city)
city.symmetric_difference_update(city_2)# will make changes in set
print(city)
