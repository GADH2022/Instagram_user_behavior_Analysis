import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def read_data_from_csv():
    comments=pd.read_csv('Resources/comments.csv')
    return comments


def data_cleaning():
    #DO NOT REMOVE FOLLOWING LINE
    #call remove_unwanted_columns() function to get dataframe
    comments=read_data_from_csv()
    #Remove Unwanted columns
    comments.describe()
    comments.drop(columns=["posted date","emoji used",
                           "Hashtags used count"],axis=1,
                             inplace=True)
                             
    comments.rename(columns={"coment": "comment_text",
                             "User id": "user_id",
                              "Photo id": "photo_id",
                              "created Timestamp": "created_at"},
                              inplace=True)
    #rename columns, only these columns are allowed in the dataset
    # 1.	id
    # 2.	comment_text
    # 3.	user_id
    # 4.	photo_id
    # 5.	created_at
    
    #export cleaned Dataset to newcsv file named "comments_cleaned.csv"
    comments.to_csv('comments_cleaned.csv')
    return comments

