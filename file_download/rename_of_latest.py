import os
import glob

dwnld_fle_path = r"D:/myGit/rep-one/file_download/file"


filename = max(glob.iglob('%s/*.zip'%(dwnld_fle_path)), key=os.path.getctime)
os.rename(filename, '%s/source.csv.zip'%(dwnld_fle_path))
print filename

