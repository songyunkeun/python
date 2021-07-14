student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(data)
#data_dic = data.to_dict()
# data_dic  = data.set_index('letter').T.to_dict()
# new_data_dic = {key:value['code'] for (key, value) in data_dic.items()}

data_frame = {index:row for (index, row) in data.iterrows()}
print(data_frame)
#print(new_data_dic)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

