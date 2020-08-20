import pprint

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_Inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        numbers = int(inventory.get(k))
        item_total += numbers
        print(str(k) + ' ' + str(inventory.get(k)))
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for k, v in inv.items():
        if inv[k] in dragonLoot:
            print(test)


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
display_Inventory(inv)
