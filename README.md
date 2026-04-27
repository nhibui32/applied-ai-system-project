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
