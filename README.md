# Flask Application for Function Testing and Results Display

This Flask application provides a web interface to run various functions, display their results, and show the outcomes of unit tests.

## Functions

### 1. Sort String as Number
- **Description**: Accepts an array of strings where each string starts with 'person_' followed by a number. The function returns the array sorted by the numbers.
- **Example Input**: `['person_1', 'person_2', 'person_3', 'person_10', 'person_100', 'person_31', 'person_22']`
- **Example Output**: `['person_1', 'person_2', 'person_3', 'person_10', 'person_22', 'person_31', 'person_100']`

### 2. Stair Draw
- **Description**: Accepts an integer that defines the base size of a staircase and draws the staircase using the '#' symbol.
- **Example Input**: `3`
- **Example Output**:
    ```
      #
     ##
    ###
    ```

### 3. Compare Skills
- **Description**: Accepts two arrays of integers, each containing 3 elements representing skills. Compares the skills and returns an array with the points of each person.
- **Example Input**: `[17, 28, 30]`, `[99, 16, 8]`
- **Example Output**: `[1, 2]`

### 4. Diagonal Difference
- **Description**: Calculates the absolute difference between the sums of the diagonals of a square matrix.
- **Example Input**: `[[1, 2, 2, 1], [2, 1, 1, 2], [1, 2, 1, 2], [2, 1, 2, 1]]`
- **Example Output**: `2`

### 5. Percentage of Elements
- **Description**: Calculates the proportion of positive, negative, and zero elements in an array with a precision of 6 decimal places.
- **Example Input**: `[-4, 3, -9, 0, 4, 1]`
- **Example Output**: `[0.500000, 0.333333, 0.166667]`

## Running the Application

1. Install Flask:
    ```bash
    pip install Flask
    ```

2. Run the application:
    ```bash
    python app.py
    ```

3. Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Running Tests

1. To run the tests, navigate to `http://127.0.0.1:5000/tests_results`.

## Directory Structure

- `app.py`: Main application file.
- `functions.py`: Contains the implementations of the functions.
- `tests.py`: Contains the unit tests for the functions.
- `templates/`: Contains the HTML templates for the Flask routes.
- `README.md`: This file.

## Dependencies

- Flask
- unittest
