# dict.get() 

# initializing string 
string_In = "Mississippi"
res = {} 

for keys in string_In: 
	res[keys] = res.get(keys, 0) + 1

# printing result 
print ("Count of all characters is : \n"
											+ str(res))
#Output:
#Count of all characters is : 
#{'M': 1, 'i': 4, 's': 4, 'p': 2}
