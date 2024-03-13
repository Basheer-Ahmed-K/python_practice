# There are two ways to slice a string
#  1. using indexing [] its parameters [start, stop, step]
#  by default the start, stop, step  values are start-0, stop-max, step-1
#  2. Using slice() function
name = "Diggibyte Technology"

first_name = name[:9]  # you can ask it should be [0:8] but here 8 is exclusive, so I`m using 9
print(first_name)

last_name = name[10:]
print(last_name)

website1 = "https://google.com"
website2 = "https://diggibyte.com"
website3 = "https://abcdefghijklmnopqrstuvwxyz.com"
# Extract only name from the link
# slice also works the same but here instead of using ":" colon we use "," comma

temp = slice(8, -4)

print(website1[temp])
print(website2[temp])
print(website3[temp])
