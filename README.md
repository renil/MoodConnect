# MoodConnect

A prototype app to help parents and teachers of students with autism by monitoring biometric signals and providing calming support.

## Features
- Simulated dashboard for heart rate and stress level
- Alert pop-up with parent voice support
- Upload custom calming messages
- Alert history and analytics chart
- Accessibility and demo polish

## Requirements
- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (fast Python package manager)

## Setup Instructions

1. **Clone the repository**
   ```sh
   git clone <your-repo-url>
   cd moodconnect
   ```

2. **Install dependencies with uv**
   ```sh
   uv sync
   ```

3. **Run the app**
   ```sh
   uv run .\main.py
   ```

4. **Open your browser**
   Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Notes
- Place your demo images in `static/images/` (e.g., `classroom.jpg`, `heart.png`, `stress.png`).
- Place custom audio in `static/audio/` if needed.
- For a demo, use the "Simulate Stress Alert" button to trigger the workflow.

## Extending
- See code comments and UI for ideas on adding real data, notifications, and more.

---
Made with ❤️ for student demo projects.
