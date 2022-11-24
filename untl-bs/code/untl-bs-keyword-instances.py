import sys
import json
import urllib.request
import urllib.parse

import requests

if len(sys.argv) != 2:
    print('usage: python untl-bs-keyword-instances <untl-bs.json>')
    exit() 

with open(sys.argv[1]) as fp:
    untl_bs = json.load(fp)

# Setting up our header line information.
header = list(range(0, 101))
header.insert(0, "UNTL-BS")
header.insert(1, "Records")
print(*header, sep='\t')

for subject in untl_bs:

    untl_bs_lookup = urllib.parse.quote_plus(subject) # To URL encode the UNTL-BS terms.

    request_url = [
        'https://digital.library.unt.edu/solrparse/raw/?q=*:*',
        'fq=(aubrey_system:PTH+OR+untl_institution:UNTA)+AND+dc_rights_access:public',
        'facet=true',
        f'fq=dc_subject.UNTL-BS_facet:"{untl_bs_lookup}"',
        'facet.field=dc_subject.KWD_count',
        'facet.limit=-1',
        'facet.mincount=1',
        'facet.query=-dc_subject.KWD_count:[1+TO+*]',  # To get the number of 0 keyword records.
        'wt=json',
        'rows=0'
        ]

    # print('&'.join(request_url))

    # Build and make the request to the Solr server.
    response = urllib.request.urlopen('&'.join(request_url)).read()

    # Convert the response (which is json) into a python object.
    data = json.loads(response.decode('utf-8'))
    record_count = data['response']['numFound']
    keyword_instance_array = [0] * 101

    if data.get('facet_counts'):
        # Convert the Solr facet format into a dict with counts.
        x = (data['facet_counts']['facet_fields']['dc_subject.KWD_count'])
        values = dict(zip([int(d) for d in x[::2]], [int(d) for d in x[1::2]]))
        zero_count = data['facet_counts']['facet_queries']['-dc_subject.KWD_count:[1 TO *]']
        keyword_instance_array[0] = zero_count
        for k in values:
            if k <= 100:
                keyword_instance_array[k] = values[k]  
                
    # Insert Subject name and total record counts.             
    keyword_instance_array.insert(0, subject)
    keyword_instance_array.insert(1, record_count)
    print(*keyword_instance_array, sep='\t')
