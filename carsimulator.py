# command = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("car has already started")
#         else:
#             started = True
#             print("car started")
#
#
#     elif command == "stop":
#         if not started:
#             print("car has already stopped")
#         else:
#             started = False
#             print("car has stopped")
#
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# help - display help menu
# quit - to quit
#         """)
#
#     elif command == "quit":
#         break
#     else:
#         print("invalid input")


#FOR LOOPS
# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(f"total: {total}")
#
# for x in range(4):
#     for y in range(3):
#         print(f"({x},{y})")

#printing the letter F using for loop
numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "*"
    print(output)


#printing an L
letters = [2,2,2,2,2,5]
for l_count in letters:
    output = ""
    for count in range(l_count):
        output += "*"
    print(output)