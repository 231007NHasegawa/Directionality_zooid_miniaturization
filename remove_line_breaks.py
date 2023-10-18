# Some scripts that edit FASTA files may encounter errors if the sequence data within the file contains line breaks. 
# This script targets all FASTA files in a directory and removes line breaks from the sequence data.
# Note: Please ensure the extension of the FASTA files is ".fa".

import os

# Specify the current directory.
directory_path = os.getcwd()

# Create a directory for output.
output_directory_path = os.path.join(directory_path, "output")
os.makedirs(output_directory_path, exist_ok=True)

# Traverse all files in the specified directory.
for filename in os.listdir(directory_path):
    if filename.endswith(".fa"):  # Check if the file is in FASTA format.
        sequence = ""
        with open(os.path.join(directory_path, filename), 'r') as file:
            for line in file:
                if line.startswith(">"):  # Lines starting with ">" are output as they are.
                    if sequence:
                        output.write(sequence + "\n")  # Output the sequence and start a new one.
                        sequence = ""
                    output = open(os.path.join(output_directory_path, filename.rsplit(".", 1)[0] + "_no_linebreaks.fa"), 'a')
                    output.write(line)
                else:
                    sequence += line.strip()  # Remove line breaks from lines not starting with ">".
            output.write(sequence + "\n")  # Output the last sequence.
        output.close()