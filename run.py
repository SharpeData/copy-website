#---------------------------------------------------------------------
# Python script to copy a website and make it ready-to-deploy
#---------------------------------------------------------------------
#   Author            : Jayadeep Karnati
#   Last modified     : 15rd Feb 2015
#   Compatibility     : Python3
#   Requirements      : Beautiful Soup
#   Specification     : Parses website with only one css folder
#---------------------------------------------------------------------

import os
from collections import defaultdict
from helpers import make_new_directory, arrange_resources, make_menu_pages
from settings import SRC as src
from settings import DEST as dest
from parse import parse_links

if __name__ == '__main__':
    """
    Creates dest folder, a 'names' dictionary
    and initiates recursive 'parse_links' process
    """
    if os.path.exists(src):
        print("Processing")
        make_new_directory(dest)
        # 'names' stores folder names to avoid conflicts
        names = defaultdict(int)
        menu_links = {}
        make_menu_pages(src, dest, menu_links)
        parse_links(names, src, menu_links,
                    input_path=os.path.join(src, "index.html"),
                    output_path=dest,
                    layer_level=0,
                    recursion_depth=3)
        arrange_resources(src, dest)
        print("Successful\n")
    else:
        print("\nError: Unable to find src location.",
              "\nEnter valid src path in settings.py.")
        quit()
else:
    print("This module is not meant to be imported.")
