# Copy-Website Python script
Crawls through the 'wget' output of a website and organizes it into folders for easy deployment.

### Installing Pre-requisites

##### Python 2 or 3
Copy-Website is tested to work with Python 2.7.6 and Python 3.4.0 in Linux and Windows.

For installing python, check out their [downloads](https://www.python.org/downloads/) page.

##### Beautiful Soup
Copy-Website requires [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/) for screen scraping.
You can download this package using pip or easy_install as follows:
```
pip install beautifulsoup4
```
```
easy_install beautifulsoup4
```

##### Wget output
The scripts operates on output files of 'wget', a computer program that retrieves content from web servers.
To generate these files, you can run `wget-script.sh` in copy-website folder.

### Running
Before running the script, you need to specify paths to source and the destination folders. Source folder must contain the output files of 'wget'. Destination folder is where you want to generate the organized website. In addition, you need to specify the path to the css folder in the source. You can now run the script using the command in the copy-website folder:
```
python run.py
```

### Customizing the script

Copy-Website script parses the html files using a layer-based architecture. In each layer, it searches for certain patterns in links and crawls into the web pages to find more links recursively. At each recursion, it organizes the layer into folders forming a tree structure of website.

This script by default works only with the output of wget-script.sh. To modify this script to suit a required website, you can customize parsing and helper functions to set the patterns you search for in the links.
