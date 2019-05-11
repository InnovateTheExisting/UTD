Step 1: Open cmd and navigate to the program folder
Step 2:For each data set there is a diffrent folder which holds the preprocessing code.Before running neural net you should run the respective dataset preprocessing code to obtain test and train data sets.

Preprocess Code:

Adult Dataset:python PreProcessAdult\preadult.py https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data 0.2
Car Dataset:python PreProcessCar\precar.py https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data 0.2
Iris Dataset:python PreProcessIris\preiris.py https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data 0.2

Step3: Next step is to run the neural net code with diffrent parameters as the following example.

Example: python NeuralNet.py learningrate iterations hiddenlayer1 hiddenlayer2
         python NeuralNet.py sigmoid 0.1 1000 4 2
		 python NeuralNet.py tanh 0.1 1000 4 2
		 python NeuralNet.py relu 0.1 1000 4 2

Output:
In Output Folder the sample output file and output screenshots contains all three data sets run using all activation functions.
If u run the program the immediate output will get appended to output.txt in the main folder(Neural Net Folder).
