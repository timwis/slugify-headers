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

And it will return database-friendly headers as JSON with special characters and extra spaces removed:
```
["animal", "no_of_legs", "domesticated", "notes_here"]
```

For greater efficiency, just pass the first row of the CSV file:
```bash
$ head -1 data.csv | python main.py
```
