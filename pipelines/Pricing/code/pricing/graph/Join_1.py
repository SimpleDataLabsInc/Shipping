from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pricing.config.ConfigStore import *
from pricing.udfs.UDFs import *

def Join_1(spark: SparkSession, in0: DataFrame, in1: DataFrame, in2: DataFrame) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.L_ORDERKEY") == col("in1.O_ORDERKEY")), "inner")\
        .join(in2.alias("in2"), (col("in2.C_CUSTKEY") == col("in1.O_CUSTKEY")), "inner")
