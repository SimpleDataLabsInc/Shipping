from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from .config import *
from retail.udfs.UDFs import *

def DataCleanup_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter(lit(True))
