from a2_support import *

# Write your classes here
class Tile:
    """
    Represents a generic tile in the Sokoban game. This class serves as the base class for otherspecific tile types. 
    """

    def is_blocking(self) -> bool:
        """
        Indicates if the tile is blocking or not.

        Returns:
        bool: False for the base Tile class since it's not blocking by default.
        """
        return False

    def get_type(self) -> str:
        """
        Retrieves the type of the tile.

        Returns:
        str: A string representation of the tile's type.
        """
        return 'Abstract Tile'

    def __str__(self) -> str:
        """
        Provides a string representation of the tile.

        Returns:
        str: The type of the tile.
        """
        return self.get_type()

    def __repr__(self) -> str:
        """
        Provides the "official" string representation of the tile, useful for debugging.

        Returns:
        str: The string representation of the tile.
        """
        return self.__str__()

class Floor(Tile):
    """
    Represents a floor tile in the Sokoban game. Inherits from the Tile class.
    """

    def get_type(self) -> str:
        """
        Returns the type of the tile.

        Returns:
        - str: Type of the tile.
        """
        return FLOOR

class Wall(Tile):
    """
    Represents a wall tile in the Sokoban game. Inherits from the Tile class.
    """

    def is_blocking(self) -> bool:
        """
        Indicates if the tile is blocking.

        Returns:
        - bool: True if the tile is blocking, False otherwise.
        """
        return True
    
    def get_type(self) -> str:
        """
        Returns the type of the tile.

        Returns:
        - str: Type of the tile.
        """
        return WALL
    
class Goal(Tile):
    """
    Represents a goal tile in the Sokoban game. Inherits from the Tile class.
    """

    def __init__(self) -> None:
        """
        Initializes the goal tile with its state set to False.
        """
        self.state = False

    def get_type(self) -> str:
        """
        Returns the type of the tile.

        Returns:
        - str: Type of the tile.
        """
        return GOAL
    
    def __str__(self) -> str:
        """
        Returns a string representation of the tile based on its state.

        Returns:
        - str: Type of the tile based on its state.
        """
        if self.state == False:
            return GOAL
        else:
            return FILLED_GOAL
    
    # Not rewriting the repr method since it references str.

    def is_filled(self) -> bool:
        """
        Indicates if the goal tile is filled.

        Returns:
        - bool: True if the tile is filled, False otherwise.
        """
        return self.state
    
    def fill(self) -> None:
        """
        Fills the goal tile by setting its state to True.
        """
        self.state = True


class Entity():
    """
    Represents a base entity in the Sokoban game.
    """

    def get_type(self) -> str:
        """
        Returns the type of the entity.

        Returns:
        - str: Type of the entity. Default is 'Abstract Entity'.
        """
        return 'Abstract Entity'
    
    def is_movable(self) -> bool:
        """
        Indicates if the entity is movable.

        Returns:
        - bool: True if the entity is movable, False otherwise. Default is False.
        """
        return False
    
    def __str__(self) -> str:
        """
        Returns a string representation of the entity.

        Returns:
        - str: Type of the entity.
        """
        return self.get_type()
    
    def __repr__(self) -> str:
        """
        Returns a formal string representation of the entity.

        Returns:
        - str: Type of the entity.
        """
        return self.__str__()


class Crate(Entity):
    """
    Represents a crate entity in the Sokoban game which requires a certain strength to move.
    """

    def __init__(self, strength: int) -> None:
        """
        Initializes a crate entity with the specified strength.

        Parameters:
        - strength (int): The strength required to move the crate.
        """
        self.strength = strength

    def get_strength(self) -> int:
        """
        Returns the strength required to move the crate.

        Returns:
        - int: The strength of the crate.
        """
        return self.strength

    def is_movable(self) -> bool:
        """
        Indicates if the crate is movable.

        Returns:
        - bool: True, since crates are always movable.
        """
        return True
    
    def get_type(self) -> str:
        """
        Returns the type of the crate.

        Returns:
        - str: Type of the crate. Defined by CRATE constant.
        """
        return CRATE
    
    def __str__(self) -> str:
        """
        Returns a string representation of the crate.

        Returns:
        - str: The strength of the crate as a string.
        """
        return str(self.strength)
    
    # Not rewriting repr since it references str.

