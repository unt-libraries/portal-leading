import urllib.request
import json
import sys

import requests



def get_solr_results_cursor(solr_query, timeout=10, cursor_mark="*", num_rows_in_one_shot=10, unique_field_name="id"):
    """
    The function imitates a cursor for bringing data from solr.
    cursor_mark is cursorMark query parameter of solr,
    num_rows_in_one_shot is kind of tuning factor for querying again and again until required number of rows are returned.
    *** solr query must not include rows and start parameters .***
    """

    fetch_more = True
    while fetch_more is True:
        num_rows_part = "&rows=" + str(num_rows_in_one_shot) + "&sort=" + str(unique_field_name) + "+asc&cursorMark=" + str(cursor_mark) + "&timeAllowed=-1"
        req = requests.get(solr_query + num_rows_part, timeout=timeout)
        solr_dict = req.json()
        num_docs = len(solr_dict['response']['docs'])
        cursor_mark = solr_dict.get('nextCursorMark')

        if num_docs == 0 or cursor_mark is None:
            fetch_more = False
        for each_dict in solr_dict['response']['docs']:
            yield (each_dict, cursor_mark)
            
def term_to_filename(term):
    """
    Normalize term into a filename by removing commas and spaces.
    """
    term = term.replace(',', '')
    term = term.replace(' ', '')
    return term + '.txt'

# Make sure there is a file with UNTL-BS terms.
if len(sys.argv) != 2:
    print('usage: python3 create-tsv-untlbs-for-topic-models.py <list of UNTL-BS subjects>')
    sys.exit()

# Open UNTL-BS terms file.
with open(sys.argv[1]) as fp:
    untl_bs = fp.read().splitlines()
   
# Iterate through the terms, create file and fill it with data. 
for term in untl_bs:
    filename = term_to_filename(term)
    term_plus = term.replace(' ', '+') # convert spaces to + for URL


    request_url = [
        "https://digital.library.unt.edu/solrparse/raw/?q=*:*",
        'fq=(aubrey_system:PTH+OR+untl_institution:UNTA)+AND+dc_rights_access:public',
        f'fq=dc_subject.UNTL-BS_facet:"{term_plus}"',
        "wt=json",
        "fl=aubrey_identifier,display_title,dc_description,dc_subject.KWD_facet,dc_subject.LCSH_facet,dc_subject.named_person_facet,dc_subject.named_animal_facet",
        ]


    # print("&".join(request_url))
    response = urllib.request.urlopen("&".join(request_url)).read()

    print(f'Writing: {term} to {filename}')
    with open(filename, 'w') as writer:

        
        for f in get_solr_results_cursor("&".join(request_url), unique_field_name='aubrey_identifier', num_rows_in_one_shot=1000):
            subjects = []
            aubrey_identifier = f[0]['aubrey_identifier']
            display_title = f[0]['display_title']
            if f[0].get('dc_description'):
                dc_description = f[0].get('dc_description')[0]
            else:
                dc_description = ''
            print(f[0])
            subjects.extend(f[0].get('dc_subject.KWD_facet', []))
            subjects.extend(f[0].get('dc_subject.LCSH_facet', []))
            subjects.extend(f[0].get('dc_subject.named_person_facet', []))
            subjects.extend(f[0].get('dc_subject.named_animal_facet', []))


            dc_subject = '\t'.join(subjects)
            
            output = '\t'.join([aubrey_identifier, display_title, dc_description, dc_subject, '\n'])
            writer.write(output)