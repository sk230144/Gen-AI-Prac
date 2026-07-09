# List in python

fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits[0]);


# dictionary

user = {"name": "Saurabh", "role":"developer"}
print(user["name"])


# tuple

point = (2, 5)
# point[0] = 4
print(point[0])

# set

unique_set = {1, 2, 3, 4, 4, 7}
print(unique_set)

# .map() and .filter()
nums = [1, 2, 3, 4, 5, 6];

# map
doubles = [x*2 for x in nums]; 

# filter  
evens = [x for x in nums if x%2 == 0]
print(doubles, "doubles")
print(evens, "evens")

squares_dic = {x : x*x for x in nums}
print(squares_dic, "squares_dic")

unique_lens = {len(w) for w in ["a","bb","cc"]}  # set comprehension
print(unique_lens, "unique_lens")


