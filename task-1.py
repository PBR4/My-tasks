#################################################################################### 1: Capitalize the names in the list.
# def capitalize():
#     name = input("Please enter your names by separating them with ',':")
#     my_list = name.split(",")
#     my_list = [word.strip().title() for word in my_list]
#     return my_list
# formatted_list = capitalize()
# print(formatted_list)
#################################################################################### 2: Final value of the list.
# n = int(input("Enter the length of the list: "))
# m = int(input("Enter m (for separating the members): "))
# ls = input("Enter the members of the list(comma-separated): ")
# numbers_list = [int(num.strip()) for num in ls.split(',')]
# sums = []
#
# for i in range(0, len(numbers_list), m):
#     part = numbers_list[i:i + m]
#     part_sum = sum(part)
#     sums.append(part_sum)
# print("List of sums:", sums)
#
# result = sums[0]
# for i in range(1, len(sums)):
#     if i % 2 == 1:
#         result -= sums[i]
#     else:
#         result += sums[i]
#
# print("Final result:", result)
#################################################################################### 3: fruits.
# num_fruits = int(input("Please enter the number of fruits: "))
# fruits_list = []
# count_fruit = {}
# for i in range(num_fruits):
#     fruits_info = {}
#     name = fruits_info["name"] = input("Please enter name: ")
#     shape = fruits_info["shape"] = input("Please enter shape: ")
#     mass = fruits_info["mass"] = int(input("Please enter mass: "))
#     volume = fruits_info["volume"] = int(input("Please enter volume: "))
#
#     if 300 <= mass <= 600 and 100<=volume<=500 and shape == "sphere":
#         fruits_list.append(fruits_info)
#
#         count_fruit[name] = count_fruit.get(name, 0) + 1
#
# print(fruits_list)
# print(count_fruit)
#################################################################################### 4: is spam or not?
# def classify_message(msg_id, msg_text):
#     invalid_id = msg_id.isdigit()
#
#     special_chars_count = sum(1 for char in msg_text if char in "!@#$%^&*()_+-=[]{}|;:'\",.<>?/\\")
#     invalid_text = special_chars_count > len(msg_text) / 2 or "spam" in msg_text.lower()
#
#     if invalid_id and invalid_text:
#         return "Fully Invalid"
#     elif invalid_id:
#         return "Invalid Sender"
#     elif invalid_text:
#         return "Invalid Content"
#     else:
#         return "Not Spam"
#
#
# msg_id = input("Enter message ID: ")
# msg_text = input("Enter message text: ")
#
# print(classify_message(msg_id, msg_text))
