#include <iostream>
#include <vector>
#include <random>
#include <numbers>
#include <typeinfo>
#include "matrix_functions.h"
#include "get_data.h"


class Dense_Layer {
    private:
        std::vector<std::vector<double>> weights{}; // where each row is the weights for a single neuron
        std::vector<double> bias{}; // where each value is a bias for a neuron
        std::vector<std::vector<double>> output{};

    public:
        Dense_Layer(int n_input_neurons=0, int n_layer_neurons=0)
        : weights{generate_random_weights(n_input_neurons, n_layer_neurons)}, bias(n_layer_neurons, 0.0) {
           
    

        }
        
         

        double generate_number() {
            // will generate a number between -1 and 1;

            std::mt19937 mt{std::random_device{}()}; //  random device as the seed
            std::uniform_real_distribution<double> gaussian_dist{-1.0, 1.0};
            return gaussian_dist(mt);
        }

        std::vector<std::vector<double>> generate_random_weights(int rows, int cols) {
            // first create an empty matrix
            std::vector<std::vector<double>> w(rows, std::vector<double>(cols, 0.0));

            // then need to iterate over the whole thing
            for(int i{0}; i < rows; i++) {
                for(int j{0}; j < cols; j++) {
                    w[i][j] = generate_number();
                }
            }

           

            return w;
        }

        void forward(std::vector<std::vector<double>>& inputs) {
           

            std::vector<std::vector<double>> tmp{matrix_product(inputs, weights)};

        
            output = vector_matrix_addition(tmp, bias);

        }
        void print() {
            print_matrix(output);

        }

        std::vector<std::vector<double>> get_output() {
            return output;
        }
    };

class Relu{
    private:
        std::vector<std::vector<double>> output{};

        std::vector<double> relu_vector(const std::vector<double>& inputs) {
        
        // runs the relu function on a vector
        std::vector<double> outputs{};
        for(double input: inputs) {
            if(input > 0){
                outputs.push_back(input);
            } else {
                outputs.push_back(0);
            }

        }
        return outputs;

        
    }
    
    public:
        void forward(const std::vector<std::vector<double>>& matrix) {

            // given a matrix of inputs, apply the relu function and set it to the output

            std::vector<std::vector<double>> out{};
            for(auto row: matrix) {
                auto relu_row{relu_vector(row)};
                out.push_back(relu_row);
            }

            output = out;
        }

        auto get_output() {
            return output;
        }

        void print() {
            if(output.size() != 0) {
                print_matrix(output);
            }
           
        }
        

};

class Softmax{
    private:
        std::vector<std::vector<double>> output{};

        std::vector<double> softmax(const std::vector<double>& inputs) {


            // applies the softmax function on a set of inputs
            std::vector<double> exp{};

            for (auto in: inputs) {
                exp.push_back(std::pow(std::numbers::e, in));
            }


            // then we want to normalize our results
            double sum{0};
            for(auto e: exp) {
                sum += e;
            }


            // then divide each value
            std::vector<double> norm_values{};
            for(auto e: exp) {
                norm_values.push_back(e / sum);
            }

            return norm_values;

        }
    
        public:
            void forward(const std::vector<std::vector<double>>& matrix) {

                std::vector<std::vector<double>> out{};

                for(auto row: matrix) {
                    auto softmax_row{softmax(row)};
                    out.push_back(softmax_row);
                }

                output = out;

            }

            void print() {
                print_matrix(output);
            }


};


class Loss {
    private:

        void clip(std::vector<std::vector<double>>& samples){
            // given a reference of the data, changes it inplace using a reference
            double min{std::pow(10, -7)};
            for(auto row: samples){
                for(auto val: row) {
                    if(val <= 0) {
                        val = min;
                    } else if(val > 1) {
                        val = 1 - min;
                    }
                }
            }

        }

        std::vector<double> get_confidences(const std::vector<std::vector<double>>& output, const std::vector<int>& target) {

            // iterate over each row, use the target index as index into the row, add to a vector
            std::vector<double> confidences{};

            int target_index{0};
            for(auto row: output) {
                confidences.push_back(row[target[target_index]]);
                target_index++;
            }

            return confidences;
        }




    public:

        std::vector<double> forward(std::vector<std::vector<double>>& output, const std::vector<int>& target)  {
            // first need to clip the data - prevents any division by 0 errors
            clip(output);

            // we will be way of tracking the target

            /*

            Our data: the confidence of our data
            [0.5, 0.2, 0.3] output 1
            [0,9, 0,05, 0,05] output 2
            [0.8, 0.15, 0.05] output 3

            0 = cat
            1 = dog
            2 = bear

            targets
            [0, 1, 1] i.e for the first its cat, for the second its a dog, for the third its also a dog (the correct answers)

            we want to extract the confidence of the correct target, we can use the indexs of the target

            for cat in the first data set we have 50% confidence
            for dog we have 90% confidence in the second set
            and in the theid we only have 15% confidence that it is a dog - our model didn't work so well

            
            */

            auto confidences{get_confidences(output, target)}; // returns the corresponding confidence to the target

            // getting the log of each value
            for(auto& value: confidences) { // note for self, need the reference when iterating over a vector to update
                value = -(std::log(value));
               
            }

            return confidences;
    }

    double loss(std::vector<std::vector<double>>& output, const std::vector<int>& target) {
        auto predictions{forward(output, target)};


        // calculate the loss on our predictions, just find the mean
        int size{static_cast<int>(predictions.size())};

        double sum{0};
        for(auto num: predictions) {
            sum += num;
        }

        return sum / size;




    }

   
        
};




int main() {
    
    // making a single neuron
    std::vector<std::vector<double>> inputs{
        {1.0, 2.0, 3.0, 2.5},
        {2.0, 5.0, -1.0, 2.0},
        {-1.5, 2.7, 3.3, -0.8}
    };


    // auto data{get_data("class1.csv")}; // getting the data from the file

    // // lets create a portion of the data set
    // std::vector<std::vector<double>> sample(data.begin(), data.begin() + 5);

    // Dense_Layer dl{2, 3}; // initialize the dense layer

    // Relu relu{}; // create an instance of the relu activation function
    // Softmax sm{};

    // dl.forward(sample);

    // std::cout << "The forwarded data looks like this: " << "\n";
    // dl.print(); // print the output of the forward data

    // relu.forward(dl.get_output()); // pass the output of the forwarding into the relu activation function

    // std::cout << "\n" << "The data after passing through the relu activation function looks like this: " << "\n";
    // relu.print(); // some of the data has been clipped to 0

    // sm.forward(dl.get_output());

    // std::cout << "\n" << "The data after passing through the softmax activation function" << "\n";
    // sm.print(); // passing the data through the softmax activation function


    // print_vector(prediction());

    Loss loss{};    

    std::vector<std::vector<double>> softmax_output{
        {0.7, 0.1, 0.2},
        {0.1, 0.5, 0.4},
        {0.02, 0.9, 0.08},
    };

    std::vector<int> targets{0, 1, 1};
    auto l {loss.loss(softmax_output, targets)};
    std::cout << "Calculated loss: " << l << "\n";




    

    return 0;
}