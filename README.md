# Memory-Match-Pet-Simulator-Game
# 🐾 Memory Match & Pet Simulator Game

🎮 This project is a combination of two interactive games:

1. **Memory Card Game** – A classic card-flipping game that tests your memory.
2. **Pet Simulator** – A virtual pet game where you feed, play with, and clean your pet to keep it alive and happy.

Both games are built using Python and are playable in the terminal/console. The memory game challenges your brain, while the pet simulator adds a nurturing element to the gameplay experience.

---

## 🧩 Features

### Memory Card Game

* Simple text-based matching game.
* Randomized card layout.
* Turn-based system.
* Match all pairs to win.

### Pet Simulator

* Name your own pet at the start.
* Real-time stat tracking: hunger, happiness, cleanliness, and age.
* Choose actions each day: feed, play, clean.
* Pet dies if hunger reaches 10 or cleanliness drops to 0.
* Infinite days until pet dies.

---

## 🕹️ How to Play

### Pet Simulator

1. On start, input your pet's name.
2. Each day, choose one action:

   * `feed`: Reduces hunger
   * `play`: Increases happiness, slightly increases hunger
   * `clean`: Increases cleanliness
3. Stats update at the end of each day.
4. Game continues until pet dies from hunger or dirtiness.

### Memory Card Game

1. A set of hidden pairs is displayed.
2. Enter coordinates (e.g., 0 1, 2 2) to flip two cards.
3. "0" refers to the first row or column.
4. If they match, they stay revealed.
5. Match all pairs to win.

---

## 📁 Project Structure

```
games/
├── petsim.py                # Pet class and simulation logic
├── memcard.py               # Memory card game logic
├── memcardprompt.ipynb      # Memory card game prompt
├── petsimprompt.ipynb       # Pet Simulator game prompt
└── README.md                # Project description and guide
```

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

Inspired by classic Tamagotchi games and traditional card matching logic. Built to blend memory challenge with pet care fun.
