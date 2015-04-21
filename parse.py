#---------------------------------------------------------------------
# Parsing functions for copy-website script
#---------------------------------------------------------------------
#   Author            : Jayadeep Karnati
#   Last modified     : 15rd Feb 2015
#   Compatibility     : Python3
#   Requirements      : Beautiful Soup
#---------------------------------------------------------------------

import os
import shutil
from bs4 import BeautifulSoup
from helpers import link_is_appropriate, get_unique_name, make_new_directory
from helpers import save_html, print_progress, print_error_when_directly_run
from helpers import parse_images, parse_menu_links, parse_css_links

file1=open("downloadablelinks.txt", "r")
downloadablelinks=file1.readlines()
file1.close()
downloadablelinks = [word.rstrip("\n") for word in downloadablelinks]        
file2=open("activedownloadablelinks.txt", "r")
activedownloadablelinks=file2.readlines()
file2.close()
activedownloadablelinks = [word.rstrip("\n") for word in activedownloadablelinks]
file3=open("activeallexternallinks.txt", "r")
activeallexternallinks=file3.readlines()
file3.close()
activeallexternallinks = [word.rstrip("\n") for word in activeallexternallinks]




def parse_links(names, src, menu_links, input_path, output_path,
                layer_level, recursion_depth):
    """
    Parses links and organizes folders recursively
    - Finds suitable links in html file corresponding to input path
    - Changes the links by giving them unique names
    - Creates a new directory with that unique name in the output_path
    - Generates the modified html file in the output_path
    """
    print_progress(layer_level)

    with open(input_path) as f:
        soup = BeautifulSoup(f.read())
        html_path = os.path.join(output_path, "index.html")
    parse_css_links(soup, layer_level)
    parse_images(soup, layer_level)
    save_html(soup, html_path)

    bread_tag = soup.find("div", attrs={"class": "breadcum"})
    bread_count = 0
    if bread_tag:
        if bread_tag.find_all('a'):
            for link_tag in reversed(bread_tag.find_all('a')):
                link_tag['href'] = bread_count*"../"
                if layer_level is 3:
                    link_tag['href'] = bread_count*"../" + "../"
                bread_count = bread_count + 1
                
    for link_tag in soup.find_all('a'):
        parse_menu_links(layer_level, link_tag, menu_links)
        link = link_tag.get('href')
        if link is None:
            continue
        elink = link_tag.get('href')
        if link.startswith("http://"):    
            if (link  in downloadablelinks):
                link = link[6:]
                link_tag['href'] = layer_level*"../" + "../external" + link
                if layer_level is 3:
                    link_tag['href'] = 4*"../" + "../external" + link
            elif (link in activeallexternallinks):
                link_tag['href'] = 'javascript:var c=confirm("Do You wish to access internet?");if(c==true){window.location="'+elink+'";}'
            else: 
                link_tag['href'] = 'javascript:alert("Link is dead");'    
        if link_is_appropriate(link, layer_level):
            name = link_tag.string.strip(" \t\n\r").partition(' ')[0].lower()
            name = get_unique_name(name, names)
            if layer_level is 2:
                name = name + "/theory"
            link_tag['href'] = name
            new_output_path = os.path.join(output_path, name)
            make_new_directory(new_output_path)

            if recursion_depth > 0:
                parse_links(names, src, menu_links,
                            input_path=os.path.join(src, link),
                            output_path=new_output_path,
                            layer_level=layer_level + 1,
                            recursion_depth=recursion_depth - 1)
        if (layer_level is 1 and link.count('&') is 3):
            name2 = link_tag.string.strip(" \t\n\r").partition(' ')[0].lower()
            link_tag['href'] = name + "/" + name2 + "/theory"         
        parse_last_layer(link_tag, names, src, menu_links, input_path,
                         output_path, layer_level, recursion_depth)
    save_html(soup, html_path)


def parse_last_layer(link_tag, names, src, menu_links,
                     input_path, output_path,
                     layer_level, recursion_depth):
    link = link_tag.get('href')
    if (link.startswith("index.html@sub") and layer_level is 3 and
        link.count('&') is 3):
        tab_tags = link_tag.find_all("div", attrs={"id": "tab_name"})
        for tab_tag in tab_tags:
            tab_name = tab_tag.string.strip(" \t\n\r").partition(' ')[0]
            tab_name = tab_name.lower().rstrip()
            link_tag['href'] = "../" + tab_name

            if tab_name is not "theory":
                if recursion_depth >= 0:
                    new_output_path = os.path.dirname(output_path)
                    new_output_path = os.path.join(new_output_path, tab_name)
                    make_new_directory(new_output_path)
                    parse_links(names, src, menu_links,
                                input_path=os.path.join(src, link),
                                output_path=new_output_path,
                                layer_level=3,
                                recursion_depth=recursion_depth-100)

print_error_when_directly_run(__name__)
