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
    


delete_item(hero_inventory)
