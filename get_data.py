from PIL import Image
import numpy as np


def print_image(filepath) -> None:

    img = Image.open(filepath)
    arr = np.array(img)

    alpha = arr[:, :, 3] # getting the alpha channel
    for row in alpha:
        for col in row:
            if col != 0:
                print(1,' ', end='')
            else:
                print(col, ' ', end='')
        print()



def write_data(filename, folder_path) -> None:
    '''
    Args:
    Filename: the name of the file to write to
    folder_path: the relvative path to the folder with the training pngs
    
    '''
    number_of_samples = 8000 # for each number we will have 8000 training examples, the rest will be used to check the network
    with open(filename, 'a') as af:
        for i in range(number_of_samples):
            image_file = f'{folder_path}{i}.png'

            img = Image.open(image_file)
            arr = np.array(img)


            alpha = arr[:, :, 3] # getting the alpha channel
            for row in alpha:
                for col in row:
                    if col != 0:
                        af.write('1')
                    else:
                        af.write('0')
            af.write('\n')
            

def read_data(filename, row_num) -> np.array:
    '''
    Args
    Filename: The name of the file containing the data
    row_num: The index of the row to read

    Returns:
    A numpy representation a single entry of the data, a 1D vector
    '''
    
    with open(filename) as rf:
        for index, line in enumerate(rf):
            if index == row_num:

                return np.array([int(char) for char in line[:-1]])


def print_data(arr: np.array) -> None:
    dimension = 28

    arr = arr[:-1]

    matrix = []
    row = []
    for i, num in enumerate(arr):
        row.append(int(num))
        if i % dimension == 0:
            matrix.append(row)
            row = []
            
            
    
    for row in matrix:
        print(row)


        

if __name__ == '__main__':

    # each row is 28 x 28 string representation of the data (784)
    data_filename = 'nine_data.txt'
    folder_path = 'archive/dataset/9/9/'

    write_data(data_filename, folder_path)
    
    arr = read_data(data_filename, 6784)
    print_data(arr)

    


