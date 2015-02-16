#-----------------------------------------------------------------------
#
# Helper functions for copy-website script
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
from settings import folder_permissions


def link_is_appropriate(link, layer_level):
    """
    Chooses appropriate links

    This is a custom function which specifies which 
    links we consider in each layer. It can be 
    modified to suit the website.
    """
    correspondence = {0:0, 1:1, 2:3, 3:-1}   # layer_level vs ampersand count
    if link is None:
        pass
    elif link.startswith("index.html@sub"):
        if correspondence[layer_level] is link.count('&'):
            return True
    return False


def get_unique_name(name, names):
    """
    Checks whether a name exists in the dictionary of names.
    Appends an integer to the name if it exists already.
    """
    if name not in names:
        names[name] = 1
        return name
    else:
        names[name] = names[name] + 1
        name = name + str(names[name])          # appends integer to name
        return get_unique_name(name, names)



def make_new_directory(path):
    """
    Creates a new directory
    """
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    os.chmod(path, folder_permissions)


def save_html(soup, path):
    """
    Writes to html file from soup
    """
    html = soup.prettify("utf-8")
    with open(path, "wb") as f:
        f.write(html)


def print_progress(layer_level):
    """
    Prints progress of processing as vertical dots
    """
    if layer_level is 1:
        print (".")

def arrange_css(target, destination):
    """
    Arranges the css files from target to destination
    """
    input_css_path = os.path.join(target, "theme", "iitg", "css")
    if os.path.exists(input_css_path):
        output_css_path = os.path.join(destination, "css")
        make_new_directory(output_css_path)
        os.chmod(output_css_path, folder_permissions)

        for file in os.listdir(input_css_path):
            if file.endswith(".css"):
                try:
                    shutil.copy2(os.path.join(input_css_path, file), output_css_path)
                except IOError:
                    print("Error: Unable to copy css files.")

        print("Arranged CSS files")
    else:
        print("\nError: CSS files missing in Target location.")


#-----------------------------------------------------------------------

if __name__ == '__main__':

    print("\nThis is not a standalone script.\nUse 'python3 run.py' to run copy-website.")
else:
    print("Imported helpers.py")

#-----------------------------------------------------------------------
