import unittest
import common_qcpia.QuChemPedIA_lib.import_file_lib as ifl

class ImportFileTest(unittest.TestCase):

    """
    Test case utilisé pour tester la fonction d'import de nouvelles mollécules dans la base de données
    ElasticSearch. 
    """

    def setUp(self):
        """Initialisation et déclaration des fichiers JSON de test"""
        self.cas2_path = "../../../json/"
        self.cas2_json = "cas2.json"
        self.cas2_id = 1

