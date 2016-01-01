"""config.py: 

    Configuration file.

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2015, Dilawar Singh and NCBS Bangalore"
__credits__          = ["NCBS Bangalore"]
__license__          = "GNU GPL"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import logging

class Args: pass
args_ = Args()

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
    filename='__log__.log',
    filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
_logger = logging.getLogger('')
_logger.addHandler(console)


# Threshold value for canny edge detector.
elow, ehigh = 150, 200 

# Min number of points in contours. Must be more than 5.
min_points_in_contours = 4

# Time averaging over frames. Increase this number for motion correction. Larger
# values will give cleaner ROIs but also reduce their numbers.
n_frames = 30

# Maximum area of neuron in um^2. This is used to reject contours. Upper limit
# is 20 um diameter (312 um^2). For toime being, I am using 200 um as upper
# limit on neuron area.
max_neuron_area = 200 #314
