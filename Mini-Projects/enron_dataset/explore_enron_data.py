#!/usr/bin/python

from poi_email_addresses import poiEmails

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

def data_info(enron_data):
    num_people = len(enron_data)
    print("Size of Enron dataset: " + str(num_people))
    num_features = [len(v) for v in enron_data.itervalues()]
    num_features = list(dict.fromkeys(num_features))
    print("Total features in Enron dataset: " + str(num_features))
    features_list = [v for v in enron_data.itervalues()][0].keys()
    print("Features:")
    for f in features_list:
        print("\t"+f)

    poi_list = poiEmails()
    # print(len(poi_list))

def persons_of_interest(enron_data):
    poi_count = 0
    for person in enron_data:
        # print("Name: " + person)
        poi_flag = enron_data[person]["poi"]
        # print("POI: " + str(poi_flag))
        if poi_flag:
            poi_count += 1

    print("Total POI: " + str(poi_count))


def single_queries(enron_data):
    stock_val = enron_data["PRENTICE JAMES"]["total_stock_value"]
    print("Stock value for James Prentice: " + str(stock_val))

    num_emails = enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
    print("Num emails from Wesley Colwell to POI: " + str(num_emails))

    stock_options = enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
    print("Stock options exercised by Jeffrey K Skilling: " + str(stock_options))


def main():
    enron_data = pickle.load(open("../../ud120-projects/final_project/final_project_dataset.pkl", "rb"))
    # print(enron_data)
    print("---- dataset information ----")
    data_info(enron_data)
    print("\n---- dataset queries ----")
    persons_of_interest(enron_data)
    single_queries(enron_data)

if __name__ == "__main__":
    main()