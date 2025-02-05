# # Exercises: Level 1

# # Create an empty tuple
# # empty_tuple = ()

# # # Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# # sisters = ("Gunjita", "Pranaya", "Asmitha")
# # brothers = ("LALA", "LALI")

# # # Join brothers and sisters tuples and assign it to siblings
# # siblings = sisters+ brothers

# # # How many siblings do you have?
# # print(siblings)
# # length = len(siblings)
# # print(length)

# # # Modify the siblings tuple and add the name of your father and mother and assign it to family_members
# # family_members = siblings + ("Sarbari", "Ranjit")  # Adding father and mother
# # print("Family members:", family_members)

# # # Exercises: Level 2

# # # Unpack siblings and parents from family_members
# # *siblings_list, mother, father = family_members
# # print("Siblings (unpacked):", siblings_list)
# # print("Father:", father)
# # print("Mother:", mother)

# # Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
# fruits = ("apple","mango" )
# vegetables = ("brinjal" , "potato")
# animal_products = ("milk" ,"meat")
# food_stuff_tp = fruits + vegetables + animal_products
# print(food_stuff_tp)
# # Change the about food_stuff_tp tuple to a food_stuff_lt list
# food_stuff_tp = list(food_stuff_tp)
# # Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# food = food_stuff_tp[2:4]
# print(food)
# food_stuff_tp =  tuple (food_stuff_tp)

# # Slice out the first three items and the last three items from food_staff_lt list
# ft = food_stuff_tp[0:3]
# lt = food_stuff_tp[3:6]
# print(ft)
# print(lt)
# Delete the food_staff_tp tuple completely
# del food_stuff_tp
# Check if an item exists in tuple:
# print(food_stuff_tp)
# Check if 'Estonia' is a nordic country

# Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print ('Iceland' in nordic_countries)
