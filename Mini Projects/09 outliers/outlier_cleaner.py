#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    raw_data = []
    ### your code goes here
    #Making a new raw_data tuple
    for i in range(0, len(predictions), 1):
        error = (net_worths[i][0] - predictions[i][0]) ** 2
        raw_data.append((ages[i][0], net_worths[i][0], error))

    #Sorting raw_data
    for i in range(0, len(raw_data), 1):
        for j in range(0, len(raw_data) - 1, 1):   
            if raw_data[j][2] > raw_data[j + 1][2]:
                temp = raw_data[j]
                raw_data[j] = raw_data[j + 1]
                raw_data[j + 1] = temp
    
    cleaned_data = raw_data[:int(len(raw_data) * 0.9)]

    return cleaned_data

