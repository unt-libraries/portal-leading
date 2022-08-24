import sys
import json
import urllib.request

import requests

if len(sys.argv) != 2:
    print('usage: python merge-untlbs-json-with-counts.py <untl-bs.json>')
    exit() 

with open(sys.argv[1]) as fp:
    untl_bs = json.load(fp)

request_url = [
    'https://digital.library.unt.edu/solrparse/raw/?q=*:*',
    'fq=(aubrey_system:PTH+OR+untl_institution:UNTA)+AND+dc_rights_access:public',
    'facet=true',
    'facet.field=dc_subject.UNTL-BS_facet',
    'facet.limit=-1',
    'facet.mincount=1',
    'wt=json',
    'rows=1'
    ]

# print('&'.join(request_url))

# Build and make the request to the Solr server.
response = urllib.request.urlopen('&'.join(request_url)).read()

# Convert the response (which is json) into a python object.
data = json.loads(response.decode('utf-8'))

# Convert the Solr facet format into a dict with counts.
x = (data['facet_counts']['facet_fields']['dc_subject.UNTL-BS_facet'])
values = dict(zip([d for d in x[::2]], [int(d) for d in x[1::2]]))

# Create a blank dict to store our final UNTL-BS values
untl_with_counts = {}

# Iterate through the valid UNTL-BS values. 
for i in untl_bs:
    # Default assign each a count of zero. 
    untl_with_counts[i] = 0
    # If they occur in the values dict (from Solr) then use the Solr values
    if i in values:
        untl_with_counts[i] = values[i]

# Pretty print the json structure
print(json.dumps(untl_with_counts, indent=2, sort_keys=True))

