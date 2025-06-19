#include <iostream>
#include <vector>
#include <tuple>


// double dotProduct(const std::vector<double>& inputs, const std::vector<double>& weights);
std::vector<double> getLayerOutput(const std::vector<double>& inputs, const std::vector<std::vector<double>>& weights, const std::vector<double>& bias);

std::vector<std::vector<double>> transposition(const std::vector<std::vector<double>>& matrix);
void print_matrix(const std::vector<std::vector<double>>& matrix);


int main() {
    
    // making a single neuron
    std::vector<double> inputs{1.0, 2.0, 3.0, 2.5}; 

    // for each neuron we have multiple biases
    std::vector<std::vector<double>> weights    { {0.2, 0.8, -0.5, 1}, 
                                                {0.5, -0.91, 0.26, -0.5},
                                                {-0.26, -0.27, 0.17, 0.87}};

    
   
    std::vector<double> bias{2, 3, 0.5}; // for each neuron we have a single bias

    std::vector<double> layer_output{getLayerOutput(inputs, weights, bias)};

    for( double output : layer_output) {
        std::cout << output << "\n";
    }


    std::vector<std::vector<double>> t {transposition(weights)};
    print_matrix(t);



    return 0;
}

// double dotProduct(const std::vector<double>& inputs, const std::vector<double>&weights) {


//     // note this is just computing the dot product then adding a bias on top
//     int counter{0};
//     double sum{};
//     for(auto input : inputs) {
//         sum += input * weights[counter];
//         counter++;

//     }

//     return sum;
// }

// uses move semantics so can return
std::vector<double> getLayerOutput(const std::vector<double>& inputs, const std::vector<std::vector<double>>& weights, const std::vector<double>& bias){

    int number_of_neurons{static_cast<int>(bias.size())};
    std::vector<double> output{};

    // for (int i = 0; i < number_of_neurons; i++) {
    //     double neuron_output{dotProduct(inputs, weights[i])};
    //     neuron_output += bias[i];


    //     output.push_back(neuron_output);


    // }

    return output;
}


// std::vector<std::vector<double>> dotProduct(const std::vector<std::vector<double>> matrix1, const std::vector<std::vector<double>> matrix2) {
//     // first need to get the size of final matrix using he 
//     i


// }
std::vector<std::vector<double>> transposition(const std::vector<std::vector<double>>& matrix) {
    int row_size {static_cast<int>(matrix.size())};
    int col_size{static_cast<int>(matrix[0].size())};

    // initialize an empty matrix

    std::vector<std::vector<double>> transposition(col_size, std::vector<double>(row_size, 0));


    int col{0};
    for(int i = 0; i < col_size; i++) {
        int row {0};
        for(int j = 0; j < row_size; j++) {
            // now need to insert each cell, doing this we are going row by row
            transposition[i][j] = matrix[row][col];
            row++;
        }
        col++;
    }

    return transposition;


}

void print_matrix(const std::vector<std::vector<double>>& matrix) {
    for(std::vector<double> row : matrix) {
        for(double col : row) {
            std::cout << col << " ,";

        }

        std::cout << "\n";
    }
}



