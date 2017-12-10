#!/usr/bin/python

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

enron_data = pickle.load(open("../tools/final_project_dataset_unix.pkl", "rb"))


#Finding number of people in dataset are present 
print()
print("Number of people dataset is available : " ,len(enron_data))
print()


#Finding number of features for each people is available
print("Number of features available for each in dataset : ",len(enron_data['METTS MARK']))
print()

#Finding features for each people is available
print("Number of features available for each in dataset -> ")
for i in enron_data['METTS MARK']:
	print("   ",i)
print()
print()


#Finding POIs In The Enron Data
no_of_poi = 0
poi_dict = []
for i in enron_data:
	if enron_data[i]["poi"] == 1:
		no_of_poi = no_of_poi + 1
		poi_dict.append(i)

print("POIs in dataset are : ",no_of_poi)
print()

#Printing the names of person of intrest emails avaliable
print("Names of POIs emails avaliable")
for i in poi_dict:
	print(i)
print()
print()


#Reading poi_names.txt
poi_names_txt = open("poi_names.txt","r").read()
poi_names_list = poi_names_txt.split("\n")
poi_names_list = poi_names_list[2:len(poi_names_list) - 1]
print("Number of POIs Exist : ", len(poi_names_list))
print()

#total value of the stock belonging to James Prentice
print("Stock belonging to James Prentice : ", enron_data['PRENTICE JAMES']['total_stock_value'])
print()

#Email messages do we have from Wesley Colwell to POIs
print("Number of emails from Wesley Colwell to POIs : ", enron_data['COLWELL WESLEY']['from_this_person_to_poi'])
print()

#Value of stock options exercised by Jeffrey K Skilling
print("Value of stock options exercised by Jeffrey K Skilling : ", enron_data['SKILLING JEFFREY K']['exercised_stock_options'])
print()

#Folks in this dataset have a quantified salary and known emails
folks_q_salary = 0
folks_k_emails = 0
folks_t_payments = 0
POIs_t_payments = 0
for i in enron_data:
	if enron_data[i]["salary"] != 'NaN':
		folks_q_salary += 1
	if  enron_data[i]['email_address'] != 'NaN':
		folks_k_emails += 1
	if  enron_data[i]['total_payments'] != 'NaN':
		folks_t_payments += 1
	if enron_data[i]['total_payments'] == 'NaN' and enron_data[i]["poi"] == 1:
		POIs_t_payments += 1 
print("Folks in this dataset have a quantified salary : ", folks_q_salary)
print()
print("Folks in this dataset have a known Email : ", folks_k_emails)
print()
print("Percentage of people in the dataset have their total payments : ",100 - (float(folks_t_payments) * 100 / len(enron_data)))
print()
print("POIs in the E+F dataset have “NaN” for their total payments : ",POIs_t_payments)
print()
