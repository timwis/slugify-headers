import sys
import csv
from slugify import slugify

reader = csv.reader(sys.stdin)
headers = next(reader)

clean_headers = []
for header in headers:
    clean_headers.append( slugify(header, separator="_") )

print ",".join(clean_headers)
