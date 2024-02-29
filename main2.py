#  1-vazifa users_info.csv fayliga yozildi

# ----------------------------------------------------------------------------

# ikkinchi vazifa
#   |
# with open("users_info.csv", "r") as file:
#     file.read()
#     print(file)
#     file.close()

# print(file)

# ----------------------------------------------------------------------------

# uchinchi vazifa
#  |
# file = open("users_info.csv", mode = "r", encoding = "utf-8")
# content = file.read()

# file2 = open("users_info.txt", mode = "w", encoding = "utf-8")
# file2.write(content)

# file.close()
# file2.close()

# ----------------------------------------------------------------------------

# tortinchi vazifa
#  |
# def raqam_qabul_qiluvchi(raqam):
#     try:
#         raqam = float(raqam)
#         natija = raqam + 2
#         return f"**<span style='color:red'>{natija}</span>**"
#     except ValueError:
#         return "**<span style='color:red'>Qabul qilingan raqam-raqam emas</span>**"
# print(raqam_qabul_qiluvchi(15))

# ----------------------------------------------------------------------------

# beshinchi vazifa
#  |
# def raqam_qabul_qiluvchi(x1,x2):
#     try:
#         x1,x2 = str(x1) or str(x2)
#         natija = x1+x2
#         return f"**<span style='color:green'>{natija}</span>**"
#     except ValueError:
#         return "**<span style='color:green'>Qabul qilingan raqam-raqam emas</span>**"
# print(raqam_qabul_qiluvchi(15))