
def delete_row(df,rowindex):
    """ delete a specific row of a dataframe """
    df.drop(index=rowindex,inplace=True)
    return df

def delete_column(df,column):
    """ delete a specific column of a dataframe"""
    df.drop(axis=1,columns=column,inplace=True)
    return df

def count_row(df):
    """ count the number of rows of a dataframe"""
    return df.shape[0]

def count_column(df):
    """ count the number of columns of a dataframe"""
    return df.shape[1]