#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include "matrix_functions.h"

int main() {
    // reading from files

    std::string filename{"class1.csv"};

    std::fstream file;
    file.open(filename, std::ios::in); // opening in read mode

    if(file.is_open()) {
        // read from the file
        std::string current_line{};

        std::vector<std::vector<double>> matrix{}; // initialize an empty vector


        
        // want to turn this into jus a big vector
        while(getline(file, current_line)) {
            // need to split the line
            std::stringstream ss(current_line);
            std::string num{};

            std::vector<double> row{};
            while(std::getline(ss, num, ',')) {
                row.push_back(std::stod(num));


            }
            matrix.push_back(row);


        }

        file.close();
        print_matrix(matrix);
        std::cout << matrix[0][0];

    }



    return 0;
    
}