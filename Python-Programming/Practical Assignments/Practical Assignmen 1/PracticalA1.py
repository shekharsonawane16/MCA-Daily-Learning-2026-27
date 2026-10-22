# 1. Read names from a file and store them in a list
with open("student.txt","r") as f:
    names = f.read().splitlines()

print(names)


# 2. Print names longer than 5 characters
# # with open("student.txt") as f:
# #     names=f.read().splitlines()

# # for name in names:
# #     if len(name) > 5:
# #         print(name)


# 3. Count names starting with a vowel
# # with open("student.txt") as f:
# #     names=f.read().splitlines()

# # count=sum(name[0].lower() in "aeiou" for name in names)
# # print(count)


# 4. Save names longer than 5 characters into a new file
# # with open("student.txt") as f:
# #     names=f.read().splitlines()

# # with open("filtered.txt","w") as f:
# #     f.write("\n".join(name for name in names if len(name) > 5))


# 5. Sort names alphabetically and print them
# # with open("student.txt") as f:
# #     names=f.read().splitlines()

# # for name in sorted(names):
# #     print(name)


# 6. Print names containing the letter "a"
# # with open("student.txt") as f:
# #     names=f.read().splitlines()

# # for name in names:
# #     if "a" in name.lower():
# #         print(name)


# 7. Count name frequency and store it in a dictionary
# # with open("student.txt") as f:
# #     names=f.read().splitlines()

# # freq={}
# # for name in names:
# #     freq[name]=freq.get(name,0)+1

# # print(freq)


# 8. String analysis of each name
# # with open("student.txt") as f:
# #     names=f.read().splitlines()

# # for name in names:
# #     print(name,len(name),name[0],name[-1],name.lower()==name.upper()[::-1])


# 9. Remove duplicates, sort by length, and save to a file
# # with open("student.txt") as f:
# #     names=f.read().splitlines()

# # names=sorted(names,key=len)

# # with open("processed.txt","w") as f:
# #     f.write("\n".join(names))



# 10. Group names by starting letter into separate files
# Creates files such as A_names.txt, B_names.txt, and S_names.txt
# with open("student.txt") as f:
#     names=f.read().splitlines()

# groups={}
# for name in names:
#     letter=name[0].upper()
#     groups.setdefault(letter,[]).append(name)

# for letter,group in groups.items():
#     with open(f"{letter}.txt","w") as f:
#         f.write("\n".join(group))