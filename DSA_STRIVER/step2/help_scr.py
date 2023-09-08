# Define the input and output file paths
input_file_path = 'DSA_STRIVER/step2/input.txt'
output_file_path = 'DSA_STRIVER/step2/output.txt'

# Open the input file for reading and the output file for writing
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    # Read the content of the input file
    content = input_file.read()

    # Replace spaces with commas
    content_with_commas = content.replace(' ', ',')

    # Write the modified content to the output file
    output_file.write(content_with_commas)

print(f'Spaces replaced with commas and saved to {output_file_path}')
