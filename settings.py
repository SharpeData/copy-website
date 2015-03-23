#-----------------------------------------------------------------------
#
# Settings of copy-website script
#
#-----------------------------------------------------------------------
import os


# Path to folder containing wget output of a website
src = os.path.join("..", "vlab")


# Path to folder in which modified website is to be deployed
dest = os.path.join("..", "website5")

# Path to folder containing the css files with respect to src
target_css = os.path.join("theme", "iitg", "css")


# Permissions of folders created in dest (used by arrange_css)
folder_permissions = 0o777			# append 0o in python3





#-----------------------------------------------------------------------

if __name__ == '__main__':

	print("\nThis is not a standalone script.\nUse 'python3 run.py' to run copy-website.")
else:
    print("\nImported settings.py")

#-----------------------------------------------------------------------