class Potion(Entity):
    """
    Represents a potion entity in the Sokoban game. 
    This is an abstract class for different types of potions, providing a base structure.
    """

    def get_type(self) -> str:
        """
        Returns the type of the entity.

        Returns:
        - str: Always returns 'Potion' for this class.
        """
        return 'Potion'
    
    def effect(self) -> dict[str, int]:
        """
        Represents the effect of the potion when consumed by the player. 
        Since this is an abstract class, the base effect is an empty dictionary.
        
        Returns:
        - dict[str, int]: An empty dictionary representing no effect.
        """
        return {}
    
class StrengthPotion (Potion):
    """
    Represents a Strength Potion entity in the Sokoban game.
    When consumed, it increases the player's strength.
    """

    def get_type(self) -> str:
        """
        Returns the type of the entity.

        Returns:
        - str: Always returns 'STRENGTH_POTION' for this class.
        """
        return STRENGTH_POTION

    def effect(self) -> dict[str, int]:
        """
        Represents the effect of the Strength Potion when consumed by the player. 
        This potion increases the player's strength by 2.
        
        Returns:
        - dict[str, int]: Dictionary detailing the effect on the player's strength.
        """
        return {'strength': 2}
    
class MovePotion (Potion):
    """
    Represents a Move Potion entity in the Sokoban game.
    When consumed, it increases the number of moves available to the player.
    """

    def get_type(self) -> str:
        """
        Returns the type of the entity.

        Returns:
        - str: Always returns 'MOVE_POTION' for this class.
        """
        return MOVE_POTION
    
    def effect(self) -> dict[str, int]:
        """
        Represents the effect of the Move Potion when consumed by the player. 
        This potion grants the player an additional 5 moves.
        
        Returns:
        - dict[str, int]: Dictionary detailing the effect on the player's moves.
        """
        return {'moves':5}
    
class FancyPotion (Potion):
    """
    Represents a Fancy Potion entity in the Sokoban game.
    When consumed, it increases both the player's strength and moves.
    """

    def get_type(self) -> str:
        """
        Returns the type of the entity.

        Returns:
        - str: Always returns 'FANCY_POTION' for this class.
        """
        return FANCY_POTION
    
    def effect(self) -> dict[str, int]:
        """
        Represents the effect of the Fancy Potion when consumed by the player.
        This potion grants the player an additional 2 strength points and 2 moves.
        
        Returns:
        - dict[str, int]: Dictionary detailing the effects on the player's strength and moves.
        """
        return {'strength': 2, 'moves':2}
        
class Player(Entity):
    """
    Represents the main player character in the game.
    
    Attributes:
    - start_strength (int): Initial strength of the player.
    - moves_remaining (int): Moves remaining for the player.
    """

    def __init__(self, start_strength: int, moves_remaining: int) -> None:
        """
        Initialize the Player with given strength and moves.
        
        Parameters:
        - start_strength (int): Initial strength value.
        - moves_remaining (int): Initial number of moves.
        """
        self.start_strength = start_strength
        self.moves_remaining = moves_remaining

    def get_type(self) -> str:
        """Returns the type of the entity, in this case, PLAYER."""
        return PLAYER
    
    def is_movable(self) -> bool:
        """
        Determines if the player can move based on remaining moves.

        Returns:
        bool: True if player has moves left, otherwise False.
        """
        return self.moves_remaining > 0
    
    def get_strength(self) -> int:
        """Returns the current strength of the player."""
        return self.start_strength
    
    def add_strength(self, amount: int) -> None:
        """Adds the specified amount to the player's strength."""
        self.start_strength += amount

    def get_moves_remaining(self) -> int:
        """Returns the number of moves remaining for the player."""
        return self.moves_remaining
    
    def add_moves_remaining(self, amount: int) -> None:
        """Adds the specified amount to the player's remaining moves."""
        self.moves_remaining += amount

    def apply_effect(self, potion_effect: dict[str, int]) -> None:
        """
        Applies the effects of a potion to the player.
        
        Parameters:
        - potion_effect (dict): Dictionary with effects to be applied. 
        Supported keys: 'strength' and 'moves'.
        """
        for effect_type, adjustment in potion_effect.items():

            if effect_type == 'strength':
                self.add_strength(adjustment)
                
            elif effect_type == 'moves':
                self.add_moves_remaining(adjustment)


