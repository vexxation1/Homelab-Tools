# **Homelab-Tools**
 *Misc tools for various homelab server devices*


## **1. DeviceDB**
 Database tool for mapping my devices to a local IP addresses schema.\
 Not much use for others, but a good framework to carry to other projects.\
 This is done as a very basic CSV Flat File schema, meaning this is not intended to scale beyond a handfull of devices.

 ## Documentation
  ### ***Database***: Class containing methods for creating and modifying a database CSV file
  Database.***update***(): Static method that takes no arguments, returns pandas DataFrame. Detects if a database file exists and acts accordingly. If no file is found, a file is generated with a 0'th record.
  
  Database.***create***(): Static method, adds a record to the database, takes 2 Arguments:
   1. **frame**: pandas DataFrame, this is the DataFrame returned by Database.update()
   2. **record**: tuple containing 2 strings, supplies the desired Device Name and IP address to be added as a record to the database

  Databse.***delete***():  Static method, removes a record from the database, takes 2 Arguments:
   1. **frame**: pandas DataFrame, the DataFrame representing the database you're removing the record from.
   2. **index**: string, the index of the record to be removed. Specifically, the value of the UID field in this implementation.


  
