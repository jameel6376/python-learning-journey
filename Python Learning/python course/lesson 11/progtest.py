#RPG character
character_profile = {
    'name': 'jameel',
    'class': 'Warrior',
    'level': 1
}

base_stats = { 
    'hp': 100,
    'attack': 15,
    'defense': 10
}


inventory = ['Wooden Sword', 'Health Potion']

special_traits = {'Critical Strike', 'Quick Dodge'}

def equip_item(item_name, attack_bonus):
    if item_name not in inventory:
        inventory.append(item_name)
        base_stats['attack'] += attack_bonus
        return f' the item {item_name} is equipped.\n updated attack stat:\n HP: {base_stats['hp']}\n Attack: {base_stats['attack']}\n Defense: {base_stats['defense']}'

def open_loot_boxes(box_rewards_list):
    if len(box_rewards_list) == 0:
        return 0 
    return box_rewards_list[0] + open_loot_boxes(box_rewards_list[1:])

while True:
    mainmenu = input('''
    === BATTLE ARENA MAIN MENU ===
    1. View Character Sheet & Inventory
    2. Equip New Weapon / Gear
    3. Enter the Battle Arena (Calculate Gold Reward)
    4. Exit Game
    ''')
    if mainmenu == "1":
        str(character_profile['level'])
        print(f' Character info:\nname: {character_profile['name']}\nclass: {character_profile['class']}\nlevel: {character_profile['level']}')
        print('\n Character Stats:\n')
        for item, quantity in base_stats.items():
         print(item + '   ' + str(quantity))
        print(f'''
        === inventory ===
        {inventory}
        ''')
    elif mainmenu == '2':
        newwpn = input(' What weapon have you found?\n')
        attdmg = int(input(' Weapon attack damage bonus:\n'))
        itequip = equip_item(newwpn, attdmg)
        print(itequip)
    elif mainmenu == '3':
        print('battle completed!')
        golddrops = [30, 60, 15, 100]
        opened = open_loot_boxes(golddrops)
        print(opened)


    
        






        




