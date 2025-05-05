try:
    with open(r"C:\Users\taiba\OneDrive\Documents\plp_all\python\week4\input.txt", "r") as infile:
        contents = infile.read()
    
    word_count = len(contents.split())

    upper_text = contents.upper()

    # Step 4: Write to output.txt
    with open(r"C:\Users\taiba\OneDrive\Documents\plp_all\python\week4\output.txt", "w") as outfile:
        outfile.write(upper_text + "\n\n")
        outfile.write(f"Word Count: {word_count}")

    # Step 5: Print success message
    print("✅ Success! 'output.txt' has been created with the processed text and word count.")
except FileNotFoundError:
    print("❌ Error: 'input.txt' not found.")
except Exception as e:
    print(f"❌ An error occurred: {e}")
