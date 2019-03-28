import os.path
import json

def load_notes():
	if os.path.exists("notes.json"):
	    with open("notes.json") as file:
	        notes = json.load(file)
	else:
	    notes = []
	return notes

def save_notes(notes):
	with open("notes.json", "w") as file:
	    json.dump(notes, file)

def add_note():
	title = input("Title >")
	description = input("Description >")
	note = {"title": title, "description" : description}
	notes.append(note)
	save_notes(notes)

notes = load_notes()

def list_notes():
	for note in notes:
		print(note)

print("""List (1)
Get (2)
Add (3)
Delete (4)""")
command = input("> ")
if command == "1":
	list_notes()

if command == "2":
	print(title,
		description)

if command == "3":
	add_note()

if command == "4":
	list_notes()