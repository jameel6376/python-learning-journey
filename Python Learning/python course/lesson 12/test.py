def createCharacter(name):

    hp = 100
    def getHP():
        nonlocal hp
        print(name + " has " + str(hp) + " HP." )
    def takeDamage(amount):
        nonlocal hp
        dt = hp - amount
        hp = dt
        if hp < 0:
            hp = 0
    def heal(amount):
        nonlocal hp
        h = hp + amount
        if h > 100:
            hp = 100
        else:
            hp = h
    return {'getHP': getHP, 'takeDamage': takeDamage, 'heal': heal}



warrior = createCharacter('Thor')
warrior['getHP']()



