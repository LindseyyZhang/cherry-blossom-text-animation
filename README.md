# 🌸 Cherry Blossom Text Animation

A poetic Python animation project that visualizes Chinese characters as leaves on a cherry blossom tree, gracefully falling with the wind.

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

## ✨ Features

- 🌳 **Recursive Tree Drawing** - Naturally growing tree structure with fractal branches
- 🍃 **Intelligent Text Layout** - Chinese characters precisely attached to branches, avoiding visual overlaps
- 💨 **Physics Wind Effects** - Press spacebar to trigger realistic wind simulation
- 🎯 **Gravity Simulation** - Text leaves fall naturally with rotation and air resistance
- 📜 **Ground Accumulation** - Fallen leaves randomly scatter on the ground creating poetic effects
- 🎨 **Visual Optimization** - Text with background layers, rich colors, and smooth animations

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- Built-in turtle library (Python standard library)

### Installation & Running

```bash
git clone https://github.com/LindseyyZhang/cherry-blossom-text-animation.git
cd cherry-blossom-text-animation
python cherry_text_animation.py
```

### VS Code Setup

1. Open project folder in VS Code
2. Right-click `cherry_text_animation.py`
3. Select "Run Python File in Terminal"

## 🎮 Controls

| Key | Function |
|-----|----------|
| **Spacebar** | Trigger wind effect, blow away text leaves |
| **R Key** | Reset scene, return all text to tree |
| **ESC Key** | Exit program |

## 📸 Screenshots

### Initial State
Cherry blossom tree with Chinese character leaves gently swaying
```
        🌸
       /   \
    春    花
   /  \    \  
  风   诗   美
```

### Wind Effect
After pressing spacebar, characters drift and fall
```
🌬️ Wind rises...
    📜 '春' (Spring) has fallen...
    📜 '花' (Flower) has fallen...
    📜 '风' (Wind) has fallen...
```

## 🎨 Cultural Background

This animation celebrates the beauty of **Chinese calligraphy** and **seasonal poetry**. Each character represents concepts from nature and classical literature:

- **春** (Spring) - The season of renewal
- **花** (Flower) - Natural beauty
- **风** (Wind) - Natural forces
- **诗** (Poetry) - Artistic expression
- **梦** (Dream) - Imagination

The falling leaves metaphor is deeply rooted in Chinese poetry, symbolizing the passage of time and the beauty of impermanence.

## 🛠️ Technical Implementation

### Core Algorithms

- **Recursive Tree Generation**: Fractal algorithm creates natural branching patterns
- **Position Filtering**: Smart avoidance of trunk area ensures text visibility
- **Physics Engine**: Simple simulation of gravity, air resistance, and wind forces
- **Animation Loop**: Smooth 60FPS animation with optimized rendering

### Code Structure

```python
class CherryBlossomTextAnimation:
    ├── __init__()              # Initialize animation
    ├── setup_canvas()          # Configure display
    ├── draw_branch()           # Recursive tree drawing
    ├── create_text_leaves()    # Generate text leaves
    ├── toggle_wind()           # Wind effect control
    ├── update_tree_leaves()    # Update attached text
    ├── update_falling_text()   # Update falling text
    └── run_animation()         # Main animation loop
```

## ⚙️ Customization

### Modify Text Content

Edit the texts list in `create_text_leaves()` method:

```python
texts = [
    "春", "夏", "秋", "冬",    # Four Seasons
    "诗", "书", "礼", "乐",    # Four Arts
    "琴", "棋", "书", "画"     # Four Refinements
]
```

### Adjust Color Scheme

```python
# Text colors
text_color = "#FF69B4"      # Pink
background_color = "#F0F8FF" # Light blue background

# Tree colors
trunk_color = "#8B4513"     # Brown trunk
branch_color = "#654321"    # Dark brown branches
```

### Modify Physics Parameters

```python
# Gravity strength
gravity = 0.05

# Wind strength  
wind_strength = 2.0

# Air resistance
air_resistance = 0.98
```

## 🔧 Troubleshooting

### Common Issues

**Q: Program closes immediately**
```python
# Add at the end of code:
input("Press Enter to exit...")
```

**Q: Animation is laggy**
```python
# Adjust refresh rate
time.sleep(0.03)  # Decrease for higher FPS
```

**Q: Too many/few characters**
```python
# Modify text list length or adjust branch density
if depth > 3 and random.random() < 0.4:  # Adjust probability
```

## 🎯 Future Improvements

- [ ] Background sound effects (wind, birds)
- [ ] Custom text input support
- [ ] Multiple tree shapes
- [ ] Seasonal variations
- [ ] Export animation as GIF
- [ ] Mobile app version

## 🤝 Contributing

Contributions are welcome! Please feel free to submit Issues and Pull Requests.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to Python Turtle library for graphics support
- Inspired by classical Chinese poetry and the imagery of falling leaves
- Special thanks to all friends who provided feedback and suggestions

---

**Making code poetic, making programs artistic** 🌸

*"Spring breeze crosses ten miles of Yangzhou road,*  
*Cherry blossoms dance full on the branches.*  
*Petals drift down to form poetry,*  
*Each character a spring, melody lingering."*