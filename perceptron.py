import sys, types, time, random, os
import pandas as pd

def weightInitializer(numberOfFields):
    weights = []
    from random import random
    from random import seed
    seed(1)
    for i in range(0, numberOfFields):
        weights.append(random())
    return weights
    pass

def weightUpdate(input, weights, index, error):
    learningRate = 0.01
    newWeights = []
    
    for i in range (len(input.columns) - 1):
        weights[i]=weights[i] + learningRate*error*input.iloc[index, i]
    
    return weights
    pass

def perceptron(input):
    outputFile = open("epoch.txt", "a+")
    weights = weightInitializer(len(input.columns) - 1)
    thresholdValue = 0.2
    weightedSum = 0
    errorFlag = True

    while(errorFlag):
        errorFlag = False

        for index, record in input.iterrows():
            inputs = []
            for i in range(len(input.columns) - 1):
                weightedSum = weightedSum + input.iloc[index, i]*weights[i]
                inputs.append(input.iloc[index, i])

            if(weightedSum - thresholdValue > 0):
                prediction = 1
            else:
                prediction = 0
            
            weightedSum = 0
            actual= input.iloc[index, -1]

            error = actual - prediction

            print(inputs, weights, actual, prediction, error)
            if(error != 0):
                errorFlag = True
                weights = weightUpdate(input, weights, index, error)
                thresholdValue = thresholdValue + 0.01*error
            
            #print(weights,thresholdValue)

    
            outputFile.write(' '.join(map(str, weights)))

        outputFile.write(" ")
        outputFile.write("----------------------------------------------------------")
        outputFile.write(" ")

    outputFile.close()        
    pass

def perceptronStart(filname):
    data = pd.read_csv(filname)
    perceptron(data)
    pass

if __name__ == '__main__':
    arguments = sys.argv
    filename = arguments[1]
    perceptronStart(filename)
    pass
