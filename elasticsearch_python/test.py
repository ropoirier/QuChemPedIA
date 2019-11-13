#!/usr/bin/python2.6
# -*-coding:Latin-1 -*
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
from django.conf import settings

#connextion à elasticsearch
es = Elasticsearch([{'host':'localhost','port':9200}])

# test insertion

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


# Test select elasticsearch dsl

s = Search(using=es, index="movies", doc_type="movie")
s = s.sort('title')
s = s.source(['title', 'director', 'year'])
s = s.query('regexp',title='k[a-z]*')

s = s[0:10]


for commit in s.execute():
	print (commit.title.encode('utf-8'),commit.director.encode('utf-8'), commit.year)