def convert_maze(game: list[list[str]]) -> tuple[Grid, Entities, Position]:
    """
    Converts a 2D list representation of a game into a more structured format.
    
    Parameters:
    - game (list[list[str]]): 2D list representation of a maze game.
    
    Returns:
    tuple[Grid, Entities, Position]: 
    - Grid: A 2D list of Tile objects representing the maze.
    - Entities: A dictionary mapping positions to Entity objects.
    - Position: A tuple representing the player's starting position.
    
    Example:
    >>> game = [['W', 'W', 'W'], 
    ...         ['W', 'P', 'W'], 
    ...         ['W', ' ', 'W']]
    >>> convert_maze(game)
    ([[Wall, Wall, Wall], [Wall, Floor, Wall], [Wall, Floor, Wall]], {(1, 1): Player()}, (1, 1))
    """
    maze = []
    entities = {}
    player_position = (0,0)

    for row_index, row in enumerate(game):
        maze_row = []

        for column_index, column in enumerate(row):
            position = (row_index, column_index)
            cell = game[row_index][column_index]

            # Handling Walls
            if cell == WALL:
                maze_row.append(Wall())
            
            # Handling Goals
            elif cell == GOAL:
                maze_row.append(Goal())

            # Handling Floors
            elif cell == FLOOR:
                maze_row.append(Floor())
            
            # Handling Player's Position
            elif cell == PLAYER:
                player_position = position
                maze_row.append(Floor())

            # Handling Potions
            elif cell == STRENGTH_POTION:
                entities[position] = StrengthPotion()
                maze_row.append(Floor())
            
            elif cell == MOVE_POTION:
                entities[position] = MovePotion()
                maze_row.append(Floor())

            elif cell == FANCY_POTION:
                entities[position] = FancyPotion()
                maze_row.append(Floor())

            # Handling Crates
            else:
                entities[position] = Crate(int(cell))
                maze_row.append(Floor())


        maze.append(maze_row)
    

    return (maze, entities, player_position)


