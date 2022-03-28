"""Dictionary related utility functions."""

__author__ = "730502223"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # prepare to read the data file as a csv rather than just strings
    csv_reader = DictReader(file_handle)
    # read each row of the csv line by line
    for row in csv_reader:
        result.append(row)
    
    # close the file to free its resources.
    file_handle.close()
    return result 


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_based_table: dict[str, list[str]], num_row: int) -> dict[str, list[str]]:
    """Creates a new table based on columns with the first n rows of data for each column."""
    result_dict: dict[str, list[str]] = {}
    for column in column_based_table:
        store_n_values: list[str] = []
        if num_row > len(column_based_table[column]):
            return column_based_table
        for n in range(0, num_row):
            item: str = (column_based_table[column])[n]
            store_n_values.append(item)
        result_dict[column] = store_n_values
    return result_dict


def select(new_column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Creates a new column-based table with a specific subset of the original columns."""
    returned_dict: dict[str, list[str]] = {}
    for column in column_names:
        returned_dict[column] = new_column_table[column]
    return returned_dict


def concat(first_column: dict[str, list[str]], second_column: dict[str, list[str]]) -> dict[str, list[str]]:
    """Creates a column-based table with two combined column-based tables."""
    empty_dict: dict[str, list[str]] = {}
    for column in first_column:
        empty_dict[column] = first_column[column]
    for column in second_column:
        if column in empty_dict:
            empty_dict[column] += second_column[column]
        else:
            empty_dict[column] = second_column[column]
    return empty_dict


def count(frequency_count: list[str]) -> dict[str, int]:
    """Given a list, the function creates a dict where the value is the count of the occurence of the key."""
    empty: dict[str, int] = {}
    for value in frequency_count:
        if value in frequency_count:
            empty[value] += 1
        else:
            empty[value] = 1
    return empty