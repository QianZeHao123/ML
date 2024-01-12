import os

# Use the current working directory
directory = os.getcwd()

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a Markdown file
    if filename.endswith('.md'):
        # Create the full file path
        filepath = os.path.join(directory, filename)

        # Read the content of the file
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        # Replace '```r' with '```{r}'
        modified_content = content.replace('```r', '```{r}')

        # Create the new file name with .Rmd extension
        new_filename = os.path.splitext(filename)[0] + '.Rmd'
        new_filepath = os.path.join(directory, new_filename)

        # Write the modified content to the new file
        with open(new_filepath, 'w', encoding='utf-8') as new_file:
            new_file.write(modified_content)

print("Processing complete.")
