import os
import random
from src.csv_resources_reader import read_csvs_and_group
from src.difficulty import difficulty_level
from src.helper import clear_screen
from src.questions.question_util import select_question_types, assign_questions, generate_questions_and_answers, generate_pdf, register_font
from datetime import datetime

# Get data
results = read_csvs_and_group('resources')



# Get general information
clear_screen()
reading_options = ['English']
print('Choose the main reading language from the options below:')
for idx, option in enumerate(reading_options, 1):
    print(f'{idx}. {option}')

while True:
    reading_choice = input('Enter the number corresponding to the reading language: ')
    if reading_choice.isdigit() and 1 <= int(reading_choice) <= len(reading_options):
        reading_language = reading_options[int(reading_choice) - 1]
        break
    else:
        print('Invalid option. Please try again.')


clear_screen()
options = ['Portuguese (WIP)', 'English (WIP)', 'Spanish (WIP)', 'French (WIP)', 'Japanese']
print('Choose the target translation language from the options below:')
for idx, option in enumerate(options, 1):
    print(f'{idx}. {option}')

while True:
    choice = input('Enter the number corresponding to the target language: ')
    if choice.isdigit() and 1 <= int(choice) <= len(options):
        target_language = options[int(choice) - 1]
        break
    else:
        print('Invalid option. Please try again.')

clear_screen()
difficulty = difficulty_level(target_language)

selected_types = select_question_types()

clear_screen()
num_questions = input('Enter the number of questions you want to generate: ')


# Generate question type list
question_type_list = assign_questions(num_questions, selected_types)

print(question_type_list)

# Generate questions and answers
questions, answers = generate_questions_and_answers(
    question_type_list,
    results,
    reading_language,
    target_language,
    difficulty
)

# Create PDFs
register_font("NotoSansJP-Regular", "./resources/font/NotoSansJP-Regular.ttf")
register_font("NotoSansJP-Bold", "./resources/font/NotoSansJP-Bold.ttf")

# Generate timestamp string
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Build file names with timestamp
questions_filename = f"./output/questions_{timestamp}.pdf"
answers_filename = f"./output/answers_{timestamp}.pdf"

generate_pdf(questions, questions_filename, titulo="Perguntas", fonte="NotoSansJP")
generate_pdf(answers, answers_filename, titulo="Respostas", fonte="NotoSansJP")

print("PDFs gerados com sucesso!")
exit()

