#include <iostream>
#include <vector>
#include <tuple>


double dotProduct(const std::vector<double>& inputs, const std::vector<double>& weights);
std::vector<double> getLayerOutput(const std::vector<double>& inputs, const std::vector<std::vector<double>>& weights, const std::vector<double>& bias);


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




    return 0;
}

double dotProduct(const std::vector<double>& inputs, const std::vector<double>&weights) {


    // note this is just computing the dot product then adding a bias on top
    int counter{0};
    double sum{};
    for(auto input : inputs) {
        sum += input * weights[counter];
        counter++;

    }

    return sum;
}

// uses move semantics so can return
std::vector<double> getLayerOutput(const std::vector<double>& inputs, const std::vector<std::vector<double>>& weights, const std::vector<double>& bias){

    int number_of_neurons{static_cast<int>(bias.size())};
    std::vector<double> output{};

    for (int i = 0; i < number_of_neurons; i++) {
        double neuron_output{dotProduct(inputs, weights[i])};
        neuron_output += bias[i];


        output.push_back(neuron_output);


    }

    return output;
}
