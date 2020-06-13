import torch
import numpy as np
from collections import namedtuple


# returned by _Network.encode
# z is the bottleneck before quantization
EncoderOutput = namedtuple('EncoderOutput', ['qbar', 'qhard', 'symbols', 'z', 'heatmap'])

# returned by _Network._quantize
_QuantizerOutput = namedtuple('_QuantizerOutput', ['qbar', 'qsoft', 'qhard', 'symbols'])

class _Network:
    def __init__(self, config, quantize = True):
        self.config = config
        self.quantize = quantize

        #self.num_chan_bn_including_heatmap = config.num_chan_bn + 1
        #self._centers = None  # Set in encode(); Access with get_centers_variable
    
