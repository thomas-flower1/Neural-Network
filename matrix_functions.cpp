#include <iostream>
#include <vector>
#include <tuple>
#include "matrix_functions.h"




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


std::vector<std::vector<double>> matrix_product(const auto& matrix1, const auto& matrix2) {
    // first need to get the size of final matrix using he 
    int matrix_1_height{static_cast<int>(matrix1.size())}; 
    int matrix_1_width{static_cast<int>(matrix1[0].size())};

    int matrix_2_height{static_cast<int>(matrix2.size())};
    int matrix_2_width{static_cast<int>(matrix2[0].size())};

    // need to make an empty matrix
    if(matrix_1_width != matrix_2_height){
        throw std::invalid_argument("Matrix dimensions do not match for multiplication");

    }

    // need to make an empty matrix
    std::vector<std::vector<double>> product(matrix_1_height, std::vector<double>(matrix_2_width, 0));

    // just call the matrix vector product multiple times now

    int length{static_cast<int>(matrix2[0].size())};

    // for each col in matrix2, call the dot product between matrix1 and the row;
    for (int i = 0; i  < length; i++) {

        auto col{get_col(matrix2, i)};
        auto vector_column{vector_matrix_product(matrix1, col)};
        add_to_col(product, vector_column, i);



    }

    return product;
    
}



// uses move semantics
std::vector<double> get_col(const auto& matrix, const int col_number) {
    std::vector<double> col{}; // 

    for(auto row : matrix) {
        col.push_back(row[col_number]);
    }

    return col;
}

void add_to_col(auto& matrix, const auto& vector, int col_num) {

    // takes a reference of a matrix and inserts the a row into specified col, does it in places
    int height{static_cast<int>(matrix.size())};
    for (int row = 0; row < height; row++) {
        matrix[row][col_num] = vector[row];
    }

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


