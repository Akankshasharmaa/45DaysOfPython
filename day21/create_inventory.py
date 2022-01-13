def create_inventory(items):
    return add_items({}, items)

def add_items(inventory_dict, items):
    for item in items:
        if item not in inventory_dict:
            inventory_dict[item] = 1
        else:
            inventory_dict[item] += 1
    return inventory_dict

def decrement_items(updated_inventory, items):
    for item in items:
        if item in updated_inventory and updated_inventory[item] > 0:
            updated_inventory[item] -= 1
        else:
            updated_inventory[item] = 0
    return updated_inventory

def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
        return inventory
    else:
        return inventory
    
def list_inventory(inventory):
    mylist = []
    for key in inventory:
        if inventory[key] > 0:
            mylist.append((key,inventory[key]))
    return mylist

if __name__ == '__main__':
    inventory_dict = create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"])

    updated_inventory = add_items(inventory_dict, ["wood", "iron", "coal", "wood"])
    
    decrement_inventory = decrement_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"])
    
    removed_inventory = remove_item({"coal":2, "wood":1, "diamond":2}, "gold")

    inventory_list = list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0})
    print(inventory_list)