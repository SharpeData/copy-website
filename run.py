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
#   Specification     : Parses website with only one css folder
#   
#
#-----------------------------------------------------------------------

import os
from collections import defaultdict

from  settings import src, dest
from helpers import make_new_directory, arrange_resources, make_menu_pages
from parse import parse_links


if __name__ == '__main__':
    """
    Creates dest folder, a 'names' dictionary
    and initiates recursive 'parse_links' process
    """

    if os.path.exists(src):
        print("Processing")
        make_new_directory(dest)

        # 'names' dictionary stores names of each folder to avoid conflicts
        names = defaultdict(int)

        menu_links = {}
        make_menu_pages(src, dest, menu_links)

        parse_links(names, src, menu_links,
                    input_path = os.path.join(src, "index.html"),
                    output_path = dest,
                    layer_level = 0,
                    recursion_depth = 3)


        arrange_resources(src, dest)
        print("Successful\n")

    else:
        print("\nError: Unable to find src location.\nEnter valid src path in settings.py.")
        quit()
else:
    """
    This script is not to be imported in another script.
    """
    print("This module is not meant to be imported.")


#-----------------------------------------------------------------------