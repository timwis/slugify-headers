import sys
import csv
import json
from slugify import slugify

reader = csv.reader(sys.stdin)
headers = next(reader)

clean_headers = []
for header in headers:
    clean_headers.append( slugify(header, separator="_") )

print json.dumps(clean_headers)
