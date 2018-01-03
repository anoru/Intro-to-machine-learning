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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "How many data points (people) are in the dataset?", len(enron_data)
print "For each person, how many features are available?", len(enron_data[enron_data.keys()[0]])

# Calculate the number of person of interest in our dataset
num_poi = 0
for person in enron_data:
	if (enron_data[person]['poi'] == True):
		num_poi = num_poi + 1

print "How many POIs are there in the E+F dataset?", num_poi

print "What is the total value of the stock belonging to James Prentice?", enron_data['PRENTICE JAMES']['total_stock_value']

print "How many email messages do we have from Wesley Colwell to persons of interest?", enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print "What's the value of stock options exercised by Jeffrey K Skilling?", enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print "Of these three individuals (Lay, Skilling and Fastow), who took home the most money ?", enron_data['LAY KENNETH L']['total_payments'], enron_data['SKILLING JEFFREY K']['total_payments'], enron_data['FASTOW ANDREW S']['total_payments']

num_quant_salary = 0
num_know_address = 0
nul_total_payments = 0
for person in enron_data:
	if (enron_data[person]['salary'] != 'NaN'):
		num_quant_salary = num_quant_salary + 1
	if (enron_data[person]['email_address'] != 'NaN'):
		num_know_address = num_know_address + 1
	if (enron_data[person]['total_payments'] == 'NaN'):
		nul_total_payments = nul_total_payments + 1


print "How many folks in this dataset have a quantified salary?", num_quant_salary
print "What about a known email address?", num_know_address
print "How many people in the E+F dataset (as it currently exists) have 'NaN' for their total payments? ", nul_total_payments, 
print "with a percentage of", float(nul_total_payments*100/len(enron_data))

percent_null_total_payment_poi = 0
for person in enron_data:
	if (enron_data[person]['poi'] == True):
		if (enron_data[person]['total_payments'] == 'NaN'):
			percent_null_total_payment_poi = percent_null_total_payment_poi + 1

print "How many POIs in the E+F dataset have 'NaN' for their total payments?", percent_null_total_payment_poi,
print "What percentage of POI's as a whole is this?", float(percent_null_total_payment_poi*100/len(enron_data))

print "What is the new number of people of the dataset after adding 10 more daat points?", len(enron_data)+10
print "What is the new number of folks with 'NaN' for total payments?", nul_total_payments+10

print "What is the new number of POI's in the dataset?", num_poi+10
print "What is the new number of POI's with NaN for total_payments?", percent_null_total_payment_poi+10

## Get the nmaes of poi from a txt file
#names_file = open("../final_project/poi_names.txt", "r")
#names_poi = []
#for line in names_file:
	#names_poi.append(line.strip())
#names_file.close()
#
#del names_poi[0]
#del names_poi[0]
#
#names_poi = list(map(lambda x:x.strip('(y)'),names_poi))
#names_poi = list(map(lambda x:x.strip('(n)'),names_poi))
#names_poi = list(map(lambda x:x.strip(' '),names_poi))
#names_poi = list(map(lambda x:x.strip('\,'),names_poi))
#
#print names_poi
#print [i for i in names_poi if i in enron_data.keys()]

#print enron_data.keys()

