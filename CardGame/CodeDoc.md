# Documentation For Card Game

# What is an EffectPacket?

EffectPacket is a chunk of information that specifies an action that the source does to a target (if A → B, the EffectPacket is the '→').
The EffectPacket holds the following information

* The source

* The target

* Healing done

* Damage and the type of damage done

* Statuses

    * infliction
 
    * frost
 
    * weak
 
    * adaptable

* Cards given

(Ex: If player A want to damage player B with type frozen, the EffectPacket should hold:

```
source: A
target: B
Damage: 1
Damage Type: frozen
```
)

# What is a Card?

Desired Effect → Card → Potion.

A card is an object that the player has in their hands. 

These objects can be selected to be **combined** into a [Potion](#what-is-a-potion). A card should display to the player its name and what it does (hopefully) effectively. At the same time, the card contains one or more effects (currently the [EffectPacket](#what-is-an-effectpacket)) that can be combined with other cards' effects so that a produced Potion has all the effects combined. 

# What is a Potion?

A potion is the combined effects of the cards. It's a collection of Effects. This is an object that the player can do three things with:

1. Consume (apply effects on self)

2. Throw (apply effects on target)

3. Store (multiply effects)



