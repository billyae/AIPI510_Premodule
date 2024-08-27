This is the repository for AIPI510 premodule assignment  

Requirements:  
Python 3.11.9  
pip 24.2  

## fetch the project

git clone https://github.com/billyae/AIPI510_Premodule.git     
cd AIPI510_Premodule

## venv

create venv:  
python -m venv handlecsvtest  

activate venv:    
in windows: handlecsvtest/Scripts/activate    
in linux: source handlecsvtest/Scripts/activate

## Installation

pip install -r requirements.txt  

## Packaging

pip install .
  
## Using this csv processor:  

handlecsv YOURFILENAME --rowindex YOURROWINDEX --columnname YOURCOLUMNNAME --countrow IFCOUNTROW --countcolumn IFCOUNTCOLUMN    

YOURFILENAME(required): a csv file needed to be processed     
YOURROWINDEX(optional): a row index you want to delete in this file     
YOURCOLUMNNAME(optional): the name of a column you want to delete in this file    
IFCOUNTROW(optional): after doing the processing, whether to show the number of all rows in modified csv file    
IFCOUNTCOLUMN(optinal): after doing the processing, whether to show the number of all columns in modified csv file    

the modified files would be in the ./output/ and would be prefixed with modified    

