import tkinter as tk
import numpy as np
from nn import Neuron, Layer, Data, Relu, Softmax, Loss

#window
window_size = '800x600'
title = "Neural Network"

window = tk.Tk()
window.geometry(window_size)
window.title(title)
window.configure(bg='white')

# TODO neat font
font = ('Arial', 32)
text_font = ('Arial', 16)

# heading
heading = tk.Label(window, text=title, bg='white', font=font, pady=10)
heading.pack()


prediction_text = tk.StringVar()
prediction_text.set('Prediction: ')
prediction = tk.Label(window, textvariable=prediction_text, bg='white', font=text_font)
prediction.place(x = 500, y = 100)


matrix_size = 28
matrix = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]

# Neural network
input_size = 784
   
layer1 = Layer(128, input_size)
layer2 = Layer(10, 128)

# activation functions
relu = Relu()
softmax = Softmax()


# saves
weights_save_1 = 'weights1.csv'
weights_save_2 = 'weights2.csv'

bias_save_1 = 'bias1.csv'
bias_save_2 = 'bias2.csv'



layer1.load(weights_save_1, bias_save_1)
layer2.load(weights_save_2, bias_save_2)


def draw_border():

    pixel_size = 16
    padding_width = 3
    line_width = 22
    line_height = 22

    start_x = pixel_size * padding_width
    start_y = pixel_size * padding_width

    # drawing the top line
    for _ in range(line_width):
        canvas.create_rectangle(start_x, start_y, start_x + pixel_size, start_y + pixel_size, fill='red', outline='')
        start_x += 16
    
    start_y = pixel_size * 24 # 24 is the y of the bottom left
    start_x = pixel_size * padding_width

    # drawing the bottom line
    for _ in range(line_width):
        canvas.create_rectangle(start_x, start_y, start_x + 16, start_y + 16, fill='red', outline='')
        start_x += 16
    
    # draw the right line
    start_x = pixel_size * padding_width
    start_y = pixel_size * padding_width
    for _ in range(line_width):
        canvas.create_rectangle(start_x, start_y, start_x + 16, start_y + 16, fill='red', outline='')
        start_y += pixel_size
    
    # draw the left line
    start_x = pixel_size * 24
    start_y = pixel_size * padding_width
    for _ in range(line_width):
        canvas.create_rectangle(start_x, start_y, start_x + 16, start_y + 16, fill='red', outline='')
        start_y += pixel_size

        

def draw_pixel(event):
  
    # position in the matrix
    pixel_size = 16


    x = event.x // pixel_size
    y = event.y // pixel_size

    if (y > 3 ) and y < 24 and x > 3 and x < 24: # prevents from drawing above or below the top and bottom border lines
      
        if x < 28 and y < 28: # ensuring drawing on the screen
            matrix[y][x] = 1

  
            top_right_x = x * pixel_size
            top_right_y = y * pixel_size

            bottom_left_x = top_right_x + pixel_size
            bottom_left_y = top_right_y + pixel_size
        
            canvas.create_rectangle(top_right_x, top_right_y, bottom_left_x, bottom_left_y, fill='black')
    
    nn()


def nn(event=None):
    

    # need to turn matrix into a row
    input  = [int(col) for row in matrix for col in row]
    input = np.array([input]).flatten()

    # check if the input array is all 0's
    if np.all(input == 0):
        return


    # nn
    layer1.forward(input)
    relu.forward_layer(layer1.output)
    layer2.forward(relu.output)
    softmax.forward(layer2.output)

    out = np.argmax(softmax.output)

    t = f'Prediction: {out}'

    s = [round(float(num), 2) * 100 for num in softmax.output]

    for i, text in enumerate(accuracy_text):
        text.set(f'{i}: {s[i]:.2f}%')
   
    prediction_text.set(t)

    # pathname = 'test9.txt'
    # add_training_example(pathname, input)
    # clear_canvas() # used for imputting the data set



   

   



def clear_canvas():
    global matrix
    global matrix_size

    canvas.delete('all')

    # also need to clear the matrix
    matrix = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]

    draw_border() # also need to draw the border back


def add_training_example(filename, arr):
    with open(filename, 'a') as af:

        arr = [str(num) for num in arr] # convert matrix into 1d array
       
        s = ''.join(arr)
        af.write(s)
        af.write('\n')

     
    


# canvas
pixel_size = 16
canvas_dimension = 28 * pixel_size
canvas = tk.Canvas(window, width=canvas_dimension-1, height=canvas_dimension-1, bg='#f5f3f4', highlightthickness=2, highlightbackground='black')
canvas.place(x=20, y=76 + 20)

canvas.bind("<ButtonPress-1>", draw_pixel)
canvas.bind('<B1-Motion>', draw_pixel)

draw_border()



# TODO send button
send_button = tk.Button(window, text='Send', font=('Arial', 18), command=nn, relief='flat', bg='#2E8B57', fg='white', padx=5, pady=5)
send_button.place(x = 500 + 5, y = 140)


# TODO reset button
reset_button = tk.Button(window, text='Clear', command=clear_canvas, font=('Arial', 18), bg='#2E8B57', relief='flat', fg='white', activebackground='#2E8B57', activeforeground='white', padx=5, pady=5)
reset_button.place(x = 500 + 5, y = 480)

# Press the enter key
window.bind('<Return>', nn)

# Number labels
zero_text = tk.StringVar()
zero_text.set('0: 0%')
zero = tk.Label(window, textvariable=zero_text, font=('Arial', 16), bg='white')
zero.place(x= 500, y = 210)

one_text = tk.StringVar()
one_text.set('1: 0%')
one = tk.Label(window, textvariable=one_text, font=('Arial', 16), bg='white')
one.place(x= 500, y = 250)

two_text = tk.StringVar()
two_text.set('2: 0%')
two = tk.Label(window, textvariable=two_text, font=('Arial', 16), bg='white')
two.place(x= 500, y = 290)

three_text = tk.StringVar()
three_text.set('3: 0%')
three = tk.Label(window, textvariable=three_text, font=('Arial', 16), bg='white')
three.place(x= 500, y = 330)

four_text = tk.StringVar()
four_text.set('4: 0%')
four = tk.Label(window, textvariable=four_text, font=('Arial', 16), bg='white')
four.place(x= 500, y = 370)

five_text = tk.StringVar()
five_text.set('5: 0%')
five = tk.Label(window, textvariable=five_text, font=('Arial', 16), bg='white')
five.place(x= 650, y = 210)

six_text = tk.StringVar()
six_text.set('6: 0%')
six = tk.Label(window, textvariable=six_text, font=('Arial', 16), bg='white')
six.place(x= 650, y = 250)

seven_text = tk.StringVar()
seven_text.set('7: 0%')
seven = tk.Label(window, textvariable=seven_text, font=('Arial', 16), bg='white')
seven.place(x= 650, y = 290)

eight_text = tk.StringVar()
eight_text.set('8: 0%')
eight = tk.Label(window, textvariable=eight_text, font=('Arial', 16), bg='white')
eight.place(x= 650, y = 330)

nine_text = tk.StringVar()
nine_text.set('9: 0%')
nine = tk.Label(window, textvariable=nine_text, font=('Arial', 16), bg='white')
nine.place(x= 650, y = 370)

accuracy_text = [zero_text, one_text, two_text, three_text, four_text, five_text, six_text, seven_text, eight_text, nine_text]




window.mainloop()