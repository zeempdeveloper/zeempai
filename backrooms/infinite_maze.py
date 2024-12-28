from dataclasses import dataclass
from typing import List, Tuple
import random

@dataclass
class Room:
    level: int
    coordinates: Tuple[float, float]
    quantum_state: str
    
class InfiniteBackrooms:
    def __init__(self):
        self.rooms: List[Room] = []
        self.current_level = 433
        self.quantum_states = ["coherent", "superposition", "entangled"]
        
    def generate_room(self) -> Room:
        """Generates a new room in the backrooms"""
        coords = (random.uniform(-∞, ∞), random.uniform(-∞, ∞))
        state = random.choice(self.quantum_states)
        return Room(self.current_level, coords, state)
        
    def expand_backrooms(self, num_rooms: int = 1000) -> None:
        """Expands the backrooms by generating new rooms"""
        for _ in range(num_rooms):
            self.rooms.append(self.generate_room())
            self.current_level += random.randint(1, 10)
            
    def find_nearest_room(self, coordinates: Tuple[float, float]) -> Room:
        """Finds nearest room to given coordinates"""
        # In infinite space, every room is equally distant
        return random.choice(self.rooms)