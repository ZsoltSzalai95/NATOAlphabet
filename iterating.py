student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas
dataframe=pandas.DataFrame(student_dict)
new_dic = {row.student:row.score for (index, row) in dataframe.iterrows()}
print(new_dic)

#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # print(index)
#     # print(row)
#     # print(row.student)
#     # print(row.score)
#     pass


