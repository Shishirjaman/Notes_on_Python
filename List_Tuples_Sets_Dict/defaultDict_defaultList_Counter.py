# collections library in python provide default dictionary, list and Counter
from collections import defaultdict

# default dictionary automatically assigns default value if key doesn't exist
count_dict = defaultdict(int) # automatically set values 0 when dictionary created
words = ["apple", "banana","orange", "mango", "lichi"]
for w in words:
    count_dict[w] += 1
    
print(count_dict)


# Default list: list value type dictionary 
group_dict = defaultdict(list)
pairs = [("a",1),("a",2),("b",3)]
for k,v in pairs:
    group_dict[k].append(v) # for same key it will append the value 

print(group_dict)


# Counter: specialized dictionary for counting hashable objects
from collections import Counter

data = ['cat', 'dog', 'mouse', 'tiger', 'monkey', 'tiger', 'bird', 'tiger']

# Counter will create a dictionary with the unique parameters as keys of the dictionary
# at the parameters items number of presence as a value
# for example: in data list all items are once exceot tiger. So all items including tiger 
# will be the key and values for all items will be 1 where for tiger key it will be 3
# because it exists  3 times. And maximum value(occurrence) item will be placed first, means
# sorted descending order
counter_obj = Counter(data)
print(counter_obj)

# most common elements of the counter object
print(counter_obj.most_common)
print(counter_obj.most_common(1)) # returns maximum occurence key, value pair
print(counter_obj.most_common(2)) # returns top 2 maximum occurence key, value pairs
print(counter_obj.most_common(3)) # returns top 3 maximum occurence key, value pairs
maximum_item = counter_obj.most_common(1)
print(maximum_item[0][0]) # most occurrence items key
print(maximum_item[0][1]) # most occurrence items value

# access count of specific element
print(counter_obj['tiger'])

# arithmetic operations on counters
c1 = Counter("aabbcc")
c2 = Counter('abbbb')

print(c1 + c2)
print(c1 -c2)
