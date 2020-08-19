stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in stuff.items():
        numbers = int(stuff.get(k))
        item_total += numbers
    print(str(stuff))
    print("Total number of items: " + str(item_total))

display_inventory(stuff)
