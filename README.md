# Squash

A simple single-player squash game written in **Python** using **Pygame**.

The objective is to keep the ball in play for as long as possible. The ball bounces off the walls, and the paddle changes its direction depending on where it is hit. Missing the ball ends the game, after which you can restart instantly.

This project was created as a way to learn Python, Pygame, collision detection, game loops, sprite handling, and basic game physics.

---

## Features

- Single-player squash gameplay
- Smooth paddle movement using delta time
- Randomized ball bounce angles
- Collision detection using `pygame.Rect`
- Game Over screen
- Instant restart without closing the game
- Custom sprites and window icon
- Compatible with both Python and PyInstaller executables

---

## Controls

| Key | Action |
|------|--------|
| **W** or **↑** | Move paddle up |
| **S** or **↓** | Move paddle down |
| **R** | Restart after Game Over |
| **Close Window** | Quit the game |

---

## Requirements

- Python 3.10 or newer
- **uv**

If you don't already have `uv` installed:

```bash
pip install uv
```

---

## Running the Game

Clone the repository:

```bash
git clone <repository-url>
cd Squash
```

Synchronize the virtual environment:

```bash
uv sync
```

Run the game:

```bash
uv run main.py
```

---

## Project Structure

```
Squash/
│
├── main.py
├── pyproject.toml
├── uv.lock
├── Assets/
│   ├── ball.png
│   ├── paddle.png
│   ├── floor.png
│   ├── gameover.png
│   └── icon.ico
├── README.md
└── LICENSE
```

---

## Building an Executable

```bash
uv run pyinstaller --onefile --windowed --add-data "Assets;Assets" main.py
```

The executable will be created in the `dist` folder.

---

## Future Improvements

- Score counter
- High score saving
- Increasing difficulty over time
- Sound effects and background music
- Particle effects
- Main menu
- Pause menu
- AI opponent
- Multiple difficulty levels
- Improved paddle physics

---

## Credits

Created by **PAPEET2785**

Built using **Python** and **Pygame**.