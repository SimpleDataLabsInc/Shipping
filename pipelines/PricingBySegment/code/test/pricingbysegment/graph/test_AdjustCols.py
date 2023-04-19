from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from pricingbysegment.graph.AdjustCols import *
from pricingbysegment.config.ConfigStore import *


class AdjustColsTest(BaseTestCase):

    def test_unit_test_(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pricingbysegment/graph/AdjustCols/in0/schema.json',
            'test/resources/data/pricingbysegment/graph/AdjustCols/in0/data/test_unit_test_.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pricingbysegment/graph/AdjustCols/out/schema.json',
            'test/resources/data/pricingbysegment/graph/AdjustCols/out/data/test_unit_test_.json',
            'out'
        )
        dfOutComputed = AdjustCols(self.spark, dfIn0)
        assertDFEquals(
            dfOut.select(
              "MKTSEGMENT",
              "QUANTITY",
              "EXTENDEDPRICE",
              "DISCOUNT",
              "TAX",
              "RETURNFLAG",
              "DELIVERYSTATUS",
              "CLEARANCE",
              "ORDERKEY"
            ),
            dfOutComputed.select(
              "MKTSEGMENT",
              "QUANTITY",
              "EXTENDEDPRICE",
              "DISCOUNT",
              "TAX",
              "RETURNFLAG",
              "DELIVERYSTATUS",
              "CLEARANCE",
              "ORDERKEY"
            ),
            self.maxUnequalRowsToShow
        )

    def setUp(self):
        BaseTestCase.setUp(self)
        import os
        fabricName = os.environ['FABRIC_NAME']
        Utils.initializeFromArgs(
            self.spark,
            Namespace(
              file = f"configs/resources/config/{fabricName}.json",
              config = None,
              overrideJson = None,
              defaultConfFile = None
            )
        )
