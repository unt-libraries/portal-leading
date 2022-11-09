import sys
import json
import urllib.request

import requests

if len(sys.argv) != 3:
    print('usage: python3 generate-subject-total-values-json.py <subject-instance-counts.json> "UNTL-BS To Lookup"')
    exit() 

with open(sys.argv[1]) as fp:
    subject_totals = json.load(fp)

untl_bs_lookup = sys.argv[2].strip().replace(' ', '+')

request_url = [
    'https://digital.library.unt.edu/solrparse/raw/?q=*:*',
    'fq=(aubrey_system:PTH+OR+untl_institution:UNTA)+AND+dc_rights_access:public',
    f'fq=dc_subject_facet:"{untl_bs_lookup}"',
    'facet=true',
    'facet.field=dc_subject_facet',
    'facet.limit=-1',
    'facet.mincount=1',
    'facet.sort=count',
    'wt=json',
    'rows=0'
    ]

# print('&'.join(request_url))

# Build and make the request to the Solr server.
response = urllib.request.urlopen('&'.join(request_url)).read()

# Convert the response (which is json) into a python object.
data = json.loads(response.decode('utf-8'))

untl_bs_lookup_count = (data['response']['numFound'])

# Convert the Solr facet format into a dict with counts.
x = (data['facet_counts']['facet_fields']['dc_subject_facet'])
collocation_values = dict(zip([d for d in x[::2]], [int(d) for d in x[1::2]]))

for term in collocation_values:
    global_count = subject_totals.get(term, 0.1) # Global count
    collocation_count = collocation_values[term]
    collocation_percent_of_total = (collocation_count / global_count) * 100
    percent_within_lookup = (collocation_count / untl_bs_lookup_count) * 100
    print(f'{term}\t{global_count}\t{collocation_count}\t{collocation_percent_of_total}\t{percent_within_lookup}')

# Pretty print the json structure
# print(json.dumps(total_values, indent=2, sort_keys=True))
