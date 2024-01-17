% Simple Dungeon Crawling Deck Builder
% Minyoung Heo

# Overview

A basic deck-builder where you need to collect minerals

You select a class.

# Core loop

The overall objective is to bring the opponent health to 0.

You draw a certain amount of mineral cards. You can play up to X mineral cards where X is the maximum capacity of a bottle. When you finish the construction of your bottle, you can get a token. Place that token on top of these ingredients to designate them as effects for your new potion.

You can play your tokens to activate the effects of the potion. 

# Enemies

# Card Master List

## Locations

The mechanic is that you can store your potion in a certain location, each location specializing in each type of damage below. Placing your potion in a corruption location means all corruption effects increase by 1, but all things corruption is _weak_ to (Decisive, Rage) will decrease by 1. Each turn these modifications happen. The longer you store the potion, the stronger it gets.

## Types of Damage:

Overal chart:

* Frozen <- Rage <- Flow <- Corruption <- Decisive …

* Frozen -> Flow -> Decisive -> Rage -> Corruption …

![Chart](damagechart.png "Chart")

_**Frozen**_ 

This kind of damage comes with negative side effects. It's meant to restrict the opponent from certain making choices.

_**Rage**_

This kind of damage is also primarily big. It deals massive damage, but also comes with more negative side effects.

_**Flow**_

This kind of damage is very _steady_. Mechanics like "being benefited from repetitive use" is kind of an idea of what kind of mechanic Flow is based on.

_**Corruption**_

This kind of damage is the poison of damage. It primarily focuses on dealing damage over time.

_**Decisive**_

This kind of damage is designed to be quick. Its damage is meant to be a priority

### Card Keywords: 

_**Infliction**_
At the start of the opponent's next turn, deals damage based on its value and decreases its value by 1

_**Frost**_
Reduces your damage dealt by half (rounded down)

_**Weak**_
Takes double damage from opponents

_**Adaptable**_
A neutral effect that turns into a specific type when mixed with other ingredients. It goes with the majority of the potion types. If it's a tie between multiple potion types, it will randomly choose one.

### Card Types:

* Quantifiers - these modify the numerical value of the effect of the potion

* Modifiers - these modify the effects of the potion
  
_**Master Card List**_
https://docs.google.com/spreadsheets/d/18WhHdy7mmHrYBu8RSTqJvJtDiZmmR1SvkhQmygA60s4/edit?usp=sharing
