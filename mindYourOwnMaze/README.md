# What the game must do:
This is a maze game where the world is a square grid. The player will start in 1 cell and can move one step at a time using the wasd keys. To win the player must find the item hidden in the grid. There are traps also hidden in cell around the grid. If the player steps on a trap it will reduce their health. There will be a search algorithem to give hints or solve the map completely. 

# Game rules:
Grid size:
- I will start with 5x5 grid 
- Starting health: 3
- Traps: 3
- movement keys: w,a,s,d
- Hint option
- I will use BFS for hints and full solve
- The full solve option will show if the player loses asking them if they want to see the solved map.
- Hope to add in a larger 8x8 sized grid that is more complex.

Plan for Data:
- grid → list of lists
- player_position → tuple → Where the player is on the grid. 
- item_position → tuple → Where the item is on the grid
- traps → list of tuples → Where each trap is on the grid
- health → integer → need whole numbers not float as they are not fixed
- game_running → boolean → simple true= is running false= not running. Good to show when running and initiate "shutdown" of the game

How grid will be shown:
- P for the player
- . for empty spaces
- traps only when stepped on, or keep them hidden until triggered
- hidden item should stay hidden until found
- only show the player and empty cells during play to avoid confusion
- reveal traps/item/health when it is found
- reveal everything at the end if the player wins or loses (ideally show a reveal button or ask if player wants to see this)

Program creation tasks:
1.	create the grid
2.	place the player
3.	place the hidden item
4.	place traps
5.	display the grid
6.	get player input
7.	move the player
8.	stop movement outside the grid
9.	check trap or item
10.	update health
11.	check win or loss
12.	add BFS or DFS hint feature

Suggested order to complete the assessment
Follow this order exactly:
1.	choose grid size and rules [Done]
2.	design the grid display [Done]
3.	implement player movement [Done]
4.	stop movement outside the map [Done]
5.	add hidden item and traps
6.	add health tracking
7.	add win and lose checks
8.	add BFS hint or solver
9.	test everything
10.	write your explanation