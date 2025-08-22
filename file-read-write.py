def modify_content(content):
    """
    Modify the content in a specific way.
    Example: Convert the text to uppercase.
    """
    return content.upper()

def read_and_write_file():
    try:
        # Ask the user for the input file name
        input_file = input("Enter the name of the file to read: ")

        # Open and read the file content
        with open(input_file, 'r') as file:
            content = file.read()

        # Modify the file content
        modified_content = modify_content(content)

        # Ask for output file name
        output_file = input("Enter the name of the new file to write to: ")

        # Write the modified content to the new file
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"File '{input_file}' read successfully.")
        print(f"Modified content written to '{output_file}'.")

    except FileNotFoundError:
        print("Error: The file you are trying to read does not exist.")
    except PermissionError:
        print("Error: Permission denied for reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    read_and_write_file()
