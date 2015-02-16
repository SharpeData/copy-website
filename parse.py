#-----------------------------------------------------------------------
#
# Parsing functions for copy-website script
#
#-----------------------------------------------------------------------
#
#   Author            : Jayadeep Karnati
#   Last modified     : 15rd Feb 2015
#   Compatibility     : Python3
#   Requirements      : Beautiful Soup
#
#-----------------------------------------------------------------------

import os, shutil
from bs4 import BeautifulSoup
from helpers import link_is_appropriate, get_unique_name, make_new_directory, save_html, print_progress


def parse_links(names, target, input_path, output_path, layer_level, recursion_depth):
    """
    Parses links and organizes folders recursively

    - Finds all the suitable links in html file corresponding to input path.
    - Changes the links by giving them unique names.
    - Creates a new directory with that unique name in the output_path.
    - Generates the modified html file in the output_path.
    """

    print_progress(layer_level)

    with open(input_path) as f:
        soup = BeautifulSoup(f.read())
    html_path = os.path.join(output_path, "index.html")
    save_html(soup, html_path)

    parse_css_links(soup, layer_level)

    for link_tag in soup.find_all('a'):
        link = link_tag.get('href')

        if link_is_appropriate(link, layer_level):
            name = link_tag.string.strip(" \t\n\r").partition(' ')[0].lower()
            name = get_unique_name(name, names)
            link_tag['href'] = name
            new_output_path = os.path.join(output_path, name)
            make_new_directory(new_output_path)

            html_path = os.path.join(output_path, "index.html")
            if recursion_depth > 0:

                parse_links(names, target,
                            input_path = os.path.join(target, link),
                            output_path = new_output_path,
                            layer_level = layer_level + 1,
                            recursion_depth = recursion_depth - 1)

    save_html(soup, html_path)


def parse_css_links(soup, layer_level):
    """
    Parses css links in html files.

    Creates new directory for css and redirects the css links
    to this directory.
    """
    for link_tag in soup.find_all('link'):
        link = link_tag.get('href')
        if link is None:
            return
        elif link.endswith("main.css"):
            link_tag['href'] = layer_level * "../" + "css/main.css"
        elif link.endswith("tabs.css"):
            link_tag['href'] = layer_level * "../" + "css/tabs.css"
        elif link.endswith("home_styles.css"):
            link_tag['href'] = layer_level * "../" + "css/home_styles.css"




#-----------------------------------------------------------------------

if __name__ == '__main__':

    print("\nThis is not a standalone script.\nUse 'python3 run.py' to run copy-website.")
else:
    print("Imported parse.py")

#-----------------------------------------------------------------------
