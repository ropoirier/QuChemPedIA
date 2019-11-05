import random
import unittest

class RandomTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random' """

    # Success
    def test_choice1(self):
        """Test le fonctionnement de la fonction 'random.choice'."""
        liste = list(range(10))
        elt = random.choice(liste)
        # Vérifie que 'elt' est dans 'liste'
        self.assertIn(elt, liste)

    # Failure
    def test_choice2(self):
        """Test le fonctionnement de la fonction 'random.choice'."""
        liste = list(range(10))
        elt = random.choice(liste)
        self.assertIn(elt, ('a', 'b', 'c'))

unittest.main()
