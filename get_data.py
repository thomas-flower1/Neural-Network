from PIL import Image
import numpy as np
import os


def print_image(filepath: str) -> None:
    '''
    Takes the relative path of a 28x28 png image of prints it to the console

    Args:
    filepath: The relative path for the image png, example would be: 'archive/dataset/0/0/0.png'

    Returns:
    n/a
    '''

    img = Image.open(filepath)
    arr = np.array(img)

    alpha = arr[:, :, 3] # getting the alpha channel
    for row in alpha:
        for col in row:
            if col != 0:
                print(1,' ', end='')
            else:
                print(' ', ' ', end='')
        print()



def write_data(filename: str, folder: str) -> None:
    '''
    Turns image pngs into a vector of 0s and 1s from the alpha channel,
    It then writes these values into the specified file

    Args:
    Filename: the name of the file to write to
    folder_path: the relvative path to the folder with the training pngs, Example: archive/dataset/0/0/
    number_of_sample: the number of samples in the training set folder

    Returns:
    n/a
    
    '''
    files = [f'{folder}/{file.name}' for file in os.scandir(folder) if file.is_file()]
    with open(filename, 'a') as af:
        for file in files:
            img = Image.open(file)
            matrix = np.array(img)

            alpha = matrix[:, :, 3] # getting the alpha channel
            for row in alpha:
                for col in row:
                    if col != 0:
                        af.write('1')
                    else:
                        af.write('0')
            af.write('\n')
            

def read_data(filename: str) -> np.array:
    '''
    Returns a matrix where each row is a sample from the dataset


    Args
    Filename: The name of the file containing the data
  

    Returns:
    A matrix of where each row is a piece of data 
    '''
    
    matrix = []
    with open(filename) as rf:
        for line in rf:
            matrix.append(np.array([int(char) for char in line[:-1]]))
    
    return np.array(matrix)


def print_array_image(arr: np.array) -> None:
    '''
    Given the vector containting the image, prints out the image again as a matrix to the console

    Args:
    arr: A vector, availble from the data files, that contains the data of the image

    Returns
    n/a

    
    '''
    dimension = 28
    arr = arr[:-1] # get rid of the newline char

    matrix = []
    row = ' '
    for i, num in enumerate(arr):
        if num != 1:
            row = row + ' '
        else:
            row = row + '1'
        if i % dimension == 0:
            matrix.append(row)
            row = ''
            
            
    for row in matrix:
        print(str(row))
    
def arr_to_matrix(arr):
    matrix = arr.reshape(28, 28)
    return matrix
            


def shift_left(arr, shift_amount):
    '''Takes in an array of 0s and 1s and shifts the images by a certan amount of pixels to the right'''

    matrix = arr_to_matrix(arr)
    solution = []
    for row in matrix:
        r = []
        for col in row:
            r.append(col)
        
        for _ in range(shift_amount):
            r.append(0)
            r.pop(0)
        
        solution.append(r)
    
    solution = np.array(solution).flatten()
    
    return solution

def shift_right(arr, shift_amount):
    '''Takes in an array of 0s and 1s and shifts the images by a certan amount of pixels to the right'''

    matrix = arr_to_matrix(arr)
    solution = []
    for row in matrix:
        r = []
        for col in row:
            r.append(col)
        
        for _ in range(shift_amount):
            r.insert(0, 0)
            r.pop()
        
        solution.append(r)
    
    solution = np.array(solution).flatten()
    return solution

def shift_up(arr, shift_amount):
    matrix = list(arr_to_matrix(arr))
    for _ in range(shift_amount):
        matrix.pop(0)
        matrix.append([0 for _ in range(len(matrix[0]))])
    
    return np.array(matrix).flatten()


def shift_down(arr, shift_amount):
    matrix = list(arr_to_matrix(arr))
    for _ in range(shift_amount):
        matrix.pop(-1)
        matrix.insert(0, ([0 for _ in range(len(matrix[0]))]))
    
    return np.array(matrix).flatten()


if __name__ == '__main__':
    '''
    When given a png and want to convert to an array for the file
    Used write_data()

    If want to augment the date
    - read the data into a matrix read_data()
    - iterate over the data and call corresponding shift function

    '''

    pass


    # pathname = 'UI samples data/zero_data.txt'
    # copy = 'UI samples data/zero_data copy.txt'

    # # #Augmenting my data
    # all_data = read_data(copy)
    # with open(pathname, 'a') as af:
    #     for data in all_data:
    #         right = shift_up(data, 3) # this is a numbpy array
    #         left = shift_down(data, 3)
    #         for number in right:
    #             af.write(str(number))
    #         af.write('\n')
    #         for number in left:
    #             af.write(str(number))
    #         af.write('\n')
    
    
    
    
            
        
   
  
