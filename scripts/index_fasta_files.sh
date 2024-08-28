#!/bin/bash 

# Function to index fasta files
index_fasta() { local folder="$1"
    # Find all .fasta and .fa files in the given folder and its subfolders
    find "$folder" -type f \( -name "*.fasta" -o -name "*.fa" \) | while read -r fasta_file; do
        # Index the fasta file
        echo "Indexing $fasta_file" samtools faidx "$fasta_file" 
        samtools faidx "$fasta_file"
	done
}
# Directory to start search (current directory if not specified)
search_dir="."
# If a directory is provided as an argument, use it
if [ "$#" -ge 1 ]; then  #checks if the number of arguments ($#) passed to the script is greater than or equal to 1
search_dir="$1" 
fi
# Call the function with the specified or default directory
index_fasta "$search_dir"
