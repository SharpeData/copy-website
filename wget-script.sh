#!/bin/bash
# wget \
#     --recursive \ 			//download the entire Web site
#     --no-clobber \ 			//don't overwrite any existing files (used in case the download is interrupted and resumed)
#     --page-requisites \		//get all the elements that compose the page (images, CSS and so on)
#     --html-extension \		//save files with the .html extension
#     --convert-links \			//convert links so that they work locally, off-line
#     --restrict-file-names=windows \	//modify filenames so that they will work in Windows as well
#     --domains website.org \		//don't follow links outside 'website.org'
#     --no-parent \			//don't follow links outside the directory 'tutorials/html/'
# www.website.org/tutorials/html/

THEWEBSITE="iitg.vlab.co.in"
THEFOLDER="/"

wget \
     --recursive \
     --no-clobber \
     --page-requisites \
     --html-extension \
     --convert-links \
     --restrict-file-names=windows \
     --domains $THEWEBSITE \
     --no-parent \
         $THEWEBSITE/$THEFOLDER/
firefox $THEWEBSITE/$THEFOLDER/index.html

