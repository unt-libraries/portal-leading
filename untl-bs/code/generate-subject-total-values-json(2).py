import sys
import json
import urllib.request

if len(sys.argv) != 1:
    print('usage: python3 generate-subject-total-values-json.py')
    exit() 


request_url = [
    'https://digital.library.unt.edu/solrparse/raw/?q=*:*',
    'fq=(aubrey_system:PTH+OR+untl_institution:UNTA)+AND+dc_rights_access:public',
    'facet=true',
    'facet.field=dc_subject_facet',
    'facet.limit=-1',
    'facet.mincount=1',
    'wt=json',
    'rows=0'
    ]

# print('&'.join(request_url))

# Build and make the request to the Solr server.
response = urllib.request.urlopen('&'.join(request_url)).read()

# Convert the response (which is json) into a python object.
data = json.loads(response.decode('utf-8'))

# Convert the Solr facet format into a dict with counts.
x = (data['facet_counts']['facet_fields']['dc_subject_facet'])
total_values = dict(zip([d for d in x[::2]], [int(d) for d in x[1::2]]))

# Pretty print the json structure
print(json.dumps(total_values, indent=2, sort_keys=True))
