import pandas as pd
from handlecsv import delete_column,delete_row,count_column,count_row

class TestHandlecsv:
    """ Class for Unit Test for Handling CSV """
    def setup_method(self):
        data=[['Bill',22,'NC'],['Tony',23,'NC'],['RuoXin',22,'NC'],['YiQing',23,'NC']]
        self.test_frame=pd.DataFrame(data,columns=['Name','Age','State'])


    def test_delete_row(self):
        print("The dataframe before delete row is ")
        print(self.test_frame)
        delete_row(self.test_frame,1)
        print("The dataframe after delete row is ")
        print(self.test_frame)

    def test_delete_column(self):
        print("The dataframe before delete column is ")
        print(self.test_frame)
        delete_column(self.test_frame,'State')
        print("The dataframe after delete column is ")
        print(self.test_frame)

    def test_count_row(self):

        print(f"The number of rows in the original csv file is {count_row(self.test_frame)}")


    def test_count_column(self):

        print(f"The number of columns in the original csv file is {count_column(self.test_frame)}")


