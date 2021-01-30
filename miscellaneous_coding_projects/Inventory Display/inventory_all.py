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
    count = 0
    x = inv['gold coin']
    y = inv['dagger']
    gold = int(x)
    dagger = int(y)

    for item in dragonLoot:
        if item in inv.keys():
            inv[item] += 1
        else:
            inv[item] = 1
    print("You have added to your inventory" + str(inv))


inv = {'gold coin': 42, 'rope': 1, 'dagger': 0}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
invAdd = addToInventory(inv, dragonLoot)
display_Inventory(inv)
