#!/usr/bin/python2.6
# -*-coding:Latin-1 -*
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
from django.conf import settings
import requests, json, os
#connextion à elasticsearch
es = Elasticsearch([{'host':'localhost','port':9200}])


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

#pubchem 

s = Search(using=es, index="molecules", doc_type="molecule")
s = s.sort('formula')
s = s.source(['formula', 'inChi', 'siblings'])
s = s.query('regexp',formula='[a-z0-9]*h19o[a-z0-9]*')

s = s[0:10]


sibling = ""
for commit in s.execute():
	print (commit.formula)
	#print (commit.inChi)
	#print (commit.siblings[1].id_log)
	sibling=commit.siblings[1]
