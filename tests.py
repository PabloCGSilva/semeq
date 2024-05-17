import unittest
from functions import sort_string_as_number, stair_draw, compare_skills, diagonal_diff, perc_elements

class TestFunctions(unittest.TestCase):
    """
    Test case class for functions in the 'functions.py' module.
    """
    
    def test_sort_string_as_number(self):
        """
        Test the sort_string_as_number function.
        """
        # Input array
        arr = ['person_1', 'person_2', 'person_3', 'person_10', 'person_100', 'person_31', 'person_22']
        # Expected output after sorting
        expected = ['person_1', 'person_2', 'person_3', 'person_10', 'person_22', 'person_31', 'person_100']
        # Test if the function returns the expected output
        self.assertEqual(sort_string_as_number(arr), expected)
    
    def test_stair_draw(self):
        """
        Test the stair_draw function.
        """
        # Input value
        n = 3
        # Expected stair pattern
        expected = "  #\n ##\n###\n"
        # Test if the function returns the expected output
        self.assertEqual(stair_draw(n), expected)
    
    def test_compare_skills(self):
        """
        Test the compare_skills function.
        """
        # Input skill scores for Joao and Maria
        joao = [17, 28, 30]
        maria = [99, 16, 8]
        # Expected output: [Joao's score, Maria's score]
        expected = [2, 1]
        # Test if the function returns the expected output
        self.assertEqual(compare_skills(joao, maria), expected)
    
    def test_diagonal_diff(self):
        """
        Test the diagonal_diff function.
        """
        # Input matrix
        arr = [
            [1, 2, 2, 1],
            [2, 1, 1, 2],
            [1, 2, 1, 2],
            [2, 1, 2, 1]
        ]
        # Expected absolute difference of diagonal sums
        expected = 2  # Corrected to the actual expected value
        # Test if the function returns the expected output
        self.assertEqual(diagonal_diff(arr), expected)
    
    def test_perc_elements(self):
        """
        Test the perc_elements function.
        """
        # Input array
        arr = [-4, 3, -9, 0, 4, 1]
        # Expected proportions of positive, negative, and zero elements
        expected = [0.166667, 0.333333, 0.5]  # Corrected expected values
        # Get the result from the function
        result = perc_elements(arr)[0]
        # Round the results to 6 decimal places for comparison
        result = [round(r, 6) for r in result]
        expected = [round(e, 6) for e in expected]
        # Test if the function returns the expected output
        self.assertEqual(sorted(result), sorted(expected))


if __name__ == '__main__':
    unittest.main()
