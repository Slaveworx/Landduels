'''##########################################################
   # CreatureCard CLASS -> defines the creature cards
   # Created: 2015 - 01 - 09 ||| Last review: 2015 - 01 - xx
   # Slaveworx, (add your credits here joe)
   #########################################################'''

import card

class CreatureCard(card.Card):


    creature_types= ("human", "animal", "magic_being", "shadow_being", "light_being")

    def creature_type(self, creature_type):
        """Defines the type of being the card has"""
        if creature_type not in self.creature_types:
           print "the creature type is not known"
        return str(creature_type)

