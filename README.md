# Сheckers:
This is a game "Сheckers" which is operated using Python3 tkinter module.
To launch this game you can use pontoon 3.6 with the installed tinker module.
Available languages:Russian
# Rules:
Board size:8x8
Pieces per side:12
First move:White
Any sequence may be chosen, as long as all possible captures are made.
# Gameplay:
The moves are carried out on the left mouse button.
The menu is called up when you click on the right mouse button anywhere in the field.
In the menu you can turn on the map editing mode (Sandbox), saves (Сохранение),
and test version of the animation (Анимация (тестовая версия)).
Also in the settings menu, you can choose which AI or players will play for white and black checkers.
"Сложный ИИ" - Thinking over 4 moves ahead.
"Средний ИИ" - Thinking over 2 moves ahead.
"Простой ИИ" - Only thinks about his move.
"Рандом" - Selects a random move from all available.
"Применить настройки"-Applies all selected settings.
# Algorithm:
This game uses minmax algorithm to bruteforce all avalible steps for AI.
