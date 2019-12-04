#!/usr/bin/python2.6
# -*-coding:Latin-1 -*
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
from django.conf import settings
import requests, json, os
#connextion à elasticsearch
es = Elasticsearch([{'host':'localhost','port':9200}])

# test insertion
"""
ins = {
	"title": "Django",
	"director": "Quentin Tarantino kill",
	"year": 2013,
    	"genres": ["Adventure", "Biography", "Drama"]
}

res = es.index(index='movies',doc_type='movie',id=7,body=ins)



# test select
res= es.search(index='movies',body={"query": {
        "query_string": {
            "query": "killll",
			"fields": ["title"]
        }
    }})
for film in res['hits']['hits']:
	print film['_source']['title']

# test suppresion
#res=es.delete(index='movies',doc_type='movie',id=7)

#print res['found']
"""

# Test select elasticsearch dsl
"""
s = Search(using=es, index="movies", doc_type="movie")
s = s.sort('title')
s = s.source(['title', 'director', 'year'])
s = s.query('regexp',title='k[a-z]*')

s = s[0:10]


for commit in s.execute():
	print (commit.title.encode('utf-8'),commit.director.encode('utf-8'), commit.year)
"""


# test données Quechempedia
"""
directory = '/home/etudiant/Documents/QuChemPedIA/elasticsearch_python/donnees/'
i = 1
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        f = open(filename)
        docket_content = f.read()
        # Send the data into es
        es.index(index='myindex', ignore=400, doc_type='docket',
        id=i, body=json.loads(docket_content))
        i = i + 1
"""

# Test lecture fichier de données Json (une molécule)
"""
f = open("C21H19OS4_SP.json")
docket_content = f.read()
# Send the data into es
es.index(index='myindex', ignore=400, doc_type='docket',
id=1, body=json.loads(docket_content))
"""



# Test insertion prototype molécule
"""
ins = {
	"formula": "C21H19OS4++",
	"inChi": "1S/C21H19OS4/c1-11-13(3)25-20(15-7-5-9-23-15)17(11)19(22)18-12(2)14(4)26-21(18)16-8-6-10-24-16/h5-10,22H,1-4H3",
	"id_user": 2,
    	"siblings": [
					{"id_log":"1t0j_moBaHZQCbKm6dnI","job":"OPT"},
					{"id_log":"190j_moBaHZQCbKm89lG","job":"TD"}
					]
}

res = es.index(index='molecules',doc_type='molecule',id=1,body=ins)
"""



s = Search(using=es, index="molecules", doc_type="molecule")
s = s.sort('formula')
s = s.source(['formula', 'inChi', 'siblings'])
s = s.query('regexp',formula='[a-z0-9]*c[a-z0-9]*')

s = s[0:10]


sibling = ""
for commit in s.execute():
	print (commit.formula)
	print (commit.inChi)
	print (commit.siblings[1].id_log)
	sibling=commit.siblings[1]


s = Search(using=es, index="myindex", doc_type="docket")
s = s.source(['data','job_type','siblings'])

for commit in s.execute():
	print (commit.siblings[0].id_log)
