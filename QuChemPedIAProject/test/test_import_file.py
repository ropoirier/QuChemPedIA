import unittest
import common_qcpia.QuChemPedIA_lib.import_file_lib as ifl

class ImportFileTest(unittest.TestCase):

	"""Test case utilise pour tester la fonction d'import de nouvelles mollecules dans la base de donnees ElasticSearch."""

	def setUp(self):
		"""Initialisation et declaration des fichiers JSON de test"""
		self.cas15_path = "../../../json/"
		self.cas15_json = "cas2.json"
		self.cas15_id = 1

	def test_import_file(self):
		"""Test echec"""
		ret = import_file(self.cas15_path, self.cas15_json, self.cas15_id)
		self.assertEqual(0,ret,"echec")
		
unittest.main()
