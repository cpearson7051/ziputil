import os
import zipfile

class zipClass:
  
  def __init__(self, zipname, frompath, topath, filetype):
    self.zipname = zipname
    self.frompath = frompath
    self.topath = topath
    self.ftype = filetype    
    self.zipNow()
            
  def zipNow(self):
    self.zipf = zipfile.ZipFile(self.topath+self.zipname, 'w')
    for file in os.listdir(self.frompath):
      if file.endswith(self.ftype):
        try:
          self.zipf.write(self.frompath+file, file)
        except IOError:
          None
      else:
        continue
    self.zipf.close()  
    