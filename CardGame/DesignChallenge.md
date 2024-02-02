# Problem

Here's the scenario. In my game, a card can create a copy of itself, with its stats modified. So we need to define this card at compile time in our code. But when the code is run, this card needs to be generated during runtime as well. 

Essentially, we need to design an object to be created at compile time, but also an object that can be created at runtime. 

_**Approach 1**_

I suddenly had a stroke of an idea: how do deep copies work? The only way that we can create objects an runtime is create deep copies of everything. 

Of course, on the surface it seems simple, but it gets complicated when you dig in. In the example above, it seems simple enough to create a deep copy of the card itself. But the issue lies in trying to modify the stats as well. We can type in our code

```
//this function creates a card object and returns it
function createNewCard(card)
	return deepCopyOf(card)
```

but when you think about it, how are going to modify its stats? Like how would you define the object itself?

```
class Card
	effect = createNewCard
	effectArgs = self
```

So my idea comes to this: (_Imagine me holding a single card_) we don't define Card as a single piece but instead (_now imagine me ripping the cards to shreds_) we perceive the Card as a bunch of parts. So I ask again (was asked in the [CodeDoc](CodeDoc.md)), what is a card?

A card consists of effects. Now a card is not an actor of these effects, nor a catalyzer. It's merely a holder. It just has it in itself, only to have this effect to be handed to the beholder.

_**So we need to ask again, what are effects?**_

Well, effects need to be "carried out". They need to act on something. There is a source and there is a target (which may be multiple). The kind of effect can be narrowed down according to the games rules, which are defined in the [DesignDoc](DesignDoc.md). What I'm getting at is that one of the effects is _creating a card_. In other words, some target is _given_ a card. But that also means, this effect _creates_ the card as well. Even though we might say "indirectly, the source of the creation is the player", really the creation happens in the _effect_. Not only that, we also have to consider the fact that each effect contains a magnitude of the effect. If the effect is damage, the magnitude of the damage could be like 3, for an effect of dealing 3 damage. Thinking of effects as a noun, a physical entity with space and volume than a concept, this effect needs to be able to generate cards during runtime. 

This creates another problem. The concept of effects creating cards which hold effects that create cards that… It creates a tautology. It's recursive. There's no way we can define a card properly if its effects is that it creates the card. 

_**Approach 2: Redefine**_

We need to ask ourselves again, but answer them more effectively: What is a card? If it is just a holder of effects, then what is an effect? An effect cannot include "creation of cards" since that causes way too much problems.

An idea that I had in mind, although this is to be touched upon for my next update on this, is that effects do not create cards, they set into motion the "card creating machine". If we can create an effective "card creating machine" that creates cards in runtime, then effects simple "run the card creating machine" and "give that output to the player". 

_**Card Creating Machine**_

The things outside of the black box are simple:

Input: The collection of effects that a card should have

Output: The outputted card

This leads to another issue, although it may be fixable: Can an effect feed itself into the machine? Can we define an effect such that it is meant to feed itself into the machine but with stats modified? How can we generalize such an effect?

