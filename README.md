Title: Football deflecting game!

Description: This project is a football game where you wwill be player as Liverpool against Manchestercity for 100 second real life(100 game minute).

How to install and play.
1. Click on code button on the top right in this repo.
2. Download as zip
3. Extract the zip file
4. Open it in virsual studio code or other python ide
5. CLick on the file main.py and click run

Project Demo video link:
https://youtu.be/t__Ac9AENqg

How to interact:
Use  "WASD" for movement of Liverpool player.
The square character in liverpool team is Mohamed Salah; he can move freely on the pitch. 
Moreover, he might randomly try to score a goal by change velocity of the ball to go toward mancity goal.
On the other hand other player in liverpool team cannot move freely as they have to follow mohamed salah and not leaving the pitch.
Don't worry about throw in as the ball will automatically throwed in.


Project design and implementation
![IMG_2395 (1)](https://github.com/user-attachments/assets/3ed7820e-87a4-45bd-97e7-eb84308e05cf)
There are in total of 8 classes for this game.
Event class is used to check all kind of collision event.
Footballer_Database is a class to store player data of every team.
FootballPlayer class is a class for drawing, initiating Mohamed Salah.
Gamedone class is use to do the end game when the time reach 100 real life second and stop the game.
main class is where most of the game mechanic is implemented wheter to be movement or collision.
Object is used to create other player and ball, calculate time to hit, and perform collision.
Score class is to check if the ball is enter a goal or not.
Timer is used to keep track of time to not make the game go over 100 second.

How are the event code modified:
The ball class is entirely changed to Object class to make it easy for collision event between ball and player.
Paddle class is change to FootballerPlayer and is a child class of Object.
The ball and wall collision is change a bit not only track if the ball is not none to hit wall, but also use code if ball if too fast and leave the wall and make a throw -in.
Paddle collision is entirely change to only detect if ball is with salah or not. Moreover the ball wont collide salah,
but will try to go to mancity goal and paddle predict is deleted as it is no longer needed.


Bug still to be resolved:
* The game is lagged so much as the game process and event are happening.
* Sometimes the ball does not collide with ball, but only deflect a little.
* Sometimes ball cannnot sense that it is near Mohamed Salah
