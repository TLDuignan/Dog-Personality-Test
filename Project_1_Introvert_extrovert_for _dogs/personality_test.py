import sys

def display(personality_type):
    print(f"Your dog is an {personality_type}")
def run():
    questions: list = [
        """
Question 1. You at the dog park. Your dog does witch of the following:
    a. Stays by your side and watches the other dogs.
    b. Runs around and plays with the other dogs.
""",
        """
Question 2. You have friends over. Does your dog:
    a. Greets the guest but then lays down in his bed.
    b. Spends the night getting pets from each person.
""",
        """
Question 3. Your dogis happier:
    a. Going for a nice hike
    b. Going to the dog park.
""",
        """
Question 4. Your dog sees another animal outside the house. Do they:
    a. Bark while watching it from the window.
    b. Bark and scratch at the door wanting to go chase it.
""",
        """
Question 5. You are introducing your dog to a new friend. Does your dog:
    a. Greets the friend but mainly stays by you.
    b. Spend the whole time sitting next to friend getting lots of love.
"""
    ]

    count_of_a: int = 0
    count_of_b: int = 0
    personality_dichotomy: str = ''
    count = 0

    for question in questions:
        answer = ''
        while not (answer == 'A' or answer == 'B'):
            count_of_a = 0
            count_of_b = 0
            try:
                answer = input(question).upper()
                if not (answer == 'A' or answer == 'B'):
                    raise ValueError("Invalid input")
            except ValueError as error:
                print(error)
            else:
                if answer == 'A':
                    count_of_a = count_of_a + 1
                if answer == 'B':
                    count_of_b = count_of_b + 1
                count = count + 1

        if count == 5:
            if count_of_a > count_of_b:
                personality_dichotomy = personality_dichotomy + 'Introvert '
            else:
                personality_dichotomy = personality_dichotomy + 'Extrovert '

    display(personality_dichotomy)


def exit_application():
    print("Exiting application...")
    sys.exit(0)


def main():
    user_input = input("""
    Is your dog an Introvert or an Extrovert?
    Take this test to quick test to find out.
    Press 1  to take test
    Press 2 to exit """)
    try:
        if not (user_input == "1" or user_input == "2"):
            raise ValueError("Invalid input")
    except ValueError as error:
        print(error)
    else:
        switcher = {
            "1": run,
            "2": exit_application
        }
        return switcher.get(user_input)()


if __name__ == "__main__":
    main()