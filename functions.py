import matplotlib.pyplot as plt
import io
import base64
def sort_string_as_number(arr):
    # Sorts the input array based on the number suffix in each string element
    return sorted(arr, key=lambda x: int(x.split('_')[1]))

def stair_draw(n):
    # Generates a string representing a staircase of height 'n' using '#' symbols
    return '\n'.join(' ' * (n - i - 1) + '#' * (i + 1) for i in range(n)) + '\n'

def compare_skills(joao, maria):
    # Compares the skills of two persons and returns the points earned by each
    joao_points = sum(1 for j, m in zip(joao, maria) if j > m)
    maria_points = sum(1 for j, m in zip(joao, maria) if j < m)
    return [joao_points, maria_points]

def diagonal_diff(arr):
    # Calculates the absolute difference between the sums of primary and secondary diagonals in a square matrix
    primary_diagonal = sum(arr[i][i] for i in range(len(arr)))
    secondary_diagonal = sum(arr[i][len(arr) - i - 1] for i in range(len(arr)))
    return abs(primary_diagonal - secondary_diagonal)

def perc_elements(arr):
    # Calculates the proportion of positive, negative, and zero elements in an array
    total_elements = len(arr)
    positive_count = len([x for x in arr if x > 0])
    negative_count = len([x for x in arr if x < 0])
    zero_count = len([x for x in arr if x == 0])

    positive_ratio = positive_count / total_elements
    negative_ratio = negative_count / total_elements
    zero_ratio = zero_count / total_elements

    ratios = [positive_ratio, negative_ratio, zero_ratio]
    labels = ['Positives', 'Negatives', 'Zeros']

    # Generates a pie chart
    fig, ax = plt.subplots()
    ax.pie(ratios, labels=labels, autopct='%1.2f%%', startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Saves the pie chart image as a base64-encoded string
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close()

    return ratios, image_base64
