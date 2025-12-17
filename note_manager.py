# note_manager.py

FILE_NAME = "notes.txt"

def add_note():
    note = input("Enter your note: ")
    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")
    print("Note added successfully!")

def view_notes():
    try:
        with open(FILE_NAME, "r") as file:
            notes = file.readlines()
            if not notes:
                print("No notes found.")
            else:
                print("\n--- YOUR NOTES ---")
                for i, note in enumerate(notes, start=1):
                    print(f"{i}. {note.strip()}")
    except FileNotFoundError:
        print("No notes file found.")

def menu():
    print("\n--- NOTE MANAGER ---")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

while True:
    menu()
    choice = input("Choose option: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
