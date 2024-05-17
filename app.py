from flask import Flask, render_template, request
from tests import TestFunctions
import unittest
from io import StringIO
from functions import sort_string_as_number, stair_draw, compare_skills, diagonal_diff, perc_elements
import matplotlib.pyplot as plt
def run_tests():
    """
    Run unit tests and return the results as a string.
    """
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestFunctions)
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=2)
    result = runner.run(suite)
    stream.seek(0)
    return stream.read()

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the index.html template.
    """
    return render_template('index.html')

@app.route('/sort_string_as_number')
def sort_string_as_number_route():
    """
    Route for the sort_string_as_number function.
    Input: None
    Output: Rendered HTML template with sorted array of strings.
    """
    arr = ['person_1', 'person_2', 'person_3', 'person_10', 'person_100', 'person_31', 'person_22']
    sorted_arr = sort_string_as_number(arr)
    return render_template('sort_string_as_number.html', sorted_arr=sorted_arr)

@app.route('/stair_draw')
def stair_draw_route():
    """
    Route for the stair_draw function.
    Input: None
    Output: Rendered HTML template with stair pattern.
    """
    n = 3
    result = stair_draw(n)
    return render_template('stair_draw.html', result=result)

@app.route('/compare_skills')
def compare_skills_route():
    """
    Route for the compare_skills function.
    Input: None
    Output: Rendered HTML template with comparison results.
    """
    joao = [17, 28, 30]
    maria = [99, 16, 8]
    result = compare_skills(joao, maria)
    return render_template('compare_skills.html', result=result)

@app.route('/diagonal_diff')
def diagonal_diff_route():
    """
    Route for the diagonal_diff function.
    Input: None
    Output: Rendered HTML template with diagonal difference result.
    """
    arr = [
        [1, 2, 2, 1],
        [2, 1, 1, 2],
        [1, 2, 1, 2],
        [2, 1, 2, 1]
    ]
    result = diagonal_diff(arr)
    return render_template('diagonal_diff.html', result=result)

@app.route('/perc_elements')
def perc_elements_route():
    """
    Route for the perc_elements function.
    Input: None
    Output: Rendered HTML template with proportion results and a pie chart.
    """
    arr = [-4, 3, -9, 0, 4, 1]
    result, image_base64 = perc_elements(arr)
    description = """
    Function: perc_elements
    Input: {}
    Output: {}
    Description: Given an array of integers, the function calculates the proportion of positive, negative, and zero elements.
    Returns an array with the proportion of each type, with precision of 6 decimal places.
    """.format(arr, result)
    return render_template('perc_elements.html', result=result, description=description, image_base64=image_base64)

@app.route('/tests_results')
def tests_results():
    """
    Route for displaying test results.
    Input: None
    Output: Rendered HTML template with test results.
    """
    results = run_tests()
    return render_template('tests_results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
