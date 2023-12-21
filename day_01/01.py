import pandas as pd

def solve():
    """Solve the first challenge of the first day."""
    # Read the input file into a dataframe
    df = pd.read_csv('day_01/input.txt', header=None, names=['Text'])
    # Add a column to the dataframe that indicates if the text contains at least two digits
    df['ContainsDigits'] = df['Text'].str.contains(r'\d.*\d')

    def get_coordinate(row):
        """
        Extract the coordinates from the row.

        :param row: The row to extract the coordinates from.
        :return: The extracted coordinates.
        """
        # Rows that contain at least two digits
        if row['ContainsDigits']:
            digits = [char for char in row['Text'] if char.isdigit()]
            if digits:
                # The first and the last digits from the input
                return int(f"{digits[0]}{digits[-1]}")
        # Rows that only contain one digit
        # This assumes that there is at least one digit in the row, but this is true for the input
        elif not row['ContainsDigits']:
            digits = [char for char in row['Text'] if char.isdigit()]
            if digits:
                # The only digit in the input repeated
                return int(f"{digits[0]}{digits[0]}")

    # Apply the function to the dataframe to get the coordinates
    df['Coordinate'] = df.apply(get_coordinate, axis=1)
    # Print the result
    print(df['Coordinate'].sum())
    

if __name__ == '__main__':
    solve()