import pandas as pd

data_frame = pd.read_excel("homework.xlsx")

print("Rows where the score is missing, i.e. is NaN:")
rows_where_the_score_is_missing = data_frame[(data_frame['score'].isna())]
print(rows_where_the_score_is_missing)

print("\n Rows the score is between a and b, where a and b are values input from console:")
min = int(input("Please enter the minimal score: "))
max = int(input("Please enter the maximal score: "))
rows_the_score_is_between_values = data_frame[(data_frame['score'] >= min) & (data_frame['score'] <= max)]
print(rows_the_score_is_between_values)

print("\n Rows sorted by score")
sorted_data_frame = data_frame.sort_values("score")
print(sorted_data_frame)

print("\n Rows sorted by name")
sorted_data_frame = data_frame.sort_values("name")
print(sorted_data_frame)

print("\n Add new element (result) to the dataframe (values input from console):")
new_element = {
               "name" : input("Enter name:"),
               "score" : input("Enter score:"),
               "attempts" : input("Enter attempts:"),
               "qualify" : input("Enter qualify:")}
dict_data_frame = pd.DataFrame.from_dict([new_element], orient='columns')
data_frame_with_new_element = pd.concat([data_frame, dict_data_frame], ignore_index = True)
print(data_frame_with_new_element)

print("\n Remove results from the dataframe (by index):")
print(data_frame)
index_to_remove = int(input("What row should be removed?:"))
new_dataframe = data_frame.drop(index_to_remove)
print(new_dataframe)

print("\n Save a list of all students that qualified, in a separate Excel file called qualified_students.xlsx. Only columns name and score should be visible there:")

qualified_students_dataframe = data_frame[(data_frame['qualify'] == "yes")]
print(qualified_students_dataframe)
qualified_students_dataframe = qualified_students_dataframe[["name", "score"]]
qualified_students_dataframe.to_excel("qualified_students.xlsx")