#!/usr/bin/python
#
# Author: Susmita Mhamane
# Date: July 9, 2024

# Import necessary libraries from PySpark
from pyspark.sql import SparkSession,DataFrame
from pyspark.sql.functions import explode, split, lower, regexp_replace, desc
import pyspark.sql.functions as F
# Initialize Spark session
spark = SparkSession.builder.appName("Spark SQL basic example").enableHiveSupport().getOrCreate()
sc = spark.sparkContext

master = "local"

spark.sparkContext.setLogLevel("WARN")

stop_words = ['i',
'',
 'me',
 'my',
 'myself',
 'we',
 'our',
 'ours',
 'ourselves',
 'you',
 'your',
 'yours',
 'yourself',
 'yourselves',
 'he',
 'him',
 'his',
 'himself',
 'she',
 'her',
 'hers',
 'herself',
 'it',
 'its',
 'itself',
 'they',
 'them',
 'their',
 'theirs',
 'themselves',
 'what',
 'which',
 'who',
 'whom',
 'this',
 'that',
 'these',
 'those',
 'am',
 'is',
 'are',
 'was',
 'were',
 'be',
 'been',
 'being',
 'have',
 'has',
 'had',
 'having',
 'do',
 'does',
 'did',
 'doing',
 'a',
 'an',
 'the',
 'and',
 'but',
 'if',
 'or',
 'because',
 'as',
 'until',
 'while',
 'of',
 'at',
 'by',
 'for',
 'with',
 'about',
 'against',
 'between',
 'into',
 'through',
 'during',
 'before',
 'after',
 'above',
 'below',
 'to',
 'from',
 'up',
 'down',
 'in',
 'out',
 'on',
 'off',
 'over',
 'under',
 'again',
 'further',
 'then',
 'once',
 'here',
 'there',
 'when',
 'where',
 'why',
 'how',
 'all',
 'any',
 'both',
 'each',
 'few',
 'more',
 'most',
 'other',
 'some',
 'such',
 'no',
 'nor',
 'not',
 'only',
 'own',
 'same',
 'so',
 'than',
 'too',
 'very',
 'can',
 'will',
 'just',
 'don',
 'should',
 'now']

# Create a DataFrame from the file path
file_path = "Complete_Shakespeare.txt"
df = spark.read.text(file_path)
df.show(10)
# Split the Row Objects in DataFrame into words and Convert the words in lower case and
df_words = df.select(explode(split("value", "\s+")).alias("Word"))
df_words.show(10)
# remove stop words from stop_words
df_filtered = df_words.filter(~(F.lower(df_words["Word"]).isin(stop_words)))
df_filtered.show(10)
df_word_counts = df_filtered.groupBy("Word").count()
df_word_counts.show(10)
df_top_words = df_word_counts.orderBy(desc("count")).limit(10)
df_top_words.show(10)
df_top_words.withColumnRenamed("count","Frequency").show(9)
#Storing DataFrame in Hive as Table
df_top_words.withColumnRenamed("count","Frequency").write.mode("overwrite").saveAsTable("Wordcount")
