# Wild world simulator -> just a game

Screenshot:
![Link to screenshot](http://i.imgur.com/NUZ9U4u.png)

(icons were made in polish language, sorry for now)
(ikony w języku polskim. W - wilk, Z - żółw, L - lis itd.)

## Basic info:

- Game written in OOP Python.

- GUI made in Tkinter library.

- I tried to use PEP8 standard, for easier code reading and editing.

- I wrote that as my very first Python project, so don't blame me for crappy code

- PyCharm was my IDE

## __Rules__
no rules, it's a ~sandbox or ~simulation
1. There are 9 creatures.

2. Each one has its own attributes like: 
  - initiative - decide which organism can move first
```
example: Fox is smarter so he moves first, then Turtle, etc.
```

  - strength - the stronger animal is, the more enemies it can defeat

  - age - if there are two animals with the same initiative, the older one moves first.

**what animal species does:**

  they move around, reproduce themself, kill each other, eat plants
  
**what plants does**

  they just spread around the map and make no moves


## Animals: 


Spiecies | desciption | strength | initiative 
------------ | -------------|-------------|---------------
Human |  he moves using WSAD, drink stamina elixir that gives up to 10 strength on 'T' key, in game he is a 'C' letter like człowiek in polish | - | -
Wolf | - | 9 | 5
Sheep | - | 4 | 4
Fox | SMART power: fox never goes on stronger enemy's teritory | 3 | 7
Turtle | <ul><li>MOTIONLESS power: turtle has lower chance to move somewhere. Often stay in place.</li><li>>SPARTAN SHIELD power: turtle avoid enemy, that has less than 5 points of strength. Enemy won't win with him, then.</li></ul> | 2 | 1
Antelope |  <ul><li>CRAZY JUMP power: antelope jumps every 2 fiels instead of 1(like other species)</li><li>FAST ESCAPE power: antelope has 50% chance to do additional move, when enemy would normally kill</li> | 4 | 4
  
## Plants:
Plant | desciption 
------------ | -------------
Grass | just grows, useless
Sow thistle | takes 3 attempts to spread somewhere
Guarana | once eaten gives +3 strength
Deadly nightshade | once eaten, kills

## Additional features:
  
- --You can SAVE game into file (txt), and then LOAD it--
  
- There are 2 boxes, that informs you about events (killing, eating, reproducing)
  
- You don't need to click 'NextRound' button, just press ENTER
  
- MAGIC PEN, hover with mouse at some field. Randomly generated organism would appear.
                  
## TODO
- [x] use PEP
- [x] update README to markdown
- [ ] fix game saving and loading beacuse it doesn't work at all
- [ ] adapt to new PEP rules
- [ ] delete crappy code, start anew
- [ ] maybe use PyGame




