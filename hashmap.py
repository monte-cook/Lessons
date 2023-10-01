# Create an empty hashmap
my_hashmap = {}

# Add key-value pairs to the hashmap
my_hashmap['name'] = 'John'
my_hashmap['age'] = 30
my_hashmap['city'] = 'New York'

# Access values using keys
print("Name:", my_hashmap['name'])
print("Age:", my_hashmap['age'])
print("City:", my_hashmap['city'])

# Check if a key exists in the hashmap
if 'country' in my_hashmap:
    print("Country:", my_hashmap['country'])
else:
    print("Country key does not exist in the hashmap")

# Modify the value associated with a key
my_hashmap['age'] = 31
print("Updated Age:", my_hashmap['age'])

# Remove a key-value pair from the hashmap
del my_hashmap['city']

# Iterate through the hashmap
for key, value in my_hashmap.items():
    print(key, ":", value)

# Check the length of the hashmap
print("Hashmap Length:", len(my_hashmap))
