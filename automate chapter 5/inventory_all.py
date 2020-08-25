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
    inv.setdefault('dagger', 1)
    x = inv['gold coin']
    y = inv['dagger']
    gold = int(x)
    dagger = int(y)

    for i in dragonLoot:
        if i == 'gold coin':
            count+=1
            math_gold = gold + count
            inv.update({'gold coin': math_gold})
        if i == 'dagger':
            count+=1
            math_dagger = dagger + count
            inv.update({'dagger':math_dagger})
        if i == 'ruby':
            count+= 1
            inv['ruby'] = 1



inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
display_Inventory(stuff)
