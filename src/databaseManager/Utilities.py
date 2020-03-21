import sqlite3
import matplotlib.pyplot as plt

'''
Utilities file to interface with the database specified by its relative path
'''


def create_table(table_name, values, table_data, database_path, debug=False):
    """
    Method to create a database at database_path (if one does not already
    exist) and populate it with a table table_name with values values of type
    data_types.

    @param table_name string, the name of the table
    @param values list of string column names in table
    @param table_data list of tuples (col_name, data_type) strings
    @param database_path string, the relative path of the database
    @param debug boolean whether or not to print debug statements
    """

    conn = sqlite3.connect(database_path)
    c = conn.cursor()

    create_info = ("CREATE TABLE IF NOT EXISTS " + table_name + "(")

    for i in range(len(values)):
        val = values[i]
        val_type = table_data[i][1]

        create_info += val + " "
        create_info += val_type + ", "

    create_info = create_info[0:-2] + ")"

    if debug:
        print(create_info)

    c.execute(create_info)

    c.close()
    conn.commit()
    conn.close()


def data_entry(table_name, values, table_data, database_path, debug=False):
<<<<<<< HEAD
    """
    Insert a single row of values into table_name within DB at database_path

    :param table_name: str name of table
    :param values: list of string values for this row
    :param table_data: list of tuples (col_name, data_type) strings
    :param database_path: rel path of database
    :param debug: flag whether or not to print debug data
    """
=======
    """ Insert values into table_name in DB at database_path """
>>>>>>> 435f436e277e5a5439f3c7d1266ede8e1cd04730
    conn = sqlite3.connect(database_path)
    c = conn.cursor()

    entry_info = "INSERT INTO " + table_name + "("
    for column in table_data:
<<<<<<< HEAD
        entry_info += column[0] + ", "

    entry_info = entry_info[:-2] + ") VALUES("
=======
        entry_info += column + ", "

    entry_info = entry_info[:-2] + ") VALUES("

    data_types = list(table_data.values())
>>>>>>> 435f436e277e5a5439f3c7d1266ede8e1cd04730

    for i in range(len(values)):
        val = values[i]
        val_type = table_data[i][1]

        if val_type == "TEXT":
            entry_info += "'" + val.lower() + "', "
        else:
            val = val.replace(",", "")
            entry_info += val + ", "

    entry_info = entry_info[0:-2] + ")"

    if debug:
        print(entry_info)

    c.execute(entry_info)
    c.close()
    conn.commit()
    conn.close()


<<<<<<< HEAD
# should probably include querying methods in the prediction module - Jesus
=======
>>>>>>> 435f436e277e5a5439f3c7d1266ede8e1cd04730
def data_query(table_name, company, database_path, date_range=None, debug=False):
    """
    Query data from `company` from table `table_name` database at `database_path`

    @param table_name string, the name of the table
    @param company string, the name of the company to query
    @param database_path string, the relative path of the database
    @param date_range optional (start, end) a tuple of values to indicate date range for query
           Either start of end can be left None, corresponding to dates less or greater than
<<<<<<< HEAD
           a date, respectively. Dates must be entered in the format 'm-d-YYYY'
=======
           a date, respectively. Dates must be entered in the format m-d-YYYY
>>>>>>> 435f436e277e5a5439f3c7d1266ede8e1cd04730
    @param debug boolean whether or not to print debug statements
    @return An array of tuples representing query results
    """

    conn = sqlite3.connect(database_path)
    c = conn.cursor()

    entry_info = "SELECT * from " + table_name + " WHERE COMPANY = '" + company.lower() + "'"

    if date_range is not None:
        if date_range[0] is not None and date_range[1] is not None:
            entry_info += " AND date_stamp BETWEEN '" + date_range[0] + "' and '" + date_range[1] + "'"
        elif date_range[0] is not None:
            entry_info += " AND date_stamp >= '" + date_range[0] + "'"
        elif date_range[1] is not None:
            entry_info += " AND date_stamp <= '" + date_range[1] + "'"

    if debug:
        print(entry_info)

    data = c.execute(entry_info)
    ret_data = [row for row in data]

    conn.close()
    return ret_data


def create_scatterplot(company, dates, y_values):
    """
    Create a scatter plot plotting `dates` against `y_values`

    @param company: The name of the company to plot
    @param dates: An array of date strings in the format 'm-d-YYYY'
            ex: ['3-20-2020', '3-21-2020']
    @param y_values: An array of values to plot
    """

    # plot
    plt.title(company)
    plt.xlabel("Date")
    plt.ylabel("Stock Price")
    plt.scatter(dates, y_values)
    plt.show()
