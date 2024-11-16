#!/usr/bin/env python3
import csv
import random
import os
import re

def extract_image_paths(text):
    """Extract image paths from text containing <img> tags."""
    pattern = r'<img src="([^"]+)">'
    return re.findall(pattern, text)

def display_sixel(image_path):
    """Display a .six file directly to terminal."""
    # Convert jpg path to six path
    six_path = image_path.replace('.jpg', '.six')
    try:
        with open(six_path, 'rb') as f:
            print(f.read().decode('ascii', errors='ignore'))
    except Exception as e:
        print(f"Error displaying image: {e}")

# Load the CSV file
with open('PsychQuestions.csv', 'r') as file:
    reader = csv.reader(file)
    # Skip header row if it exists
    header = next(reader, None)
    # Filter out any rows with non-numeric scores
    data = [row for row in reader if row[2].isdigit()]
    datalength = len(data)
    print("Number of items in the list:", datalength)

choice1 = input('1/2 Person? (1/2)')
totalq = 0
totalqc = 0

if choice1.lower() == '1':
    print('1 Person')
    players = 1
elif choice1.lower() == '2':
    print('2 Person')
    players = 2
else:
    print('Invalid choice')

while True:
    # Find the minimum score in the third column
    min_score = min(int(row[2]) for row in data if row[2].isdigit())
    questions = [row for row in data if row[2].isdigit() and int(row[2]) == min_score]
    length = len(questions)
    row = random.choice(questions)

 # Display question and any images in it
    print('Question:', row[0])
    question_images = extract_image_paths(row[0])
    for img_path in question_images:
        display_sixel(img_path)

    if players == 1:
        input('Reveal? (Any)')

    # Display answer and any images in it
    print('Answer:', row[1])
    answer_images = extract_image_paths(row[1])
    for img_path in answer_images:
        display_sixel(img_path)

    while True:
        totalq = (totalq + 1)
        choice = input('Were you correct? (y/n/e-asy) ')

        if choice.lower() == 'y':
            row[2] = str(int(row[2]) + 1)
            os.system('clear')
            totalqc = (totalqc + 1)
            print('Lukes Intermittent Learning Script ------- Running PsychQuestions.csv -------')
            print('Recorded Correct  - ','Score:', row[2],' Completion:  %', (100-((length/datalength)*100)), ' Accuracy:  %', (100*totalqc/totalq))
            print('----------------------------------------------------------------------------')
            break
        elif choice.lower() == 'n':
            os.system('clear')
            print('Lukes Intermittent Learning Script ------- Running PsychQuestions.csv -------')
            print('Recorded Incorrect  - ','Score:', row[2],' Completion:  %', (100-((length/datalength)*100)), ' Accuracy:  %', (100*totalqc/totalq))
            print('----------------------------------------------------------------------------')
            break
        elif choice.lower() == 'e':
            row[2] = str(int(row[2]) + 3)
            os.system('clear')
            print('Lukes Intermittent Learning Script ------- Running PsychQuestions.csv -------')
            print('Recorded Easy  - ','Score:', row[2],' Completion:  %', (100-((length/datalength)*100)), ' Accuracy:  %', (100*totalqc/totalq))
            print('----------------------------------------------------------------------------')
            break
        else:
            print('Invalid choice')
