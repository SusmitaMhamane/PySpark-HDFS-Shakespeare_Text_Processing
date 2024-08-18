Shakespeare Text Processing with PySpark and Hive

-- Author: Susmita Mhamane
-- Date: July 9, 2024

This project demonstrates how to process and analyze the Complete Works of William Shakespeare using PySpark and store the results in Hive. The goal is to count word frequencies while excluding common stop words.

------------------------------------------------------------------------------------------------------------------

Project Structure:

unset-jupyter.sh: A shell script to unset environment variables related to Jupyter notebooks.
Shakespeare.py: A PySpark script to process the text file, count word frequencies, and store the results in Hive.
Shakespeare.sh: A shell script to manage the file on HDFS, execute the PySpark script, and display Hive tables.
Complete_Shakespeare.txt: The text file containing the complete works of William Shakespeare.
Prerequisites
Before running the scripts, ensure you have the following installed and configured:

Apache Spark: Ensure Spark is properly installed and configured.
Hive: Ensure Hive is installed and properly integrated with Spark.
HDFS: Make sure Hadoop Distributed File System (HDFS) is set up.
Python 3: PySpark requires Python 3.x.
Setup Instructions
Prepare Environment

Make sure to configure Spark and Hive in your environment. Verify that Hive is accessible from Spark.

------------------------------------------------------------------------------------------------------------------

Prepare the Text File:

Place Complete_Shakespeare.txt in the ~/shared/ directory or update the path in Shakespeare.sh accordingly.

Set Execute Permissions:

Ensure the scripts have execute permissions by running: chmod +x unset-jupyter.sh Shakespeare.py Shakespeare.sh.

Running the Scripts:

Unset Jupyter Environment Variables

Run the unset-jupyter.sh script to unset any Jupyter-related environment variables: ./unset-jupyter.sh.

Run the Main Script

Execute Shakespeare.sh to manage files on HDFS, run the PySpark script, and display Hive tables: ./Shakespeare.sh.

Script Details
unset-jupyter.sh
Unsets environment variables related to Jupyter notebooks to avoid conflicts.

Shakespeare.py
Functionality: Reads the text file, splits text into words, filters out stop words, counts word frequencies, and stores the results in a Hive table.
Key Steps:
Reads text from Complete_Shakespeare.txt.
Splits text into words and filters out stop words.
Counts word frequencies and stores results in Hive.
Shakespeare.sh
Functionality: Manages the file on HDFS, runs the PySpark script, and queries Hive tables.
Key Steps:
Checks if Complete_Shakespeare.txt exists on HDFS and removes it if present.
Uploads Complete_Shakespeare.txt to HDFS.
Executes Shakespeare.py using spark-submit.
Displays Hive tables and queries the wordcount table.
Results
After running Shakespeare.sh, the top 10 most frequent words in the text will be displayed, and the results will be stored in a Hive table named wordcount. You can query this table using Hive commands.

------------------------------------------------------------------------------------------------------------------

Troubleshooting:

File Not Found: Ensure Complete_Shakespeare.txt is in the correct directory and the path is correctly specified.
Permission Issues: Check permissions for the scripts and HDFS directories.
Hive Integration: Verify that Hive is correctly configured and accessible from Spark.