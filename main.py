import sys
import csv
import argparse
import json
from slugify import slugify

# Look for --json argument
parser = argparse.ArgumentParser(description="Slugify headers")
parser.add_argument("--json", dest="output_json", action="store_true", help="output in json")
args = parser.parse_args()

reader = csv.reader(sys.stdin)
headers = next(reader)

clean_headers = []
for header in headers:
    clean_headers.append( slugify(header, separator="_") )

if args.output_json:
  print json.dumps(clean_headers)
else:
  print ",".join(clean_headers)
