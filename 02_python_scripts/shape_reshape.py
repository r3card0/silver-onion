import numpy as np

def description():
    program_description = """
    This program shows how to use shape and reshape
    """
    return program_description

def determine_row():
    row_ = int(input('Set number of rows: '))
    return row_

def determine_column():
    col_ = int(input('Set number of columns: '))
    return col_

row_ = determine_row()
col_ = determine_column()


def create_array():
    arr_ = np.random.randint(1,10,(row_,col_))
    return arr_

def shape():
    shape_ = create_array().shape
    return shape_

def run():
    print(create_array())
    print(shape())


if __name__ == "__main__":
    run()