class SokobanModel:
    """
    Represents the model for the Sokoban game, managing game state and logic.
    """

    def __init__(self, maze_file: str) -> None:
        """
        Initializes the Sokoban model by reading maze configurations from a file.

        Parameters:
        - maze_file (str): Path to the file containing maze configurations.
        """
        raw_maze, player_stats = read_file(maze_file)
        maze, entities, player_position = convert_maze(raw_maze)
        self.maze = maze
        self.entities = entities
        self.player_position = player_position
        self.player_strength, self.player_moves = player_stats

    def get_maze(self) -> Grid:
        """
        Returns the current state of the maze.
        
        Returns:
        Grid: A 2D list of Tile objects representing the current maze state.
        """
        return self.maze
    
    def get_entities(self) -> Entities:
        """
        Returns the entities currently present in the maze.

        Returns:
        Entities: A dictionary mapping positions to Entity objects.
        """
        return self.entities
    
    def get_player_position(self) -> tuple[int, int]:
        """
        Returns the current position of the player in the maze.

        Returns:
        tuple[int, int]: A tuple representing the player's current position.
        """
        return self.player_position
    
    def get_player_moves_remaining(self) -> int:
        """
        Returns the number of moves remaining for the player.

        Returns:
        int: Number of moves left for the player.
        """
        return self.player_moves
    
    def get_player_strength(self) -> int:
        """
        Returns the current strength of the player.

        Returns:
        int: Player's current strength.
        """
        return self.player_strength
    
    def attempt_move(self, direction: str) -> bool:
        """
        Attempts to move the player in the specified direction.

        Parameters:
        - direction (str): Direction to move the player in (UP, DOWN, LEFT, RIGHT).

        Returns:
        bool: True if the move was successful, False otherwise.
        """

        # Helper functions for move logic

        def add_tuple(tuple1: tuple, tuple2: tuple) -> tuple: 
            """
            Adds two tuples element-wise.

            Parameters:
            - tuple1 (tuple): First tuple.
            - tuple2 (tuple): Second tuple.

            Returns:
            tuple: Resulting tuple after element-wise addition.
            """
            return tuple(a + b for a, b in zip(tuple1, tuple2))

        def player_move() -> tuple:
            """
            Computes the player's new position after a move.

            Returns:
            tuple: Player's new position after the move.
            """
            return add_tuple(self.player_position, DIRECTION_DELTAS[direction])

        def index_check(position: tuple) -> bool:
            """
            Checks if a given position is valid within the maze boundaries and not a wall.

            Parameters:
            - position (tuple): Position to check.

            Returns:
            bool: True if position is valid, False otherwise.
            """
            row, col = position
            if not (0 <= row < len(self.maze) and 0 <= col < len(self.maze[row])):
                return False
            tile = self.maze[row][col]
            if tile.get_type() == WALL:
                return False
            return True

        def change_key(d: dict, old_key, new_key) -> dict:
            """
            Changes a key in a dictionary to a new key.

            Parameters:
            - d (dict): Dictionary to modify.
            - old_key: Key to be changed.
            - new_key: New key to replace the old key.

            Returns:
            dict: Modified dictionary.
            """
            if old_key in d:
                d[new_key] = d[old_key]
                del d[old_key]
            return d

        def check_potion(position: tuple) -> None:
            """
            Checks for and applies effects of a potion at a given position.

            Parameters:
            - position (tuple): Position to check for a potion.
            """
            potion = self.entities.get(position)
            if potion and potion.get_type() in [STRENGTH_POTION, MOVE_POTION, FANCY_POTION]:
                effects = potion.effect()
                self.player_strength += effects.get('strength', 0)
                self.player_moves += effects.get('moves', 0)
                del self.entities[position]

        # Validate movement direction
        movements = [UP, DOWN, LEFT, RIGHT]
        if direction not in movements:
            return False

        # Calculate new position
        new_position = player_move()
        if not index_check(new_position):
            return False

        # Handle interactions with entities
        entity = self.entities.get(new_position)
        if entity and entity.get_type() == CRATE:
            crate_new_position = add_tuple(new_position, DIRECTION_DELTAS[direction])
            
            # Ensure crate can be pushed to the new position
            if not index_check(crate_new_position):
                return False
            if crate_new_position in self.entities:
                return False
            if self.player_strength < entity.get_strength():
                return False
            
            # Move crate to new position
            change_key(self.entities, new_position, crate_new_position)
            
            # Handle crate reaching a goal
            row, col = crate_new_position
            if self.maze[row][col].get_type() == GOAL:
                self.maze[row][col].fill()
                del self.entities[crate_new_position]

        # Apply potion effects if applicable
        check_potion(new_position)

        # Update player's position and decrease the number of moves remaining
        self.player_position = new_position
        self.player_moves -= 1
        return True

    def has_won(self) -> bool:
        """
        Checks if the player has won the game.

        Returns:
        bool: True if all goals are filled, False otherwise.
        """
        # Check if all goals are filled
        for row in self.maze:
            for tile in row:
                if tile.get_type() == GOAL:
                    if tile.is_filled() == False:
                        return False              
        return True

class Sokoban: 
    """
    Represents the main Sokoban game controller class.
    Facilitates communication between the model and the view and handles user input.
    """

    def __init__(self, maze_file: str) -> None:
        """
        Initializes the Sokoban game with given maze file.

        Parameters:
        - maze_file (str): The path to the maze file to be loaded.
        """
        self.model = SokobanModel(maze_file)
        self.view = SokobanView()

    def display(self) -> None:
        """
        Displays the current state of the game, including the maze, entities, player stats, etc.
        """
        # Setting up the variables for ease of use
        maze = self.model.get_maze()
        entities = self.model.get_entities()
        position = self.model.get_player_position()
        moves = self.model.get_player_moves_remaining()
        strength = self.model.get_player_strength()

        # Display game state and player stats
        self.view.display_game(maze, entities, position)
        self.view.display_stats(moves, strength)

    def play_game(self) -> None:
        """
        The main game loop. Continues until the game is won, lost, or the player quits.
        """

        while True:

            # Check if player has won or lost
            if self.model.has_won():
                self.display()
                print("You won!")
                return

            elif self.model.get_player_moves_remaining() == 0:
                print("You lost!")
                return
            
            # Display game state and prompt user for a move
            self.display()
            move = input("Enter move: ")

            # Exit game if user enters 'q'
            if move == 'q':
                return
            elif not self.model.attempt_move(move):
                print("Invalid move\n")


def main():
    """
    The primary entry point for the Sokoban game.
    Initializes the game with a specified maze file and starts the game loop.
    """

    # Initialize the Sokoban game with the specified maze file
    game = Sokoban('maze_files/maze2.txt')

    # Start the game loop
    game.play_game()
    

if __name__ == '__main__':
    main()
