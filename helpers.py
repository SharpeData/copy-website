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

import os, shutil, re
from bs4 import BeautifulSoup
from settings import folder_permissions, target_css



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

def copy_directory(src, dest):
    try:
        shutil.copytree(src, dest)
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    except OSError as e:
        print('Directory not copied. Error: %s' % e)


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


def make_menu_pages(src, dest, menu_links):

    with open(os.path.join(src, "index.html")) as f:
        soup = BeautifulSoup(f.read())

    for link_tag in soup.find_all('a', attrs={"href": re.compile("^index.html@pg")}):
        link = link_tag.get('href')
        if link is None:
            continue

        name = link_tag.string.strip(" \t\n\r").partition(' ')[0].lower()
        menu_links[link] = name

        with open(os.path.join(src, link)) as f:
            menu_soup = BeautifulSoup(f.read())

        for menu_link_tag in menu_soup.find_all('a', attrs={"href": "index.php.html"}):
            menu_link_tag['href'] = "../../"

        for menu_link_tag in menu_soup.find_all('a', attrs={"href": re.compile("^index.html@pg")}):
            menu_link_tag['href'] = "../../menus/" + menu_link_tag.string.strip(" \t\n\r").partition(' ')[0].lower()

        parse_css_links(menu_soup, layer_level = 2)
        parse_images(menu_soup, layer_level = 2)

        make_new_directory(os.path.join(dest, "menus", name))
        save_html(menu_soup, os.path.join(dest, "menus", name, "index.html"))


def arrange_resources(src, dest):
    """
    Arranges all resources from src into dest
    """

    list_of_dirs = [name for name in os.listdir(src)
                    if os.path.isdir(os.path.join(src, name))]
    for dir_name in list_of_dirs:
        copy_directory(os.path.join(src, dir_name), os.path.join(dest, "res", dir_name))

def parse_css_links(soup, layer_level):
    """
    Parses css links in html files.
    Modifies all css links according to layer_level
    """
    for link_tag in soup.find_all('link'):
        link = link_tag.get('href')
        if link is None:
            continue
        if link.endswith(".css"):
            link_tag['href'] = layer_level * "../" + "res/" + link
            if layer_level is 3:
                link_tag['href'] = 4 * "../" + "res/" + link

def parse_images(soup, layer_level):
    """
    Parses image links in html files
    Modifies all images links according to layer_level
    """
    for link_tag in soup.find_all('img'):
        link = link_tag.get('src')
        if link is None:
            continue
        if not link.startswith("http"):
            link_tag['src'] = layer_level * "../" + "res/" + link
            if layer_level is 3:
                link_tag['src'] = 4 * "../" + "res/" + link

def parse_menu_links(layer_level, link_tag, menu_links):
    """
    Modifies links in the menu
    """
    link = link_tag.get('href')
    if link is None:
        return
    if link.startswith("index.php.html"):
        link_tag['href'] = layer_level * "../"
        if layer_level is 3:
            link_tag['href'] = 4 * "../"

    for menu_link, menu_name in menu_links.iteritems():
        if link.startswith(menu_link):
            link_tag['href'] = layer_level * "../" + "menus/" + menu_name
            if layer_level is 3:
                link_tag['href'] = 4 * "../" + "menus/" + menu_name


#-----------------------------------------------------------------------

if __name__ == '__main__':

    print("\nThis is not a standalone script.\nUse 'python3 run.py' to run copy-website.")
else:
    print("Imported helpers.py")

#-----------------------------------------------------------------------