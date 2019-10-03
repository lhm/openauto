from pyspark.sql import SparkSession
from pyspark.sql.functions import concat_ws, md5, sum

spark = SparkSession.builder.getOrCreate()

file_location = '/app/sample.csv'
df = spark.read.format("csv").option("inferSchema", True).option("header", True).load(file_location)

# all columns except 'ID' and 'r'; we'll use those to merge rows
compcols = df.columns[1:-1]

# add digest for identical columns
res = df.withColumn("digest", md5(concat_ws(',', *compcols)))

# count identical rows
summarized = res.groupby('digest').agg(sum('r').alias('count'))

# create new dataframe including digest and counts, without 'ID' and 'r'
result = summarized.join(res, 'digest').select('digest', *compcols, 'count').drop_duplicates()

# write result to disk
result.write.mode('overwrite').option('header', 'true').csv('/app/sample-summarized.parts')

# then merge with: csvstack sample-summarized.parts/*.csv > sample-summarized.csv
