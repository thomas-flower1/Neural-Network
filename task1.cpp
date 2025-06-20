#include <iostream>
#include <vector>
#include <tuple>


// double dotProduct(const std::vector<double>& inputs, const std::vector<double>& weights);
std::vector<double> vector_matrix_product(const std::vector<std::vector<double>>& matrix, const std::vector<double>& vector);
std::vector<std::vector<double>> transposition(const std::vector<std::vector<double>>& matrix);
auto matrix_product(const std::vector<std::vector<double>> matrix1, const std::vector<std::vector<double>> matrix2);



void print_vector(const auto& vector);
void print_matrix(const std::vector<std::vector<double>>& matrix);


int main() {
    
    // making a single neuron

    std::vector<double> test_vector{1, 2, 3};
    std::vector<std::vector<double>> test_matrix{{1, 2, 3},
                                              {4, 5, 6}};

    auto t {vector_matrix_product(test_matrix, test_vector)};

    print_vector(t);

    

    return 0;
}


std::vector<double> vector_matrix_product(const std::vector<std::vector<double>>& matrix, const std::vector<double>& vector){

    int matrix_height{static_cast<int>(matrix.size())};
    int matrix_width{static_cast<int>(matrix[0].size())};

    // create an empty matrix
    std::vector<double> product {}; // syntax for initializing an empty list , does not assign it a garbage value



    /*
    [1 2] . [1] = 1 [1] + 2 [2]
    [3 4] . [2]     [3]     [4]

    [1 2]   [1]     [1]     [2]
    [2 4] . [2] = 1 [2] + 2 [4]
    [5 6]   [3]     [5]     [6]
    
    
    
    */

    int vector_size{static_cast<int>(vector.size())};

    for(int row = 0; row < matrix_height; row++) {
        
        double sum {0}; 

        for(int j = 0; j < vector_size; j++) {
            sum += vector[j] * matrix[row][j];
        }
        product.push_back(sum); // can just append to the back

    }

    return product;

    




}


auto matrix_product(const std::vector<std::vector<double>> matrix1, const std::vector<std::vector<double>> matrix2) {
    // first need to get the size of final matrix using he 
    int matrix_1_height{static_cast<int>(matrix1.size())}; 
    int matrix_1_width{static_cast<int>(matrix1[0].size())};

    int matrix_2_height{static_cast<int>(matrix2.size())};
    int matrix_2_width{static_cast<int>(matrix2[0].size())};

    // need to make an empty matrix
    if(matrix_1_width != matrix_2_height){
        return;

    }

    // need to make an empty matrix
    std::vector<std::vector<double>> product(matrix_1_height, std::vector<double>(0, matrix_2_height));








}
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

void print_vector(const auto& vector) {
    for(auto item : vector){
        std::cout << item << "\n";
    }
}


