
'''
Created on March 11, 2021

@author: Alexandros.FRANGIADOULIS

'''
#General
import os
import time
import pandas as pd
import numpy as np

#Mongo
import pymongo
from pymongo import MongoClient

class mongo_tool(object):

    def __init__(self,client_link):

        self.client_link = client_link

    def upload_df(self,df,database_name,colection_name):
        '''This is a function of the mongo tool to
        upload a dataframe to selected database straigt in an application'''

        client        = MongoClient(self.client_link)
        database      = client[database_name]
        collection    = database[colection_name]

        collection.insert_many(df.to_dict('records'))

    def drop_collection(self,database_name,collection_name):
        '''This is a function of the class mongo_tool
        to delete a specific collection in a given database,
        from standard given link'''

        client   = MongoClient(self.client_link)
        database = client[database_name]
        mycol = database[collection_name]

        mycol.drop()

        print('*********\n\nCollection:',collection_name,'\nin database:',database_name,'\nDeleted!\n\n*********')

    def show_collections(self,database_name):

        '''This is a function of the class mongo tool,
        In which the aim is to return the list of all collections
        in a given database inside the link of the cluster'''

        client   = MongoClient(self.client_link)
        database = client[database_name]

        col_list = []

        #list the collections
        for coll in database.list_collection_names():
            col_list.append(coll)

        return col_list

    def retrieve_collection_df(self,database_name,collection_name):
        '''This is a function to retrieve a collection from a database as Data-Frame'''

        try:
            client   = MongoClient(self.client_link)
            database = client[database_name]

            collection = database[collection_name]
            data = pd.DataFrame(list(collection.find()))

            data.drop('_id', axis = 1)

            return data
        except:
            print('data do not exist')

    def show_databases(self):
        '''This is a function to return the names of the databases of the client'''
        client = MongoClient(self.client_link)
        databases = list(client.list_database_names())

        databases.remove('admin')
        databases.remove('local')

        return databases



























