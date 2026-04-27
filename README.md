# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]

## Functionality

This project is an AI-assisted Game Glitch Investigator system. The system helps identify, explain, and verify bugs in a number guessing game. Instead of only fixing the game manually, the project includes a reliability testing system that checks whether the game logic gives consistent and correct responses.

The system supports:
- Debugging incorrect game behavior
- Separating game logic into reusable functions
- Running automated reliability tests
- Using guardrails to make sure guesses and results are handled safely
- Logging or tracking testing behavior for easier debugging

## AI Feature: Reliability and Testing System

This project includes a reliability testing system that evaluates whether the game responds correctly to different inputs. The tests check cases where the guess is correct, too low, or too high. This makes the system more reliable because it can verify that the logic still works after changes are made.

To run the reliability tests:

```bash
python reliability_tests.py

## System Diagram

```mermaid
flowchart TD
    A[User Input: Game Guess or Debug Request] --> B[Game Logic Module]
    B --> C[AI-Assisted Debug Explanation]
    C --> D[Output: Feedback and Bug Explanation]

    B --> E[Reliability Tester]
    E --> F[Test Results: Pass or Fail]

    F --> G[Human Review]
    D --> G

    G --> H[Improved Game System]

# Applied AI System: Game Glitch Investigator

## Title and Summary

The **Game Glitch Investigator** is an AI-assisted debugging system designed to analyze and verify the correctness of a number guessing game. This project enhances a simple game by integrating reliability testing and structured logic validation to ensure consistent and accurate behavior.

This system matters because it demonstrates how AI-inspired workflows can improve software reliability, automate debugging, and support decision-making in real-world applications.

---

## Original Project (Module 1)

This project is based on my original Module 1 project: **Game Glitch Investigator**.
The original goal was to debug a number guessing game by identifying incorrect logic and improving the game's response behavior. It focused on separating logic into reusable functions and ensuring correct outputs for user guesses.

---

## Architecture Overview

The system is composed of three main components:

* **Game Logic Module**: Handles user guesses and determines outcomes.
* **AI-Assisted Debug Layer**: Provides explanations for game behavior and potential issues.
* **Reliability Testing System**: Automatically evaluates correctness across multiple test cases.

Data flows through the system as follows:

User Input → Game Logic → AI Explanation → Output
Additionally, the Reliability Tester runs parallel checks to validate correctness, and results are reviewed before improving the system.

---

## System Diagram

```mermaid
flowchart TD
    A[User Input] --> B[Game Logic]
    B --> C[AI Explanation]
    C --> D[Output]

    B --> E[Reliability Tester]
    E --> F[Test Results]

    F --> G[Human Review]
    D --> G
```

---

## Setup Instructions

Follow these steps to run the project:

1. Clone the repository:

```bash
git clone https://github.com/nhibui32/applied-ai-system-project.git
cd applied-ai-system-project
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the main application:

```bash
python app.py
```

4. Run reliability tests:

```bash
python reliability_tests.py
```

---

## Sample Interactions

### Example 1

Input:

```
Guess: 5
Secret: 5
```

Output:

```
Correct!
```

### Example 2

Input:

```
Guess: 3
Secret: 5
```

Output:

```
Too low!
```

### Example 3

Input:

```
Guess: 8
Secret: 5
```

Output:

```
Too high!
```

---

## Design Decisions

* I separated the game logic into `logic_utils.py` to make the system modular and testable.
* I added a reliability testing system to ensure correctness across different scenarios.
* I chose a simple structure instead of adding complex AI models to focus on reliability and clarity.
* Trade-off: The system is not using advanced AI models (like RAG or agents), but it demonstrates strong reliability and testing practices.

---

## Testing Summary

The reliability testing system validates core game logic across multiple cases:

* Correct guesses
* Too high guesses
* Too low guesses

What worked:

* The modular design made testing straightforward.
* Automated tests ensured consistent outputs.

What didn’t:

* The system currently has limited test coverage.
* Edge cases (invalid input types) could be expanded further.

---

## Reflection

This project taught me how to transform a simple program into a more structured and reliable AI system. I learned the importance of testing, modular design, and building systems that are not only functional but also trustworthy.

It also helped me understand how AI systems require evaluation and validation, not just output generation. This experience strengthened my problem-solving skills and my ability to think about system design from a reliability perspective.

---

## Future Improvements

* Add more advanced AI features (e.g., automated debugging suggestions)
* Expand test coverage and edge case handling
* Introduce logging for better traceability
* Integrate a user interface for better interaction


## Testing Summary

The system includes an automated reliability testing module that evaluates the correctness of the game logic.

- 6 out of 6 test cases passed
- Reliability score: 1.00
- Tests cover correct guesses, too high, and too low scenarios
- Logging is implemented to track test results and errors

The results show that the system is consistent and reliable for core functionality.