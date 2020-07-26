day_one = open("um-deliveries-20140519.txt")
def order_info():
    for line in day_one:
        line = line.rstrip()
        words = line.split('|')
    
        melon = words[0]
        count = words[1]
        amount = words[2]
    
        print(f"Delivered {count} {melon} for total of ${amount}")
    day_one.close()
    
def order(day_one):
    print("Day 1")
    
    order_info.order.info
    
order(day_one)


# def day_one():
#     print("Day 1")
#     the_file = open("um-deliveries-20140519.txt")
   
    
#     for line in the_file:
#         line = line.rstrip()
#         words = line.split('|')
    

#         melon = words[0]
#         count = words[1]
#         amount = words[2]

#         print(f"Delivered {count} {melon} for total of ${amount}")
#     the_file.close()
# day_one(order_report)

# def day_two():
#     print("Day 2")
#     the_file = open("um-deliveries-20140520.txt")
#     for line in the_file:
#         line = line.rstrip()
#         words = line.split('|')

#         melon = words[0]
#         count = words[1]
#         amount = words[2]

#         print(f"Delivered {count} {melon} for total of ${amount}")
#     the_file.close()
# day_two()

# def day_three():
#     print("Day 3")
#     the_file = open("um-deliveries-20140521.txt")
#     for line in the_file:
#         line = line.rstrip()
#         words = line.split('|')

#         melon = words[0]
#         count = words[1]
#         amount = words[2]

#         print(f"Delivered {count} {melon} for total of ${amount}")
#     the_file.close()
# day_three()
