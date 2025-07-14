import tkinter as tk
import numpy as np
from nn import Neuron, Layer, Data, Relu, Softmax, Loss
from get_data import print_array_image, read_data


window_size = '800x600'
title = "Neural Network"

window = tk.Tk()
window.geometry(window_size)
window.title(title)
window.configure(bg='white')

font = ('Arial', 32)
text_font = ('Arial', 16)

# heading
heading = tk.Label(window, text=title, bg='white', font=font, pady=10)
heading.pack()


prediction_text = tk.StringVar()
prediction_text.set('Prediction: ')
prediction = tk.Label(window, textvariable=prediction_text, bg='white', font=text_font)
prediction.place(x = 500, y = 100)



matrix = [[0 for _ in range(28)] for _ in range(28)]



def draw_pixel(event):
  
    # position in the matrix
    x = event.x // 16 
    y = event.y // 16 

    matrix[y][x] = 1


    top_right_x = x * 16
    top_right_y = y * 16

    bottom_left_x = top_right_x + 16
    bottom_left_y = top_right_y + 16

    canvas.create_rectangle(top_right_x, top_right_y, bottom_left_x, bottom_left_y, fill='black')

count = 0
correct = 0
def nn(event=None):
    global correct
    global count

    # need to turn matrix into a row
    input  = []
    for row in matrix:
        for col in row:
            input.append(int(col))
    
    input = np.array([input]).flatten()

    # check if the input array is all 0's
    if np.all(input == 0):
        return

    # Adding new training data
    pathname = 'three.txt'
    add_training_example(pathname, input)


    # nn
    input_size = 784
   
    layer1 = Layer(128, input_size)
    layer2 = Layer(10, 128)

    # activation functions
    relu = Relu()
    softmax = Softmax()


    # saves
    savefile1 = 'selfweights1.csv'
    savefile2 = 'selfweights2.csv'
    # savefile1 = 'layer1weights.csv'
    # savefile2 = 'layer2weights.csv'


    layer1.load(savefile1)
    layer2.load(savefile2)

    # forwarding
    layer1.forward(input)
    relu.forward_layer(layer1.output)
    layer2.forward(relu.output)
    softmax.forward(layer2.output)

    out = np.argmax(softmax.output)
    t = f'Prediction: {out}'

    prediction_text.set(t)
    clear_canvas()

   



def clear_canvas():
    global matrix
    canvas.delete('all')

    # also need to clear the matrix
    matrix = [[0 for _ in range(28)] for _ in range(28)]


def add_training_example(filename, arr):
    with open(filename, 'a') as af:

        arr = [str(num) for num in arr]
       
        s = ''.join(arr)
        af.write(s)
        af.write('\n')

     
    


# canvas
pixel_size = 16
canvas_dimension = 28 * pixel_size
canvas = tk.Canvas(window, width=canvas_dimension, height=canvas_dimension, bg='#f5f3f4', highlightthickness=2, highlightbackground='black')
canvas.place(x=20, y=76 + 20)

canvas.bind("<ButtonPress-1>", draw_pixel)
canvas.bind('<B1-Motion>', draw_pixel)




# TODO send button
send_button = tk.Button(window, text='Send', font=('Arial', 18), command=nn, relief='flat', bg='#2E8B57', fg='white', padx=5, pady=5)
send_button.place(x = 500 + 5, y = 140)


# TODO reset button
reset_button = tk.Button(window, text='Clear', command=clear_canvas, font=('Arial', 18), bg='#2E8B57', relief='flat', fg='white', activebackground='#2E8B57', activeforeground='white', padx=5, pady=5)
reset_button.place(x = 500 + 5, y = 480)

# Press the enter key
window.bind('<Return>', nn)





window.mainloop()