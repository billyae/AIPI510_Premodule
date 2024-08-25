from setuptools import setup, find_packages

setup(
    name='Handle CSV files',
    description='delete specific row or column in a csv file and count the number of rows or colunms in the file and output the modified csv file',
    packages=find_packages(),
    author='Zihao Yang',
    entry_points="""
    [console_scripts]
    handlecsv=handlecsv.main:main
    """,
    install_requires=['click==7.1.2', 'pandas==1.2.0'],
    version='0.0.1',
    url='https://github.com/billyae/AIPI510_Premodule',
)
