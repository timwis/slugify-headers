# Slugify Headers
A python script to get database_friendly_field_names for a CSV file

## Usage
Given a CSV file where the first row contains malformed headers, ie.:
```
Animal,No. of Legs, DOMESTICATED, Notes** Here
Dog, 4, true, "great pet"
Cat, 4, false, "no thx"
```

Pass the file to this script via `stdin`:
```bash
$ cat data.csv | python main.py
```

And it will return database-friendly headers with special characters and extra spaces removed:
```
animal,no_of_legs,domesticated,notes_here
```

For greater efficiency, just pass the first row of the CSV file:
```bash
$ head -1 data.csv | python main.py
```

To replace the header line in the original file, use silly simple posix programs:
```bash
# Get clean headers and put then in a new file
$ head -1 data.csv | python main.py > new_data.csv

# Append the source file without the first row to the new file
$ tail -n+2 data.csv >> new_data.csv
```
