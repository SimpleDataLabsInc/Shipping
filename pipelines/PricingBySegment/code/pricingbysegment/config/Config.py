from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, market_segment: str=None, wholesale_discount: float=None, threshold: int=None, **kwargs):
        self.spark = None
        self.update(market_segment, wholesale_discount, threshold)

    def update(self, market_segment: str="MACHINERY", wholesale_discount: float=0.1, threshold: int=1000, **kwargs):
        prophecy_spark = self.spark
        self.market_segment = market_segment
        self.wholesale_discount = self.get_float_value(wholesale_discount)
        self.threshold = self.get_int_value(threshold)
        pass
