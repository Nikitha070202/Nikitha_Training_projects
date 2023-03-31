import time

# Define the questions and answers
QUESTIONS = {  
    "What's the name of Python's sorting algorithm": [
        "Timsort", "Quicksort", "Merge sort", "Bubble sort"
    ],
    
    "Which built-in function can get information from the user": [
        "input", "get", "print", "write"
    ],
    "Which keyword do you use to loop over a given list of elements": [
        "for", "while", "each", "loop"
    ],
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
}

# Set the initial score to 0
score = 0

# Loop through the questions
for question, alternatives in QUESTIONS.items():
    # Get the correct answer and print the alternatives
    correct_answer = alternatives[0]
    for alternative in sorted(alternatives):
        print(f"  - {alternative}")
    
    # Start the timer
    start_time = time.time()

    # Get the user's answer
    answer = input(f"{question}? ")
    
    # Stop the timer and calculate the elapsed time
    elapsed_time = time.time() - start_time
    
    # Check the user's answer
    if answer == correct_answer:
        print("Correct!")
        # Add points to the score based on how fast the user answered
        if elapsed_time < 5:
            score += 3
        elif elapsed_time < 10:
            score += 2
        else:
            score += 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
    
    # Print the elapsed time and the current score
    print(f"Time: {elapsed_time:.2f}s")
    print(f"Score: {score}")
