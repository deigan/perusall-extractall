# Perusall Extractall

A python script to extract comments from all parts of a Perusall assignment, sorted by student.

## To use

Download the comments .csv file from Perusall > Assignment > All comments > Download as document.

Put perusall-extractall.py in the same directory as the comments file.

Go to that directory in your terminal and run:

`python perusall-extractall.py your-input-file.csv`

This will output a file called your-input-file-extracted-comments.txt.

You can also give an alternative output file name as an optional argument:

`python perusall-extractall.py your-input-file.csv outputfile.txt`
