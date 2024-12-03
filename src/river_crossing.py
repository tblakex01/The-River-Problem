from enum import Enum
from typing import List, Set, Optional
from dataclasses import dataclass
from collections import deque

class Bank(Enum):
    LEFT = "left"
    RIGHT = "right"

class AnimalType(Enum):
    WOLF = "wolf"
    GOAT = "goat"
    CABBAGE = "cabbage"

@dataclass
class Animal:
    type: AnimalType
    location: Bank
    
    def can_eat(self, other: 'Animal') -> bool:
        if self.type == AnimalType.WOLF and other.type == AnimalType.GOAT:
            return True
        if self.type == AnimalType.GOAT and other.type == AnimalType.CABBAGE:
            return True
        return False

class GameState:
    def __init__(self):
        self.animals = {
            AnimalType.WOLF: Animal(AnimalType.WOLF, Bank.LEFT),
            AnimalType.GOAT: Animal(AnimalType.GOAT, Bank.LEFT),
            AnimalType.CABBAGE: Animal(AnimalType.CABBAGE, Bank.LEFT)
        }
        self.farmer_location = Bank.LEFT
        self.moves: List[str] = []
    
    def is_valid(self) -> bool:
        for animal in self.animals.values():
            if animal.location != self.farmer_location:
                for other in self.animals.values():
                    if (animal.location == other.location and 
                        animal.can_eat(other)):
                        return False
        return True
    
    def is_complete(self) -> bool:
        return all(animal.location == Bank.RIGHT 
                  for animal in self.animals.values())
    
    def get_possible_moves(self) -> List[Optional[AnimalType]]:
        moves = [None]  # Farmer can move alone
        for animal_type, animal in self.animals.items():
            if animal.location == self.farmer_location:
                moves.append(animal_type)
        return moves
    
    def make_move(self, animal_type: Optional[AnimalType]) -> None:
        new_bank = (Bank.RIGHT if self.farmer_location == Bank.LEFT 
                   else Bank.LEFT)
        
        # Move farmer
        self.farmer_location = new_bank
        
        # Move animal if one was selected
        if animal_type:
            self.animals[animal_type].location = new_bank
            
        # Record move
        move_str = f"Move farmer"
        if animal_type:
            move_str += f" with {animal_type.value}"
        move_str += f" to {new_bank.value} bank"
        self.moves.append(move_str)

class RiverCrossing:
    def solve(self) -> Optional[List[str]]:
        start_state = GameState()
        visited = set()
        queue = deque([(start_state, [])])
        
        while queue:
            current_state, path = queue.popleft()
            state_hash = self._hash_state(current_state)
            
            if state_hash in visited:
                continue
                
            visited.add(state_hash)
            
            if current_state.is_complete():
                return current_state.moves
                
            for move in current_state.get_possible_moves():
                new_state = self._clone_state(current_state)
                new_state.make_move(move)
                
                if new_state.is_valid():
                    queue.append((new_state, path + [move]))
        
        return None
    
    def _hash_state(self, state: GameState) -> str:
        return (f"{state.farmer_location.value}|" + 
                "|".join(f"{k.value}:{v.location.value}" 
                        for k, v in sorted(state.animals.items())))
    
    def _clone_state(self, state: GameState) -> GameState:
        new_state = GameState()
        new_state.farmer_location = state.farmer_location
        new_state.moves = state.moves.copy()
        for animal_type, animal in state.animals.items():
            new_state.animals[animal_type] = Animal(
                animal_type, animal.location)
        return new_state

def main():
    game = RiverCrossing()
    solution = game.solve()
    
    if solution:
        print("Solution found!")
        print("\nSteps to solve:")
        for i, move in enumerate(solution, 1):
            print(f"{i}. {move}")
    else:
        print("No solution found!")

if __name__ == "__main__":
    main()