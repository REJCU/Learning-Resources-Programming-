hero_inventory = {
    'gold coin': 1250,
    'health potion': 3,
    'mysterious map': 1,
    'rusty sword': 1,
    'wolf pelt': 12,
    'dragon scale': 2,
    'bread': 5,
    'unidentified scroll': 4
}

def delete_item(hero_inventory):
    selling = input(str('Sell: '))
  #  del hero_inventory[selling]
 #   print(hero_inventory)
    selling_amount = int(input(("amount: ")))
    x = hero_inventory[selling]
    x = x - selling_amount
    hero_inventory[selling] = x
    print(hero_inventory)
    



chest = {"health potion" : 3,
         "dragon_scale" : 1}

def find_treasure(chest):
    for item,amount in chest.items():
        hero_inventory.setdefault(item, 0)
        hero_inventory[item] += amount
    print(hero_inventory)



def search():
    if 'mysterious map' in hero_inventory:
        print("You know where to go")


search()
