#ifndef MATRIX_FUNCTIONS_H
#define MATRIX_FUNCTIONS_H
#include <vector>

std::vector<double> vector_matrix_product(const std::vector<std::vector<double>>& matrix, const std::vector<double>& vector);
std::vector<std::vector<double>> transposition(const std::vector<std::vector<double>>& matrix);
std::vector<std::vector<double>> matrix_product(const auto& matrix1, const auto& matrix2);

std::vector<double> get_col(const auto& matrix, const int col_number);
void add_to_col(auto& matrix, const auto& vector, int col_num);

void print_vector(const auto& vector);
void print_matrix(const std::vector<std::vector<double>>& matrix);

#endif