# AIPI510_Premodule
This is the repository for AIPI510 premodule assignment

Requirements:
Python 3.11.9
pip 24.2

## venv

in the dectionary of this project:

create venv:
python -m venv handlecsv

activate venv:
in windows: handlecsv/Scripts/activate
in linux: source handlecsv/Scripts/activate

## Installation

pip install -r requirements.txt

## Packaging

python -m setup build
python -m setup install

## Using this csv processor:

handlecsv YOURFILENAME --rowindex YOURROWINDEX --columnname YOURCOLUMNNAME --countrow IFCOUNTROW --countcolumn IFCOUNTCOLUMN   

YOURFILENAME: a csv file needed to be processed    
YOURROWINDEX: a row index you want to delete in this file    
YOURCOLUMNNAME: the name of a column you want to delete in this file    
IFCOUNTROW: after doing the processing, whether to show the number of all rows in modified csv file    
IFCOUNTCOLUMN: after doing the processing, whether to show the number of all columns in modified csv file    

the modified files would be in the ./output/ and would be prefixed with modified

