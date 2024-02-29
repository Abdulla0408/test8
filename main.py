import csv
user = {"first_name": "Abdulla", "last_name":"Hayitboyev", "age":15}

with open("abdulla.csv", mode = "w") as abdull_file:
    header = ["first_name", "last_name", "age"]

    writer = csv.Dictwriter(abdull_file,header, lineterminator = "\n", delimiter = ";")
    writer.writeheader()
    writer.writerow(user)
    
# ------------------------------------------------------------------------------------------------

# import csv 
# with open("users_info_for_dict.csv", mode = "r") as file:
#     reader = csv.DictReader(file)
#     for user in reader:
#         text = f"""Ismi: {user['first_name']}
# Familiyasi: {user['last_name']}
# Yoshi: {user['age']}"""
#         print(text)
#         print("-"*100)

# ------------------------------------------------------------------------------------------------

# print("\033[31m\033[1m{}".format ("Hello World!"))

# def red(text, bold=False):
#     t = "\033[31m{}"
#     if bold:
#             t = "\033[31m\033[1m{}]"
    
#     return t.format(text)

# print(red("HelloWorld"))

# ------------------------------------------------------------------------------------------------

# def red(text, bold=False):
#     t = "\034[2m{}"
#     if bold:
#             t = "\034[0-7m\034[6m{}]"
    
#     return t.format(text)

# print(red("HelloWorld"))