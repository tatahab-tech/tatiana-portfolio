# Super Mario Bros Style Platformer

A 2D platformer game built with JavaScript and Phaser.js that runs in the browser. Jump, collect coins, defeat enemies, and complete the level!

![Game Preview](https://img.shields.io/badge/Game-Platformer-green) ![Phaser.js](https://img.shields.io/badge/Phaser.js-3.70.0-blue) ![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)

## 🎮 How to Play

1. **Open the game**: Simply open `index.html` in your web browser
2. **Controls**:
   - **Arrow Keys**: Move left and right
   - **Spacebar**: Jump
   - **R Key**: Restart game (when game over)
3. **Objective**: Collect all gold coins to win the level
4. **Enemies**: Jump on enemies to defeat them, avoid touching them from the side

## 🚀 Quick Start

1. Clone or download this repository
2. Open `index.html` in any modern web browser
3. Start playing immediately - no installation required!

## 🎯 Game Features

### Core Mechanics
- **Player Movement**: Smooth left/right movement with arrow keys
- **Jumping**: Physics-based jumping with spacebar
- **Collision Detection**: Realistic platform and enemy interactions
- **Gravity**: Authentic platformer physics

### Game Elements
- **Platforms**: Multiple platforms to navigate
- **Enemies**: Moving enemies that can be defeated by jumping on them
- **Coins**: Collectible gold coins worth 10 points each
- **Score System**: Track your progress with a scoring system
- **Win/Lose Conditions**: Clear objectives and game over states

### Visual Design
- **Modern UI**: Beautiful gradient background and glass-morphism design
- **Color-Coded Elements**: 
  - 🔴 Red player character
  - 🟤 Brown enemies
  - 🟡 Gold coins
- **Responsive Layout**: Centered game container with instructions

## 📁 Project Structure

```
cursor tutorial/
├── index.html          # Main HTML file with Phaser.js CDN
├── styles.css          # Game styling and UI design
├── game.js            # Complete game logic and mechanics
└── README.md          # This documentation file
```

## 🛠️ Technical Details

### Dependencies
- **Phaser.js 3.70.0**: Game framework loaded via CDN
- **Modern Browser**: Chrome, Firefox, Safari, or Edge

### Game Configuration
- **Canvas Size**: 800x600 pixels
- **Physics Engine**: Arcade physics with gravity
- **Framerate**: 60 FPS (browser dependent)

### Key Components
- **Player Character**: Physics-enabled sprite with movement and jumping
- **Platform System**: Static collision platforms
- **Enemy AI**: Simple back-and-forth movement
- **Collectible System**: Coin collection with score tracking
- **Game State Management**: Win/lose conditions and restart functionality

## 🎨 Customization

### Adding New Levels
1. Modify the `create()` function in `game.js`
2. Add new platforms using `platforms.create()`
3. Position enemies and coins with `enemies.create()` and `coins.create()`

### Changing Visuals
1. Replace colored rectangles with actual sprite images
2. Modify colors in the `setTint()` calls
3. Update the background gradient in `styles.css`

### Adding New Features
- **Power-ups**: Add new collectible types
- **Sound Effects**: Integrate Phaser audio
- **Multiple Levels**: Create level progression system
- **Player Animations**: Add sprite animations
- **More Enemy Types**: Create different enemy behaviors

## 🐛 Troubleshooting

### Common Issues
- **Game not loading**: Ensure you're opening `index.html` in a web browser, not a text editor
- **Controls not working**: Make sure the game canvas has focus (click on it)
- **Performance issues**: Try refreshing the page or using a different browser

### Browser Compatibility
- **Chrome**: ✅ Fully supported
- **Firefox**: ✅ Fully supported
- **Safari**: ✅ Fully supported
- **Edge**: ✅ Fully supported

## 📝 Development Notes

This game was built as a learning project to demonstrate:
- Phaser.js game development
- 2D platformer mechanics
- Physics-based gameplay
- Game state management
- Modern web development practices

The game uses simple colored rectangles instead of sprite images to keep it lightweight and easy to understand. This makes it perfect for learning game development concepts!

## 🤝 Contributing

Feel free to fork this project and add your own features:
- New enemy types
- Power-ups and special abilities
- Multiple levels
- Sound effects and music
- Better graphics and animations

## 📄 License

This project is open source and available under the MIT License.

---

**Have fun playing!** 🎮✨
