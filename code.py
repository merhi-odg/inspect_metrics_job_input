import logging
import pandas


logger = logging.getLogger(__name__)
logging.basicConfig(level="INFO")


# modelop.metrics
def metrics(data):
    
    logger.info("input shape: %s", data.shape)
    
    yield {"foo": "bar"}
