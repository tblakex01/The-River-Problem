# 🚣 The River Problem 🌊

A Python implementation of the classic river crossing puzzle featuring a farmer trying to transport a wolf, a goat, and a cabbage across a river.

## 🎮 The Puzzle

A farmer needs to transport three items across a river:
- 🐺 Wolf
- 🐐 Goat
- 🥬 Cabbage

### Rules
- 🚣 The boat can only carry the farmer and at most one item
- 🐺 If left alone, the wolf will eat the goat
- 🐐 If left alone, the goat will eat the cabbage
- 🧑‍🌾 The farmer must be present for all river crossings

## 🛠️ Implementation

This solution features:
- Object-oriented design with proper encapsulation
- Type hints for better code clarity
- Breadth-first search algorithm for finding the optimal solution
- State validation to ensure no animals eat each other
- Comprehensive move tracking

## 🚀 Usage

```bash
python river_crossing.py
```

## 🧪 Output

The program will output a step-by-step solution showing how to safely transport all items across the river.

## 🏗️ Architecture

- `Bank`: Enum representing river banks
- `AnimalType`: Enum for different transportable items
- `Animal`: Dataclass representing an item with its current location
- `GameState`: Class managing the current state of the puzzle
- `RiverCrossing`: Main solver class implementing BFS algorithm

## 📝 License

MIT License