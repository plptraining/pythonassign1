# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

def read_and_modify_file():
    filename = input("Enter the filename to read from: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            modified = content.upper()  # Example modification: convert to uppercase

        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified)

        print(f"✅ File read successfully and written to '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except IOError:
        print("❌ Error: Could not read or write to the file.")

# Run the function
read_and_modify_file()
