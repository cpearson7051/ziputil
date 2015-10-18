import os
import zipfile


def zipdir(path, zip):
  for file in os.listdir(path):
    if file.endswith('.tif'):
      try: 
        zip.write(path+file, file)
      except IOError: 
        None
    else:
      continue       
      
      
def main():
  frompath = '/mnt/ephem0/Processed/1234/'
  topath = 
  zip = zipfile.ZipFile(topath+'1234.zip', 'w')
  zipdir(frompath, zip)
  zip.close()
  
if __name__ == '__main__':
  main()
  
