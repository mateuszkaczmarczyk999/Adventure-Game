import csv

#inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {}

def import_inventory(inventory, filename='import_inventory.csv'):
    """imports new inventory items from a file, updates "inv" dictionary"""
    file_init = open(filename, "a+")

    with open(filename, newline='') as f:
        file_list = csv.reader(f)
        imp_inv = []
        i = 0
        for row in file_list:
            if i > 0:
                imp_inv.append([row[0], row[1]])
            i += 1

    file_init.close()

    for item in range(len(imp_inv)):
        if (imp_inv[item][0]) in inv.keys():
            inv[imp_inv[item][0]] += int(imp_inv[item][1])
        elif (imp_inv[item][0]) not in inv.keys():
            inv[imp_inv[item][0]] = int(imp_inv[item][1])

import_inventory(inv)


def display_inventory(inventory):
    """displays actual inventory in simple list"""
    print()
    print("Inventory:")
    for item in inventory:
        print(inventory[item], item)
    print('Total number of items:', sum(inventory.values()))


def add_to_inventory(inventory, items):
    """adds new items to inventory"""
    updated_inv_dict = inventory.copy()
    for thing in items:
        if thing in updated_inv_dict:
            updated_inv_dict[thing] += 1
        else:
            updated_inv_dict[thing] = 1

    return updated_inv_dict

loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


inv = add_to_inventory(inv, loot)
display_inventory(inv)


def print_table(inventory, order="unorder"):
    """displays inventory in table"""
    inv_list = []
    strings_list = []
    quantities_list = []

    for thing in inv:                       # converts dictionary to list
        inv_list.append([inv[thing], thing])

    for string in range(len(inv_list)):     # checks for longest string
        strings_list.append(inv_list[string][1])
    longest = max(strings_list, key=len)
    max_str_lenght = len(longest)

    for quantity in range(len(inv_list)):  # checks for longest number of quantities
        quantities_list.append(inv_list[quantity][0])
    largest_quantity = max(quantities_list)
    longest_number = len(str(largest_quantity))

    if order == "count,desc":
        inv_list_copy1 = inv_list[:]
        inv_list_copy1.sort()
        inv_list_copy1.reverse()

    elif order == "count,asc":
        inv_list_copy2 = inv_list[:]
        inv_list_copy2.sort()

    if order == "unorder":
        list_to_print = inv_list[:]
    elif order == "count,desc":
        list_to_print = inv_list_copy1[:]
    elif order == "count,asc":
        list_to_print = inv_list_copy2[:]

    strings_len_shift = max_str_lenght + 4          # generates shift parameters
    str_shift = "{:>" + str(strings_len_shift) + "}"
    quantities_len_shift = longest_number + 5
    qua_shift = "{:>" + str(quantities_len_shift) + "}"

    print()
    print("Inventory:")
    print(qua_shift.format("count"), str_shift.format("item name"))
    print("-" * (quantities_len_shift + strings_len_shift + 1))

    for item in range(len(list_to_print)):
        print(qua_shift.format(list_to_print[item][0]), str_shift.format(list_to_print[item][1]))

    print("-" * (quantities_len_shift + strings_len_shift + 1))
    print("Total number of items:", sum(inventory.values()))
    print()

print_table(inv, "count,desc")


def export_inventory(inventory, filename='export_inventry.csv'):
    """exports all inventory to file"""
    file_init = open(filename, "w")
    inv_temp = [['item_name', 'count']]

    for thing in inventory:                       # adds inv dictionary to temporary list
        inv_temp.append([inventory[thing], thing])

    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)

        for item in range(len(inv_temp)):
            writer.writerow(inv_temp[item])

    file_init.close()

export_inventory(inv)
