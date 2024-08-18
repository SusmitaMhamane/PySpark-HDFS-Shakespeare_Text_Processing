#!/bin/bash

#
# Author: Susmita Mhamane
# Date: July 9, 2024

source ./unset_jupyter.sh
hdfs dfs -test -e /user/talentum/Complete_Shakespeare.txt
if [ $? -eq 0 ]; then
    echo "File is There"
    hdfs dfs -rm /user/talentum/Complete_Shakespeare.txt
    echo "File Deleted Successfully"
fi
echo "-------------------------------------------------------------------------------------"
echo "Putting file on HDFS"
hdfs dfs -put ~/shared/Complete_Shakespeare.txt /user/talentum/
echo "File copied successfully."
echo "---------------------------Executing PySpark Script----------------------------------"
spark-submit Shakespeare.py
echo "-------------------------------------------------------------------------------------"
echo "Showing tables"
hive -e "show tables;"
echo "-------------------------------------------------------------------------------------"
echo "Displaying Records Stored in Hive Table"
hive -e "select * from wordcount limit 9;"
