import numpy as np

def description():
    program_description = """
    This program creates a tensor of 5 dimensions
    """
    return program_description

def tensor5():
    dimension = int(input('Choose dimension (s) of the array: '))
    tensor = np.array([1,2,3],ndmin=dimension)
    return tensor

array_= tensor5()

def dimensions():
    dim = array_.ndim
    return dim

dimens = dimensions()

def show_array():
    print(array_)
    message1= f'The array created has {dimens} dimensions'
    print(message1)
    

# add one dimension on axis 1
def add_dimension():
    axe = int(input('Choose (1) if you want to add col, or (0) if you want to add row: '))
    expand = np.expand_dims(array_,axis=axe)
    return expand

array_expanded = add_dimension()

def show_new_array():
    print(array_expanded)
    message1= f'The new array has {dimens+1} dimensions'
    print(message1)


def run():
    print(description())
    show_array()
    show_new_array()


if __name__ == "__main__":
    run()