from nnfs.datasets import spiral_data
import nnfs

nnfs.init()

x, y = spiral_data(samples=100, classes=3)

# we are creating 3 classes each with 100 samples

# lets put our data into 3 separate files for our c++
for i in range(len(x)):
    if i >= 200:
      
        # we want to add to class 1
        with open("class1.csv", 'a') as af:
            # need to format quickly
            af.write(f'{x[i][0]},{x[i][1]}\n')
    elif i >= 100:
        with open("class2.csv", 'a') as af:
            af.write(f'{x[i][0]},{x[i][1]}\n')
    else:
        with open("class3.csv", 'a') as af:
            af.write(f'{x[i][0]},{x[i][1]}\n')
            
   





