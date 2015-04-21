#---------------------------------------------------------------------
# Settings of copy-website script
#---------------------------------------------------------------------
import os

# Path to folder containing wget output of a website
SRC = os.path.join("..", "vlab")

# Path to folder in which modified website is to be deployed
DEST = os.path.join("..", "website12")

# Path to folder containing the css files with respect to src
TARGET_CSS = os.path.join("theme", "iitg", "css")

# Permissions of folders created in dest (used by arrange_css)
FOLDER_PERMISSIONS = 0o777			# append 0o in python3
