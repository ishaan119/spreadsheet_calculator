import re
import sys


def parse_spreadsheet_data():
    columns, rows = sys.stdin.readline().strip().split()
    columns = int(columns)
    rows = int(rows)
    expressions = []
    for _ in range(rows * columns):
        expressions.append(sys.stdin.readline().strip())

    return rows, columns, expressions


def evaluate_expression(
        cell, cell_to_expression_dict, evaluated_cell_values, visited_cells):
    valid_operators = ['*', '/', '+', '-']
    if cell in evaluated_cell_values:
        return evaluated_cell_values[cell]

    # If cell is already visited in an expression it is a cyclic dependencies
    if cell in visited_cells:
        print(
            "Cyclic dependency found for cell: {0} in expression: {1}".format(
                cell, cell_to_expression_dict[cell]))
        sys.exit(1)

    # In recursive calls if cell we can find the cell
    visited_cells.append(cell)
    expression = cell_to_expression_dict[cell]

    tokens = expression.split()
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(float(token))
        elif re.match(r'^[A-Z]+\d+$', token):
            # It is a reference to a cell and resolve it recursively
            value = evaluate_expression(
                token, cell_to_expression_dict, evaluated_cell_values, visited_cells)
            # An expression can have multiple References hence need to add to the stack
            stack.append(value)
        elif token in valid_operators:
            # Pop two values from the stack
            # Important to note that since expression are evaluated
            # right to left second term is popped first
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                # Check for divide by 0
                if b == 0:
                    print("Invalid Division 0 found for expression: {0}".format(expression))
                    sys.exit(1)
                stack.append(a / b)
        else:
            print("Invalid operator found: {0}. Supported operators: {1}".format(token, valid_operators))

    result = stack.pop()
    evaluated_cell_values[cell] = result
    visited_cells.remove(cell)
    return result


def main():
    # Parsing input for row and column value and expressions
    rows, columns, expressions = parse_spreadsheet_data()

    # Cell Names using row and columns
    cells = []
    for row in range(rows):
        for column in range(columns):
            # Use Ascii Values UpperCase
            cells.append("{0}{1}".format(chr(65 + row), column + 1))

    cell_to_expression_dict = {}
    cells_len = len(cells)
    for i in range(cells_len):
        cell_to_expression_dict[cells[i]] = expressions[i]

    results = []
    evaluated_cell_values = {}
    visited_cells = []
    for cell in cells:
        cell_value = float(
            evaluate_expression(
                cell, cell_to_expression_dict, evaluated_cell_values, visited_cells))
        results.append(f"{cell_value:.5f}")

    # Output the results in the required format
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
