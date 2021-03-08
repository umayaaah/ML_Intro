#!/usr/bin/python

from poi_email_addresses import poiEmails
from feature_format import featureFormat

""" 
    Exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
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

    print("Total persons of interest: " + str(poi_count))

def single_queries(enron_data):
    stock_val = enron_data["PRENTICE JAMES"]["total_stock_value"]
    print("Stock value for James Prentice: " + str(stock_val))

    num_emails = enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
    print("Num emails from Wesley Colwell to POI: " + str(num_emails))

    stock_options = enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
    print("Stock options exercised by Jeffrey K Skilling: " + str(stock_options))

def top_payment(enron_data, persons):
    top = 0
    name = ""
    for p in persons:
        t_pay = (enron_data[p]["total_payments"])
        if(t_pay>top):
            top = t_pay
            name = p
        print(p + " - Total payments: " + str(t_pay))

    print("Top payment of $" + str(top) + " to " + name)
    
def all_salaries(enron_data):
    salaries = []
    for person in enron_data:
        s = enron_data[person]["salary"]
        if isinstance(s, int):
            salaries.append(s)
    # print(salaries)
    print("Salary info available for " + str(len(salaries)) + " people in the dataset")

def all_emails(enron_data):
    emails = []
    for person in enron_data:
        e = enron_data[person]["email_address"]
        if e != "NaN":
            emails.append(e)
    print("Email info available for " + str(len(emails)) + " people in the dataset")

def name_exists(enron_data, name):
    name = name.upper()
    if name in enron_data.keys():
        print(name + " exists in dataset")
    else:
        print(name + " does not exist in dataset")

def main():
    enron_data = pickle.load(open("../../ud120-projects/final_project/final_project_dataset.pkl", "rb"))
    # print(enron_data)
    print("---- dataset information ----")
    data_info(enron_data)
    print("\n---- dataset queries ----")
    persons_of_interest(enron_data)
    name_exists(enron_data, "KRAUTZ MICHAEL")
    single_queries(enron_data)
    top_payment(enron_data, ["SKILLING JEFFREY K", "FASTOW ANDREW S", "LAY KENNETH L"])
    all_salaries(enron_data)
    all_emails(enron_data)

if __name__ == "__main__":
    main()