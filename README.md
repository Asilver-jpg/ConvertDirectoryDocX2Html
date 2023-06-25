# ConvertDirectoryDocX2Html

A set of utilities for the file server experience. 

convertDocToHTML.py - replicates the file structure of the google docs that the team wrote the files in into pure HTML to be put in an S3 bucket.

getFileServerObjects.py - prints a list of FileNodes for directories and files in the terminal. Needed in the fileServerExperience in Directory.ts and Files.ts respectively whenever a directory or file is added, moved or removed. Not needed to run if the file is changed. Run the previous command in this case.
