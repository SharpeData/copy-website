#-----------------------------------------------------------------------
#
# Python script to copy a website and make it ready-to-deploy
#
#-----------------------------------------------------------------------
#
#   Author            : Jayadeep Karnati
#   Last modified     : 15rd Feb 2015
#   Compatibility     : Python3
#   Requirements      : Beautiful Soup
#
#-----------------------------------------------------------------------

import os
from collections import defaultdict

from  settings import target, destination
from helpers import make_new_directory, arrange_css
from parse import parse_links


if __name__ == '__main__':
    """
    Creates destination folder, a 'names' dictionary
    and initiates recursive 'parse_links' process
    """

    if os.path.exists(target):
        print("Processing")
        make_new_directory(destination)

        # 'names' dictionary stores names of each folder to avoid conflicts
        names = defaultdict(int)

        parse_links(names, target,
                    input_path = os.path.join(target, "index.html"),
                    output_path = destination,
                    layer_level = 0,
                    recursion_depth = 3)

        arrange_css(target, destination)
        print("Successful\n")

    else:
        print("\nError: Unable to find target location.\nEnter valid target path in settings.py.")
        quit()
else:
    """
    This script is not to be imported in another script.
    """
    print("This module is not meant to be imported.")


#-----------------------------------------------------------------------