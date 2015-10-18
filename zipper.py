import os
import zipfile


def zipdir(path, zip):
  for file in os.listdir(path):
    if file.endswith('.txt'):
      try: 
        zip.write(path+file, file)
      except IOError: 
        None
    else:
      continue       
      
      
def main():
  frompath = '/Users/path'
  topath = 
  zip = zipfile.ZipFile(topath+'myzip.zip', 'w')
  zipdir(frompath, zip)
  zip.close()
  
if __name__ == '__main__':
  main()
  
