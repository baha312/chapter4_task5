# AK-47
#
# Soldier Ryan has an AK47
# Soldiers can fire ("tigi-tigitishh").
# Guns can fire bullets.
# Guns can fill bullets - increase the number of bullets(reloads)
#
# Create class Act_of_Shooting, which will inheritates from class Soldier, class Guns.
# Where soldier will fire from a gun and reload, and fire one more time.

class Soldier:
    def __init__(self,name):
        self.name = name

class Gun:
    def __init__(self):
        self.bullets = 35

    def AK47(self):
        print(f"\tSoldier {self.name.title()} scream 'A-ta-ta'")
        print(f"\t\tAK47 did: ")
        if self.bullets:
            piy = 0
            for x in range(self.bullets):
                piy += 1
                self.bullets -= 1
                print("\t\t\tti-gi-ti-gi-tish",piy)
        else:
            print(f"No bullets!")
            self.patrons()

    def patrons(self):
        print(f"\t\t\tBullets left {self.bullets} pieces")

    def reload(self):
        self.bullets = 40
        print(f"\t\t\tSoldier {self.name.title()} scream 'REALOAD!'")

class Act_of_Shooting(Soldier,Gun):
    def __init__(self,name):
        Soldier.__init__(self,name)
        Gun.__init__(self)
        print(f"\t\t\tBullets: {self.bullets} pieces")

Soldier = Act_of_Shooting("Peter")
Soldier.AK47()