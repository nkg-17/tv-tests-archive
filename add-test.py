#!/usr/bin/python3

import os
import sys
import os.path


# "about" field is not documented. 
# It's just to remember the source of the test ("3.docx - task 7" for example).
description_format = """
{{
    "title": "{title}",

    "problem": {{
        "text": "{problem}",
        "answer": "{placeholder}"
    }},

    "solution": {{
        "text": "{solution}",
        "answer": "{answer}"
    }},

    "about": "{about}"
}}
"""


def create_description(
		title: str="", 
		problem: str="",
		placeholder: str="Ответ", 
		solution: str="", 
		answer: str="",
		about: str="") -> str:
	return description_format.format(
		title=title,
		problem=problem,
		placeholder=placeholder,
		solution=solution,
		answer=answer,
		about=about
	)


script_dir = os.path.dirname(os.path.realpath(__file__))
tests_folder = os.path.join(script_dir, 'tests')


def is_valid_id(folder: str) -> bool:
	return os.path.isdir(os.path.join(tests_folder, folder)) and folder.isalnum()


ids = [ int(item) for item in os.listdir(tests_folder) if is_valid_id(item)]

last_id = max(ids)
new_id = str(last_id + 1)
new_test_folder = os.path.join(tests_folder, new_id)

os.mkdir(new_test_folder)
with open(os.path.join(new_test_folder, 'description.json'), 'w') as file:
	file.write(create_description(title=new_id))

print(f"Created new test \"{new_id}\"")