# 🐍 Snake Game - Python in Browser

A classic Snake game written in **pure Python with PyGame**, running directly in your browser using **Pyodide** (WebAssembly Python).

🌐 **Play Now:** [https://your-username.github.io/snake-game-python-web/](https://your-username.github.io/snake-game-python-web/)

## 🚀 How It Works

This project uses:
- **Pyodide**: Python compiled to WebAssembly that runs in the browser
- **PyGame**: Popular game library for Python
- **GitHub Pages**: Free hosting for static websites
- **JavaScript Bridge**: Communication between Python and browser APIs

## 🎮 Features

- 🐍 Classic Snake gameplay with smooth controls
- 🎨 Beautiful modern UI with responsive design
- 📱 Touch-friendly controls for mobile devices
- 📊 Real-time score tracking
- 🔄 Instant restart functionality
- ⚡ Adaptive speed increase as you score

## 🎯 How to Play

1. Use **Arrow Keys** or **on-screen buttons** to control the snake
2. Eat the **red food** to grow and earn points
3. Avoid hitting yourself
4. Press **R** to restart at any time
5. Speed increases every 50 points

## 🛠️ Local Development

1. Clone the repository:
```bash
git clone https://github.com/your-username/snake-game-python-web.git
cd snake-game-python-web
```

2. Open `index.html` in a modern browser

3. Or use a local server:
```bash
python -m http.server 8000
# Then visit http://localhost:8000
```

## 📁 Project Structure

```
snake-game-python-web/
├── index.html          # Main HTML file with UI and Pyodide setup
├── snake.py            # Python game logic using PyGame
├── README.md           # This file
└── .nojekyll           # Prevents Jekyll processing on GitHub
```

## 🔧 Technical Details

The game runs Python code directly in the browser through:
1. Pyodide loads Python 3.10 runtime as WebAssembly
2. Micropip installs PyGame from PyPI
3. JavaScript bridge handles input/output
4. Canvas API renders PyGame graphics

## 🚀 Deployment to GitHub Pages

1. Push code to GitHub repository
2. Go to Settings → Pages
3. Select "Deploy from branch"
4. Choose "main" branch and "/ (root)" folder
5. Your game will be live at: `username.github.io/snake-game-python-web`

## ⚠️ Limitations

- Initial load time: ~15-30 seconds (downloading Python runtime)
- Performance: Slower than native PyGame (WebAssembly overhead)
- Audio: PyGame audio might not work in browser

## 🤝 Contributing

Found a bug or have an improvement?
1. Fork the repository
2. Create a feature branch
3. Submit a Pull Request

## 📄 License

MIT License - feel free to use this for your own projects!

## 🙏 Acknowledgments

- [Pyodide](https://github.com/pyodide/pyodide) team for bringing Python to the browser
- [PyGame](https://www.pygame.org) community
- GitHub for free hosting
