#-----------------------------------------------------------------------
#
# Settings of copy-website script
#
#-----------------------------------------------------------------------


# Path to folder containing wget output of a website
target = "../vlab/"


# Path to folder in which modified website is to be deployed
destination = "../website5/"

# Permissions of folders created in destination (used by arrange_css)
folder_permissions = 0o777			# append 0o in python3





#-----------------------------------------------------------------------

if __name__ == '__main__':

	print("\nThis is not a standalone script.\nUse 'python3 run.py' to run copy-website.")
else:
    print("\nImported settings.py")

#-----------------------------------------------------------------------
