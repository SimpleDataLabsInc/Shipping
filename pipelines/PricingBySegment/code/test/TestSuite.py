import unittest

from test.pricingbysegment.graph.test_AdjustCols import *
from test.pricingbysegment.graph.test_ByOrderkey import *

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(unittest.TestSuite())
