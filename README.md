# Unit 1: A classic game 
![](game.gif)

# Criteria A: Planning



## Problem definition

The owner of the local game shop is an enthusiast of classic computer games. He has been looking for a talented programmer that can help him revive his passion for text-based games. He has few requirements for this task:


Apart for this requirements, the owner is open to any type of game, topic or genre.

### Proposed Solution


## Design statement
I will try to design and make a game for a client who is the owner of the local game shop. The game will be an escape game and is constructed using the software python 3.10. It will take 3 weeks to make and will be evaluated according to the criteria A and B.

## Justification 
This game is created using python because it is the only language I am familiar with, thus it is one of the most commonly used programming languages in the world. The game will be based on Mac OS, with an application called Pycharm. Pycharm was chosen to be used for this project because I am familiar with the application, and is one of the most used coding applications in the world. Pycharm is beginner-friendly in which the errors are clearly identified and highlighted. In addition, Pycharm processes are quick and efficient and therefore increases productivity and speed of my work. 
 
## Details
This game is an entirely text-based adventure game, in which the goal of the player is to escape the ISAK KAC building without getting caught by anyone. The player is meant to make appropriate decisions throughout the game to complete the game. The game will provide an inventory system where players are able to pick up items and use them accordingly. The game will keep track of the players’ name and score (time taken for the player to complete the game), and this information will be transferred to a database and will be displayed. The results would be displayed in ranking form where the person who completed the game the fastest would be inscripted on top. Additionally, this game is designed to be completed in a specific period of time frame, which is 15 mins. 


## Success Criteria
1. The game has to be entirely text-based.
2. The game must record the time played.
3. The game must record the player name and score.
4. Display rankings; name of player and score
5. Inventory system to secure items obtained by player
6. Add time limit of 15 mins

# Criteria B: Design

## System Diagram
![](system_diagram1.jpg)
Figure 1. system diagram for the game

The system will be based on Mac OS 10.15.6 with Dual-Core Intel Core i3. This game will be created on python 3.9, where input will be from keyboard and output generated as text on screen monitor. 


## Flow Diagrams
![](flowchart1.jpg)
Flow chart 1:
This is the flow chart for the confirm input system, where, the users' name, grade and advisor are asked and confirmed to ensure accuracy in the input of information.

![](flowchart2.jpg)
Flow chart 2:
This is the flow chart of the beginning of the game, where the player is asked two locational option to preceed into. Here, one option leads to an immediate game ending, and the other proceeds to picking up items and filling the inventory.

![](flowchart3.jpg)
Flow chart 3:
This is the flow chart of the recording of the data, name and time taken for user to complete the game. Additionally, it determines whether the player has completed the game in time or not. The data is printed in an external file. 
***** the scenario of the game is set as stop and clean time, 13:10, and the program displays the time taken, as well as the time in reference to 13:10

## Test plan

| Description                                                      | Type                | Inputs                                                                                                             | Expected output                                                                                                                                                                                                              |
|------------------------------------------------------------------|---------------------|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Testing the confirm user input system                            | Unit testing        | Enter: "Nagisa" "11" "Mr. Osorio"                                                                                  | Text asking:  "Is your name Nagisa?" "Is your grade 11?" "Is your advisor Mr. Osorio?" If all output questions answered "yes": Proceed with the game If answered "no": The user is asked to renter their initial information |
| Testing whether the whole MVP sections are functional altogether | Integration testing | Inputs of all listed sections: User information input Location input Item obtainment input Inventory opening input | The user is clearly notified the success/failures of the game Whether, user successfully completes the game or not,  the time taken is measured and stated The users name and time is displayed in database                  |
| Clear headings and guiding comments in the code                  | Code review         | -                                                                                                                  | Clear heading at the top of each function/section Guiding comments on every change in situation/location of the game                                                                                                         |

## Record of Tasks
| Task No |               Planned Action               |                                                    Planned Outcome                                                    | Time estimate | Target completion date | Criterion |
|:-------:|:------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|:-------------:|:----------------------:|:---------:|
| 1       | create system diagram                      | to have a clear idea of the hardware and software requirements for the proposed solution                              | 20mins        | Sep 24                 | B         |
| 2       | Plan problem definition                    | The client is identified, and the reason for the program development is described.                                    | 30mins        | Oct 1                  | A         |
| 3       | Proposed solution rationale                | The design statement is clearly identified with justification for the decisions made for the creation of the program. | 30mins        | Oct 2                  | A         |
| 4       | Success criteria                           | Have six factors that determine the success of the final product                                                      | 30mins        | Oct 5                  | A         |
| 5       | Paste all Criteria A information on GitHub | All three areas of Criteria A is posted on GitHub, in the correct location                                            | 30 mins       | Oct 5                  | -         |
| 6       | Plan MVP                                   | Have concrete plan on which section of game will be used as MVP                                                       | 10 mins       | Oct 15                 | B         |
| 7       | Code MVP                                   | Program and complete the MVP, then test MVP until functional                                                          | 180 mins      | Oct 17 - Oct 21        | B         |
| 8       | Check MVP with someone                     | Find someone to check and try out the MVP to get feedback                                                             | 30 mins       | Oct 22                 | C         |
| 9       | Review and correct MVP                     | Make necessary adjustments derived from the feedback and errors                                                       | 60 mins       | Oct 22                 | C         |
| 10      | Selection of flow chart sections           | Depict three appropriate sections to draw the flow charts                                                             | 20 mins       | Oct 23                 | B         |
| 11      | Draw Flow diagram                          | Draw the three flow charts                                                                                            | 40 mins       | Oct 23                 | B         |
| 12      | Film 3 minute video on MVP                 | Have a detailed explanation video about the MVP                                                                       | 60 mins       | Oct 24                 | B         |
| 13      | Test plan table                            | Have the test plan table completed (unit testing, integration testing and code review)                                | 60 mins       | Oct 25                 | B         |
| 14      | All criteria B resources posted on Github  | All areas of criteria B are posted on Github, in the right location and format                                        | 30 mins       | Oct 25                 | -         |
| 15      | Confirm requirements (success criteria)    | Check whether all six criteria listed are met in the code, if not make necessary adjustments                          | 30 mins       | Oct 25                 | C         |
| 16      | Paste MVP code on Github                   | Post the code on Github at the very end of the page.                                                                  | 10 mins       | Oct 26                 | -         |
| 17      | Review all submissions on the Github page  | Have all necessary information in the page, organized and finalized                                                   | 30 mins       | Oct 26                 | -         |



### MVP code

Refer to file:
adventure_game.py in this repository.



