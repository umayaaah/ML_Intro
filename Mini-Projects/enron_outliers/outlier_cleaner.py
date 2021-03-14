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

    for i in range(len(predictions)):
        err = abs(predictions[i] - net_worths[i])
        # print(err)
        entry = (ages[i], net_worths[i], err)
        # print(entry)
        cleaned_data.append(entry)

    cleaned_data = sorted(cleaned_data, key=lambda x: x[2], reverse=True)
    to_remove = int(0.1*len(cleaned_data))
    removed = cleaned_data[:to_remove]
    cleaned_data = cleaned_data[to_remove:]
    
    print("Removed 10 percent of data set ({0} data points). Data points removed: {1}\n".format(to_remove, removed))
    # print(cleaned_data)
    
    return cleaned_data

