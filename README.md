---
title: Student Study Buddy
emoji: 📚
colorFrom: yellow
colorTo: green
sdk: gradio
sdk_version: 6.11.0
python_version: 3.12
app_file: app.py
pinned: false
---

## **Project Overview**
This project is an AI environment built using the **OpenEnv** framework. It simulates a student's study session where an agent must balance completing academic tasks with managing a dynamic "stress" level. The environment is designed to test how an AI can prioritize work based on deadlines and self-care.

## **Core Logic**
* **Task Management**: The environment tracks multiple tasks (e.g., Math, AI Project, Reading), each with its own priority and deadline.
* **Stress Variable**: Stress starts at **0.5** and naturally increases by **0.05** every turn.
* **Stress Management**: The agent can choose a `"rest"` action to lower stress by **0.2**.
* **Deadline Penalties**: Completing a task before its deadline yields a higher reward, while late tasks result in a penalty.



## **Scoring System**
The included `grader.py` evaluates the agent's performance based on two criteria:
1.  **Completion**: All 3 tasks must be finished for the highest score.
2.  **Health**: The final stress level must be below **0.5** to receive a perfect **1.0** score.

## **Installation & Usage**
To run this simulation locally:

1. **Clone the repository** and navigate to the folder.
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the simulation**:
   ```bash
   python main.py
   ```

## **File Structure**
* `env/environment.py`: Contains the `StudentEnv` class and the `step()` logic.
* `env/models.py`: Defines the Pydantic data structures for Tasks, Actions, and Observations.
* `env/grader.py`: The evaluation script for final performance.
* `main.py`: The entry point that runs the simulation loop.

---
