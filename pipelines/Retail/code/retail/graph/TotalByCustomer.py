from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from retail.config.ConfigStore import *
from retail.udfs.UDFs import *

def TotalByCustomer(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("customer_id"))

    return df1.agg(
        first(col("first_name")).alias("first_name"), 
        first(col("last_name")).alias("last_name"), 
        sum(col("amount")).alias("amounts")
    )
