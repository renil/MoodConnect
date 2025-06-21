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


### The Goal for This Week: The "Wizard of Oz" Prototype

The students should **not** try to build the real technology this week. Instead, they should build a prototype that *simulates the user experience*. This is called a "Wizard of Oz" prototype: it looks like a fully functional app to the user, but behind the scenes, a human (or a simple script) is pulling the levers.

The aim is to **tell a convincing story** of how the app would work and show its value, not to build the actual prediction engine.

---

### Part 1: The Bare Minimum Plan for a 1-Week Prototype

**Core Concept:** A simple web-based dashboard that fakes all the complex parts. A web app is much faster to prototype than a native mobile app.

**Technology Stack (Choose the easiest):**
*   **No-Code/Design Tool:** **Figma.** They can build a fully interactive, clickable mockup that looks and feels exactly like a real app. This is the **highly recommended** approach for a 1-week deadline. It requires zero coding.
*   **Simple Web Code:** **HTML, CSS, and basic JavaScript.** This is for students who want to write some code. They can use a framework like Bootstrap to make it look good quickly.

---

### The 7-Day Plan:

**Day 1-2: Storyboarding and Design**
*   **Goal:** Define the exact user journey you want to demonstrate.
*   **Tasks:**
    1.  **Map it out:** On a whiteboard or paper, draw the screens. Who is the user? A parent checking in. What do they see?
    2.  **Screen 1: The Dashboard.** This is the main screen. It should have:
        *   A box for "Live Video Feed" (this will be a static image or a pre-recorded, looped video).
        *   A section for "Biometric Data" with widgets for:
            *   Heart Rate (e.g., "85 bpm")
            *   Stress Level (e.g., a gauge showing "Calm")
            *   Activity Level (e.g., "Low")
    3.  **Screen 2: The Alert.** What happens when the app predicts a mood change?
        *   A prominent pop-up or notification appears: **"ALERT: High Stress Levels Detected for [Child's Name]. Possible Overstimulation."**
    4.  **Screen 3: The Intervention.** What can the parent do?
        *   The alert screen should have a button: **"Play Calming Message."**
    5.  **Create Assets:**
        *   Find a stock photo or short, generic video of a classroom.
        *   Record a simple audio message on a phone: "Hey sweetie, it's Dad. Remember to take a deep breath. You're doing great."

**Day 3-4: Build the Static UI**
*   **Goal:** Create the look of the dashboard.
*   **Tasks (Figma):**
    *   Build the screens you designed. Use shapes, text, and placeholders. Import the classroom image. Make it look polished and real.
*   **Tasks (HTML/CSS):**
    *   Write the HTML to structure the page (divs for video, biometrics, etc.).
    *   Apply CSS to style it. Use a framework like Bootstrap to save time on buttons and layout. At this stage, nothing works yet—it's just a visual shell.

**Day 5: Add Simulated Interactivity**
*   **Goal:** Make the prototype feel dynamic.
*   **Tasks (Figma):**
    *   Use Figma's "Prototype" mode to link buttons to other screens. Clicking on a mock-up element will transition the user to the "Alert" artboard.
*   **Tasks (JavaScript):**
    1.  **Create a "Simulate Alert" button** (this button won't be in the final app, it's just for the demo).
    2.  Write a simple JavaScript function. When the "Simulate Alert" button is clicked:
        *   Change the "Stress Level" text to "High."
        *   Make the "Heart Rate" number jump up (e.g., to "120 bpm").
        *   Display the "ALERT" pop-up (which was hidden before).

**Day 6: Integrate the Intervention**
*   **Goal:** Make the support feature work. This is the one piece of *real* functionality they will build.
*   **Tasks (Figma):**
    *   On the "Alert" screen, link the "Play Calming Message" button to a new screen that says "Message Sent!" and maybe shows an audio waveform.
*   **Tasks (JavaScript):**
    1.  Add the pre-recorded audio file to your project folder.
    2.  Use the HTML `<audio>` tag.
    3.  Write a JavaScript function so that when the "Play Calming Message" button is clicked, the audio file plays.

**Day 7: Refine and Prepare Presentation**
*   **Goal:** Polish the demo and be ready to explain it.
*   **Tasks:**
    *   Clean up the UI. Check for typos.
    *   Practice the demonstration. The student presenting will navigate the prototype, click the "Simulate Alert" button, and explain what is happening: "Our algorithm has detected a pattern of rising heart rate and fidgeting from the video, predicting a meltdown."
    *   Prepare a 2-slide presentation:
        *   **Slide 1:** The Problem & Our Vision.
        *   **Slide 2:** The Future Roadmap (see Part 2 below).

---

### Part 2: The Plan for Extensibility (The Future Roadmap)

This is where they show they've thought beyond the one-week prototype. They should present this after their demo.

**Phase 1: Validating the Intervention (The Next 3-6 Months)**
*   **Goal:** Build a real, but simple, version to test the core idea: does a parent's voice help?
*   **Features:**
    *   **Manual Trigger:** Forget AI. Create a simple app for the teacher. The teacher sees a student is becoming dysregulated and presses a button in their app ("Alert Parent").
    *   **Parent Notification:** The parent gets a push notification on their phone.
    *   **Voice Library:** The parent can pre-record several messages ("deep breath," "quiet time," "good job focusing").
    *   **Remote Playback:** The parent can select a message, and it plays on a dedicated speaker or tablet in the classroom.
*   **Tech:** This requires a real mobile app (React Native or Flutter is good for cross-platform) and a simple backend (Firebase is perfect for this).

**Phase 2: Integrating Real Data (The Next 6-12 Months)**
*   **Goal:** Begin collecting the data needed for the AI model.
*   **Features:**
    *   **Wearable Integration:** Build the connection to the Apple HealthKit and Oura Ring APIs to pull real, live biometric data. This is a significant engineering challenge.
    *   **Data Logging:** Securely and ethically store this time-series data, linking it to the manual triggers from Phase 1. **Crucially, they must address data privacy and get parental consent (HIPAA/FERPA compliance).** This is a major hurdle.
    *   **Dashboard V2:** Display the *real* biometric data on the parent/teacher dashboard.

**Phase 3: Developing the Prediction Model (Year 2+)**
*   **Goal:** Build the "magic" they simulated in the prototype.
*   **Features:**
    *   **Initial ML Model:** Using the data collected in Phase 2, build a simple prediction model. Start with just one data source. For example: "Can we predict a teacher-reported event just from heart rate data?"
    *   **Multi-Modal AI:** This is the ultimate goal. Combine the biometric data stream with a video analysis stream (using computer vision to detect repetitive behaviors, facial expressions, etc.). This is a research-level problem that requires a massive, labeled dataset.
    *   **Personalization:** The model would need to be fine-tuned for each individual child, as autism is a spectrum and triggers are unique.

**Phase 4: Building an Ecosystem**
*   **Goal:** Expand beyond a simple alert system.
*   **Features:**
    *   **Analytics & Insights:** Provide parents and therapists with long-term trend reports. "We've noticed stress levels are highest during math class on Tuesdays."
    *   **Communication Tools:** Allow for secure, quick communication between the parent and teacher within the app.
    *   **Intervention Library:** Expand beyond voice messages to include visual aids, social stories, or connections to other therapeutic tools.

---
Made with ❤️ for student demo projects.
