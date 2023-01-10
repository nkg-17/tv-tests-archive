#!/usr/bin/python

import os
import sys
import json


tests = {}

for tid in os.listdir("./tests"):
	if os.path.isdir(os.path.join("./tests", tid)):
		print(f"Loading {tid} ... ", end='')
		try:
			desc = {}
			with open(os.path.join("tests", tid, "description.json")) as f:
				desc = json.load(f)
			
			test = {
				'id': tid,
				'problem': {
					'text': desc['problem']['text'],
					'answer': {
						'type': 0,
						'placeholder': desc['problem']['answer']
					}
				},
				'solution': {
					'text': desc['solution']['text'],
					'answer': desc['solution']['answer']
				}
			}

			tests[tid] = test
			print('ok')
		except Exception as e:
			raise e

with open("tests.json", 'w') as f:
	json.dump(tests, f, indent=4)

print(f"Saved {len(tests)} tests to 'tests.json'")