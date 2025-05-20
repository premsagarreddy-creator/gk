dddddddddddef gk_quiz():
    """Main function placeholder for General Knowledge Quiz."""
    pppppppass
def print_banner():
    print("Welcome to the General Knowledge Quiz!")
    RED = '\033[91m'
    gggggGREEN = '\033[92m'
    YELLlllllllOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    def print_banner():
        print(CYAN + "\n🌍 Welcome to the General Knowledge Quiz! 🌍\n" + RESET)
        def print_question(q, options):
    print(YELLOW + q + RESET)
    for key, val in options.items():
        print(f"  {key}) {val}")
   def get_valid_input():
    while True:
        ans = input("Enter your answer (a/b/c/d): ").lower()
        if ans in ['a', 'b', 'c', 'd']:
            return ans
        print(RED + "Invalid input, try again." + RESET)

  def ask_question(question, options, correct):
    print_question(question, options)
    answer = get_valid_input()
    if answer == correct:
        print(GREEN + "Correct!\n" + RESET)
        return True
    else:
        print(RED + f"Wrong! Correct answer is '{correct}'.\n" + RESET)
        return False
    def question1():
    return ask_question(
        "Which country is known as the Land of the Rising Sun?",
        {'a': 'China', 'b': 'Japan', 'c': 'South Korea', 'd': 'Thailand'},
        'b'
    )
  def question2():
    return ask_question(
        "What is the capital city of Australia?",
        {'a': 'Sydney', 'b': 'Melbourne', 'c': 'Canberra', 'd': 'Brisbane'},
        'c'
    )
    def question3():
    return ask_question(
        "Who invented the telephone?",
        {'a': 'Alexander Graham Bell', 'b': 'Thomas Edison', 'c': 'Nikola Tesla', 'd': 'Guglielmo Marconi'},
        'a'
    )
    def question4():
    return ask_question(
        "What is the largest continent by area?",
        {'a': 'Africa', 'b': 'Asia', 'c': 'Europe', 'd': 'North America'},
        'b'
    )

def question5():
    return ask_question(
        "Which ocean is the deepest in the world?",
        {'a': 'Atlantic Ocean', 'b': 'Indian Ocean', 'c': 'Arctic Ocean', 'd': 'Pacific Ocean'},
        'd'
    )
    questions = [question1, question2, question3, question4, question5]
    def run_gk_quiz():
    print_banner()
    score = 0
    for q in questions:
        if q():
            score += 1
    print(f"You scored {score}/{len(questions)}!")
import time

def loading():
    print("Loading questions", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")
def run_gk_quiz():
    print_banner()
    loading()
    score = 0
    for q in questions:
        if q():
            score += 1
    print(f"You scored {score}/{len(questions)}!")
def show_score(score, total):
    print(f"\nYou scored {score}/{total}!")
    if score == total:
        print("🏆 Excellent! Perfect score!")
    elif score >= total * 0.6:
        print("👍 Good job!")
    else:
        print("📘 Keep learning!")
        def run_gk_quiz():
    print_banner()
    loading()
    score = 0
    for q in questions:
        if q():
            score += 1
    show_score(score, len(questions))
def ask_replay():
    answer = input("Do you want to play again? (y/n): ").lower()
    if answer == 'y':
        run_gk_quiz()
    else:
        print("Thanks for playing!")
def run_gk_quiz():
    print_banner()
    loading()
    score = 0
    for q in questions:
        if q():
            score += 1
    show_score(score, len(questions))
    ask_replay()
    def run_gk_quiz():
    """Run the full general knowledge quiz with questions, scoring, and replay."""
    print_banner()
    loading()
    score = 0
    for q in questions:
        if q():
            score += 1
    show_score(score, len(questions))
    ask_replay()
    def ask_question(question, options, correct):
    """
    Display a question and options, validate input, and return True if correct.
    """
    print_question(question, options)
    answer = get_valid_input()
    if answer == correct:
        print(GREEN + "Correct!\n" + RESET)
        return True
    else:
        print(RED + f"Wrong! Correct answer is '{correct}'.\n" + RESET)
        return False
    def safe_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\nQuiz interrupted. Exiting.")
        exit()
def get_valid_input():
    while True:
        ans = safe_input("Enter your answer (a/b/c/d): ").lower()
        if ans in ['a', 'b', 'c', 'd']:
            return ans
        print(RED + "Invalid input, try again." + RESET)

def ask_replay():
    answer = safe_input("Do you want to play again? (y/n): ").lower()
    if answer == 'y':
        run_gk_quiz()
    else:
        print("Thanks for playing!")
if __name__ == "__main__":
    run_gk_quiz()
    """
General Knowledge Quiz Module
Includes a multiple-choice general knowledge quiz game with scoring and replay.
"""

import time

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

