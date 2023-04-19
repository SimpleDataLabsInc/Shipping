from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from pricingbysegment.graph.ByOrderkey import *
from pricingbysegment.config.ConfigStore import *


class ByOrderkeyTest(BaseTestCase):

    def test_unit_test_(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pricingbysegment/graph/ByOrderkey/in0/schema.json',
            'test/resources/data/pricingbysegment/graph/ByOrderkey/in0/data/test_unit_test_.json',
            'in0'
        )
        dfIn1 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pricingbysegment/graph/ByOrderkey/in1/schema.json',
            'test/resources/data/pricingbysegment/graph/ByOrderkey/in1/data/test_unit_test_.json',
            'in1'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/pricingbysegment/graph/ByOrderkey/out/schema.json',
            'test/resources/data/pricingbysegment/graph/ByOrderkey/out/data/test_unit_test_.json',
            'out'
        )
        dfOutComputed = ByOrderkey(self.spark, dfIn0, dfIn1)

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
