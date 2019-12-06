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
	"formula": "BH48P12C",
	"inChi": "1S/C21H19OS4/c1-11-13(3)25-20(15-7-5-9-23-15)17(11)19(22)18-12(2)14(4)26-21(18)16-8-6-10-24-16/h5-10,22H,1-4H3",
	"id_user": 2,
    	"siblings": [
					{"id_log":"1t0j_moBaHZQCbKm6dnI","job":"OPT"},
					{"id_log":"190j_moBaHZQCbKm89lG","job":"TD"}
					]
}

res = es.index(index='molecules',doc_type='molecule',id=10,body=ins)
"""
#Fonction intersection permettant de faire l'intersection de deux listes
# Paramètres :
#				liste1 : première liste
#				liste2 : deuxième liste
# Retour :		Liste finale avec l'intersection
def intersection(liste1, liste2):
    liste3 = [value for value in liste1 if value in liste2]
    return liste3

#Fonction decomposer_molecule permmettant de décomposer la molécule par éléments pour
#un recherche plus pertinente
# Paramètre :
#				mol_recherche : molécule d'entrée
# Retour :		Liste des éléments d'une molécule
def decomposer_molecule(mol_recherche):
	liste_mol_recherche = list(mol_recherche)
	liste_mol = []
	mol = liste_mol_recherche[0]
	for i in range(1,len(mol_recherche)):
		if(liste_mol_recherche[i].isdigit()):
			mol+=liste_mol_recherche[i]
		else:
			liste_mol.append(mol)
			mol = liste_mol_recherche[i]
	liste_mol.append(mol)
	return liste_mol

#Fonction recherche_partielle permettant de rechercher une molécule dans la base de donnée
#à partir d'une recherche, elle fournit les meilleurs résultats
# Paramètres :
# 				mol_recherche   : Recherche
#			    limite_resultat : Limite des résultats
#				avec_pertinence : Activation de la pertinence
# Retour :	    Liste des molécules
def recherche_partielle(mol_recherche,limite_resultat,avec_pertinence):
	s = Search(using=es, index="molecules", doc_type="molecule")
	s = s.source(['formula', 'inChi', 'siblings'])
	s = s.query('regexp',formula='[a-z0-9]*'+mol_recherche+'[a-z0-9]*')
	s = s.sort('formula')
	s = s[0:limite_resultat]


	print ("Liste resultat de : "+mol_recherche)
	for commit in s.execute():
		print ("\t"+commit.formula)
		#print (commit.inChi)
		#print (commit.siblings[1].id_log)
	if(avec_pertinence):
		recherche_partielle_pertinent(mol_recherche,limite_resultat)

#Fonction recherche_partielle permettant de rechercher une molécule dans la base de donnée
#à partir d'une recherche, elle fournit les résultats pertinents autre que les meilleurs résultats
# Paramètres :
# 				mol_recherche   : Recherche
#				limite_resultat : Limite des résultats
# Retour : 		Liste des molécules
def recherche_partielle_pertinent(mol_recherche,limite_resultat):
	liste_liste_mol = []
	for element in decomposer_molecule(mol_recherche):
		s = Search(using=es, index="molecules", doc_type="molecule")
		s = s.source(['formula', 'inChi', 'siblings'])
		s = s.query('regexp',formula='[a-z0-9]*'+element+'[a-z0-9]*')
		s = s.sort('formula')
		s = s[0:limite_resultat]
		liste_mol = []
		print ("Liste resultats pertinent de : "+element)
		for commit in s.execute():
			print ("\t"+commit.formula)
			liste_mol.append(commit.formula)
			#print (commit.inChi)
			#print (commit.siblings[1].id_log)
		liste_liste_mol.append(liste_mol)
		liste_mol = []
	print("Liste resultats pertinent de : "+mol_recherche)
	liste_mol_final = liste_liste_mol[0]
	for i in range(1,len(liste_liste_mol)):
		liste_mol_final=intersection(liste_mol_final,liste_liste_mol[i])

	for molecule in liste_mol_final:
		print("\t"+molecule)

recherche_partielle("c21hs4",10,1)
#recherche_partielle_pertinent("c3s4",10)
#decomposer_molecule("c3s4")
