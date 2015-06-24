# Python
AUTHOR: Michal Martyniak, Poland
Wild world simulator ->  turn-based game.

Screenshot:
http://s24.postimg.org/5tx589udx/in_Game_Photo.png
(ikony w języku polskim. W - wilk, Z - żółw, L - lis itd.)


Base info:

-Game written in OOP Python.

-GUI made in Tkinter library.

-I have written the code imitiating PEP8 standard, for easier code reading and editing.

-PyCharm was my IDE
---------------------------------------------------------------------------------------------------------
In game there are 9 creatures.

Each one have own attributes like for example: 

initiative - decide which organism has priority movement in current round

             example: Fox is smarter so he moves first, then Turtle
             
strength - the stronger the more enemies can it kill

age - if there are two animals with the same initiative, the older one moves first.

--------------------------------------------------------------------------------------------------------
Animal species:

  they move around, reproduce themself, kill each other, eat plants
  
  
  
  
Plants species:

  they just spread around the map and stay in place
  
  
  
  
  

Animals: 

  *Human: he moves using WSAD, T- elixir that gives up to 10 strength
  
  *Wolf : strength=9, initiative=5
  
  *Sheep: strength=4, initiative=4
  
  *Fox  : strength=3, initiative=7
  
          'good sense of smell' power: fox never goes on stronger enemy's teritory
          
          
  *Turtle  : strength=2, initiative=1
  
          'motionless' power: turtle has lower chance to move somewhere. Often stay in place.
          
          'spartan shield' power: turtle avoid enemy, that has less than 5 points of strength.  
          
                                  Enemy won't win with him, then.
                                  
                                  
  *Antelope  : strength=4, initiative=4
  
          'jumping' power: antelope jumps every 2 fiels instead of 1(like other species)
          
          'fast escape' power: antelope has 50% chance to do additional move, when enemy would normally kill
          
          
          
Plants:  

  *Grass:   just grows
  
  *SowThistle: takes 3 attempts to spread somewhere
  
  *Guarana: gives +3 strength to creature, which eat it
  
  *DeadlyNightshade: Kills everyone, who eat it
  
  
  ----------------------------------------------------------------------------------------
  Additional features:
  
  *You can SAVE game to file (txt), and then LOAD it
  
  *There are 2 boxes, that informs you about events (killing, eating, reproducing)
  
  *You don't need do click 'NextRound' button, just press ENTER
  
  *MAGIC PEN, hover with mouse at some field. Randomly generated organism would appear.
                  
    



