import pandas as pd
import numpy as np

workersDict1 = {"name": ["Ahmet", "Nazlı", "Mehmet", "Necmi", "Gül", "Sevda", "Murat"],
         "departmant": ["IT", "Back End", "AI", "IT", "Back End", "AI", "Dev Ops"],
         "salary":[10000, 7500, 5600, 8200, 6250, 6900, 9000]}

workersDict2 = {"name": ["Mehmet", "Irem", "Kadir", "Furkan", "Buse", "Merve", "Semih"],
         "departmant": ["IT", "Back End", "AI", "Dev Ops", "Back End", "AI", "Dev Ops"],
         "salary":[8000, 6300, 6000, 7500, 6250, 8500, 9000]}

workersDF1 = pd.DataFrame(workersDict1)
workersDF2 = pd.DataFrame(workersDict2)

print("Welcome. Today, we will ask you to choose between concatenating and merging the dataframes.")
print("First, you may want to see the dataFrames. You can see them below:")
print("----------------")
print(f"Workers DataFrame 1: \n {workersDF1}")
print("----------------")
print(f"Workers DataFrame 2: \n {workersDF2}")
print("----------------")

answer = input("Now, choose between merge/concat the dataframes")

if answer == "concat":
    concattedDataFrame = pd.concat([workersDF1, workersDF2], ignore_index=True)
    print("You choosed concatenating these DataFrames. Concatted version: ")
    print(concattedDataFrame)

elif answer == "merge":
    concattedDataFrame = pd.merge(workersDF1, workersDF2, on="name")
    print("You choosed concatenating these DataFrames. Concatted version: ")
    print(concattedDataFrame)