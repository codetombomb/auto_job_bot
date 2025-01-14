import csv
from pprint import pprint
from dotenv import dotenv_values
import pandas as pd

# Load environment variables
config = dotenv_values()


def replace_placeholders(text):
    for env_key, env_value in config.items():
        placeholder = f"{{{env_key}}}"
        if placeholder in text:
            text = text.replace(placeholder, env_value)

    return text.strip().strip()


def process_csv(file_path):
    processed_data = {}
    # Open the CSV file
    with open(file_path, '+', newline='', encoding='utf-8') as csv_file:
        # Read the CSV file
        # Loop through each row in the CSV file
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            # Get the question and answer from the row
            question = row[0]
            answer = row[1]
            # Replace placeholders in the question and answer
            question = replace_placeholders(question)
            answer = replace_placeholders(answer)
            processed_data[question] = answer
    # csv_writer = csv.writer(csv_file)
    # csv_writer.writerow([question, answer])
    # csv_file.close()
    return processed_data


def make_data_frame(data_dict):
    df = pd.DataFrame(list(data_dict.items())[
                      1:-1], columns=['Prompt', 'Answer'])
    return df


def make_data_frame_from_csv(file_path):
    processed_data = process_csv(file_path)
    data_frame = make_data_frame(processed_data)

    return data_frame

# Process the CSV file
# processed_csv_data = make_data_frame_from_csv('qa_pairs.csv')
# pprint(processed_csv_data)

# Write to trainer_sheet.csv


def write_to_trainer_sheet(prompt, answers):
    with open('trainer_sheet.csv', 'a', newline='\n', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        answers_string = ';'.join(answers)
        writer.writerow([prompt, answers_string])
