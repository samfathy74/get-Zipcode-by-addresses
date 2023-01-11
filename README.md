# ZipCode USA Python Script

This Python script allows you to add zip codes to an excel file for addresses data with address, city, and state in the USA. It uses the `uszipcode` library and `pandas` library to perform this task.

  

## Getting Started

To use this script, you'll need to install the `uszipcode` library and `pandas` library. You can do this by running the following command in your command line:

<pre> <code> pip install uszipcode pandas</code></pre>

  

## Usage

This script reads an excel file with data containing address, city, and state columns , then it uses `uszipcode` library to get the zip codes by matching the city and state columns, and finally it saves the excel file with the new column zip_code beside the other columns.

  

The script can be run using the command :

<pre><code> python script_name.py</code> </pre>

It is important to mention that :
- The excel file should be in the same directory of the script.
- The excel file name should be contacts.xlsx
- The output excel file name after running the script will be contacts_with_zip.xlsx

  

## Example
 Before running the script:

|Address| City | State |
|--|--|--|
|1600 Pennsylvania Ave | Washington | DC |
|4301 1st Ave SE | Cedar Rapids | IA|

After running the script:
|Address| City | State | zip_code |
|--|--|--|--|
|1600 Pennsylvania Ave | Washington | DC | 20500 |
|4301 1st Ave SE | Cedar Rapids | IA|52401|
 

 ***You can customize the script by changing the input and output excel files name, or changing the columns name and number to fit your data*** 

  

## Authors

This script is developed by me, You can use it, modify it and make it fit your needs.

  

## Acknowledgments

A big thanks to the authors and contributors of the `uszipcode` and `pandas` libraries for making it possible to easily get zip codes by address, city, or state in Python.
