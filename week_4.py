def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            content = file.read()

        # Modify the content (for example, convert to uppercase)
        modified_content = content.upper()

        with open(output_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to '{output_filename}' successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: Could not read or write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask user for input and output filenames
input_file = input("Enter the name of the file to read from: ")
output_file = input("Enter the name of the new file to write to: ")

read_and_modify_file(input_file, output_file)
