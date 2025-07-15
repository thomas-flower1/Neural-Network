from PIL import Image
import numpy as np


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



def write_data(filename: str, folder_path: str, number_of_samples: int=10000) -> None:
    '''
    Turns image pngs into a vector of 0s and 1s from the alpha channel,
    It then writes these values into the specified file

    Args:
    Filename: the name of the file to write to
    folder_path: the relvative path to the folder with the training pngs, Example: archive/dataset/0/0/
    number_of_sample: the number of samples in the training set folder

    Note this assums the filenames in the folder are like: 0.png, 100.png etc


    Returns:
    n/a
    
    '''
  
    with open(filename, 'a') as af:
        for i in range(number_of_samples):
            image_file = f'{folder_path}{i}.png'

            img = Image.open(image_file)
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
    Returns a matrix where each row is a sample ftom thr dataset


    Args
    Filename: The name of the file containing the data
    row_num: The index of the row to read

    Returns:
    A numpy representation a single entry of the data, a 1D vector
    '''
    
    matrix = []
    # TODO update
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


        

if __name__ == '__main__':
    # write_file = 'one_data.txt'
    # folder_path = 'archive/dataset/9/9/'
    # write_data(write_file, folder_path)

    # arr = read_data(write_file)
    # print_array_image(arr[5000])

    matrix = read_data('nine.txt')[200:220]
    
    for row in matrix:
        print_array_image(row)



