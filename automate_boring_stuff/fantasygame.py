stuff = {'rope': 1,
             'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    num_item = 0
    for x,y in inventory.items():
        num_item = num_item + x.get(item, 0)
    print("Total number of items: " + str(num_item))

print(display_inventory(stuff))

