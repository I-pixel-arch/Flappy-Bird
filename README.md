# 🐦 Flappy Bird AI

This is an AI-powered clone of the popular Flappy Bird game built using **Python**, **Pygame**, and the **NEAT (NeuroEvolution of Augmenting Topologies)** algorithm. The game simulates a population of birds learning to play Flappy Bird through evolution and neural networks.

![Flappy Bird AI Demo](preview.gif)

---

## 🎮 Features

- Fully playable **Flappy Bird clone** in Pygame
- **AI training** using NEAT (via `Train.py`)
- **Model evaluation** using a saved genome (via `Model.py`)
- Modular and readable Python code (Bird, Pipe, Base, Background, etc.)
- Score tracking, collision detection, and procedural pipe generation

---

## 🧠 How It Works

The AI learns to play the game by evolving a neural network using the NEAT algorithm:

- **Inputs to the network**:
  - Bird’s current Y position
  - Distance to top and bottom of the next pipe
- **Output**:
  - Whether the bird should jump

Fitness is rewarded for survival and pipe-passing.

---

## 🗂️ Project Structure

```
├── Bird.py           # Bird behavior & animation
├── Pipe.py           # Pipes and collision logic
├── Base.py           # Scrolling ground
├── Background.py     # Moving background
├── Environment.py    # Game constants & assets
├── Train.py          # NEAT training logic
├── Model.py          # Load and evaluate saved model
├── images/           # Game assets (bird, pipe, bg)
├── model             # Saved NEAT model
└── config-feedforward.txt  # NEAT configuration
```

---

## 🔧 Requirements

Install dependencies:

```bash
pip install pygame neat-python
```

Make sure you have an `images/` directory with:
- `bird1.png`, `bird2.png`
- `pipe.png`
- `bg.png`
- `base.png`

---

## 🚀 Running the Project

### 1. Train the AI
```bash
python Train.py
```
This starts the NEAT training loop. The best genome will be saved as `model`.

### 2. Run the Trained Model
```bash
python Model.py
```
This loads the saved model and lets it play the game using its trained neural network.

---

## 📄 NEAT Configuration

The NEAT config file (`config-feedforward.txt`) defines:
- Network structure
- Mutation rates
- Population size
- Compatibility threshold

You can tweak this to experiment with learning behavior.

---

## 📊 Fitness Evaluation

Each bird's fitness is determined by:
- Survival time (incremental reward)
- Passing through pipes (+5 reward)
- Crashing (-1 penalty)

---

## 📌 Controls (for manual play/testing)

> The AI plays automatically. No manual control needed.

However, in a manual version (if implemented), you'd typically use:
- `SPACE`: Make the bird jump

---

## 🧠 Acknowledgements

- NEAT algorithm: [neat-python](https://github.com/CodeReclaimers/neat-python)
- Game concept: *Flappy Bird* by Dong Nguyen

---

## 🪪 License

This project is open source under the MIT License.

---

## 🙌 Contribute

Feel free to fork, improve, or train new AI models. PRs are welcome!