import click
import pandas as pd
from .handle_csv import delete_row,delete_column,count_row,count_column

@click.command()
@click.argument('filename',type=click.Path(exists=True))
@click.option('--rowindex',type=int,default=-1,help='This is the index of row to be deleted in the csvfile')
@click.option('--columnname',type=str,default="-1",help='This is the name of column to be deleted in the csvfile')
@click.option('--countrow',type=bool,default=False,help='This is whether you want to count the number of rows in the csvfile after delete')
@click.option('--countcolumn',type=bool,default=False,help='This is whether you want to count the number of columns in the csvfile after delete')
def main(filename,rowindex,columnname,countrow,countcolumn):
    """ Simple programe of doing some basic operations with a specific csv file and modify the csv file based on those operations"""

    df=pd.read_csv(filename)

    if rowindex!=-1:
        df=delete_row(df,rowindex)
        print(f"The row with {rowindex} index has been successfully deleted!")
    
    if columnname!="-1":
        df=delete_column(df,columnname)
        print(f"{columnname} has been successfully deleted!")

    if countrow==True: 
        rowcount=count_row(df)
        print(f"The number of rows in the modified csv file is {rowcount}")

    if countcolumn==True:
        columncount=count_column(df)
        print(f"The number of columns in the modified csv file is {columncount}")

    filename=filename.split("/")[-1]
    with open(f"./output/modified_{filename}","a+") as file:
        df.to_csv(f"./output/modified_{filename}",index=False)

    print(f"we have successfullly modify this csv file. Here is the modified file ./output/modified_{filename}")
