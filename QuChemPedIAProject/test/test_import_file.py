from django.test import TestCase
from common_qcpia.QuChemPedIA_lib import import_file_lib as ifl

class ImportFileTestCase(TestCase):

    """Test case utilisé pour tester la fonction d'import de nouvelles mollécules dans la base de données ElasticSearch."""
	
	# Voir doc UnitTest pour la fonction setUp(self)
    def setUp(self):
        """Initialisation et déclaration des fichiers JSON de test"""
        self.cas2_path = "../../../json/"
        self.cas2_json = "cas2.json"
        self.cas2_id = 1
		
    def test_import_file(self):
    	# Utilisation de la méthode d'import de molécules en passant le cas n°2 en paramètre
        ret = ifl.import_file(self.cas2_path,self.cas2_json,self.cas2_id)
        # On vérifie que la méthode retourne bien la valeur souhaitée
        self.assertEqual(ret,0)
