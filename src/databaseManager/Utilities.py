import sqlite3

'''
Utilities file to interface with the database specified by its relative path
'''


def create_table(table_name, values, data_types, database_path, debug=False):
    """
    Method to create a database at database_path (if one does not already
    exist) and populate it with a table table_name with values values of type
    data_types.

    @param table_name string, the name of the table
    @param values list of string column names in table
    @param data_types list of equal size to values of column data type strings
    @param database_path string, the relative path of the database
    @param debug boolean whether or not to print debug statements
    """

    conn = sqlite3.connect(database_path)
    c = conn.cursor()

    create_info = ("CREATE TABLE IF NOT EXISTS " + table_name + "(")

    for i in range(len(values)):
        val = values[i]
        val_type = data_types[i]

        create_info += val + " "
        create_info += val_type + ", "

    create_info = create_info[0:-2] + ")"

    if debug:
        print(create_info)

    c.execute(create_info)

    c.close()
    conn.commit()
    conn.close()


def data_entry(table_name, values, data_types, database_path, debug=False):
    """ Insert values into table_name in DB at database_path """
    conn = sqlite3.connect(database_path)
    c = conn.cursor()

    entry_info = ("INSERT INTO " + table_name + " VALUES(")

    for i in range(len(values)):
        val = values[i]
        val_type = data_types[i]

        if val_type == "TEXT":
            entry_info += "'" + val + "', "
        else:
            entry_info += val + ", "

    entry_info = entry_info[0:-2] + ")"

    if debug:
        print(entry_info)

    c.execute(entry_info)
    c.close()
    conn.commit()
    conn.close()

