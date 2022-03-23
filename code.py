import logging
import pandas


# modelop.metrics
def metrics(data):
    
    logging.info("input shape: %s", data.shape)
    
    yield {"foo": "bar"}
