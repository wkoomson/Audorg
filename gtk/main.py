#!/usr/bin/env python2
#TODO LIST
# finish progress bar
#############
from sys import exit
from os import rename, makedirs, listdir, remove
from os.path import isdir,isfile
from shutil import move
from Spr import tak, replace_all
import mutagen
import gtk
import gtk.glade

try:
  import pygtk
  #tell pyGTK, if possible, that we want GTKv2
  pygtk.require("2.0")
except:
  print "You need to install pyGTK or GTKv2 or set your PYTHONPATH correctly"
  print "try: export PYTHONPATH=/usr/local/lib/python2.2/site-packages/"
  sys.exit(1)
  
check = 'Check!'  
  
class audorg:   
    def __init__(self):
        self.gladefile = "audorg.glade"
        self.windowname = "Audorg"
        self.wTree = gtk.glade.XML(self.gladefile, self.windowname)
        
        self.window = self.wTree.get_widget("Audorg")
        self.musicdir = self.wTree.get_widget('musicdir')
        self.newmusicdir = self.wTree.get_widget('newmusicdir')
        self.dirp = self.wTree.get_widget('dirp')
        self.clean = self.wTree.get_widget('clean')
        self.start = self.wTree.get_widget('start')
        self.progressbar = self.wTree.get_widget('progressbar')
        
        self.window.show()
        dic = {"on_Audorg_destroy" : self.quit,
               "on_start_clicked" : self.on_start_clicked}
        
        self.wTree.signal_autoconnect(dic)
        
        
    def org(self,musicdir,musfile,newmusicdir,dirp,filep):
        previous = 0
        for m in musfile:
            mfor = '.' + m.split(".")[-1]
            try:
                musta = mutagen.File(m, easy=True)
                artist = str(musta['artist'][0])
                album = str(musta['album'][0])
                title = str(musta['title'][0])
                tracknumber = str(musta['tracknumber'][0]).split('/')[0]
                genre = str(musta['genre'])[2:-3]
                dirdict = {'artist':artist, 'album':album, 'title':title,
                           'tracknumber':tracknumber, 'genre':genre}
                filepattern = replace_all(filep, dirdict) # PROBLEM LINE
                print(filepattern)
                dirpattern = replace_all(dirp, dirdict)
                makedirs(newmusicdir + dirpattern)
            except OSError:
                pass
            finally:
                if isfile(newmusicdir + dirpattern + '/' + m.split('/')[-1]):
                    pass
                elif not isfile(newmusicdir + dirpattern + '/' + m.split('/')[-1]):
                    move(m,newmusicdir + dirpattern)
                m = newmusicdir + dirpattern + '/' + m.split('/')[-1]
                rename(m, newmusicdir + dirpattern + '/' + filepattern + mfor)
                print('*')
                fraction = 1.0/len(musfile) + previous
                self.progressbar.set_fraction(fraction)
                previous = previous + 1.0/len(musfile)
                del m, dirdict, artist, album, title, tracknumber, genre, dirpattern
        self.progressbar.set_fraction(0)        
                
    def on_start_clicked(self,widget):
        print check
        
        musicdir =  self.musicdir.get_filename()
        newmusicdir =  self.newmusicdir.get_filename()
        dirp = self.dirp.get_text()
        clean = self.clean.toggled()
        
        musfile = tak(musicdir)
        
        filep = dirp.split('/')[-1]
        dirp = dirp.split('/')[:-1]
        dirp = '/'.join(dirp)
        
        self.musicdir.set_sensitive(False)
        self.newmusicdir.set_sensitive(False)
        self.dirp.set_sensitive(False)
        self.clean.set_sensitive(False)
        self.start.set_sensitive(False)
        
        print check
        
        self.org(musicdir,musfile,newmusicdir,dirp,filep)
        
        if clean:
            print 'Happily Empty!'
        else:
            pass
        
        self.musicdir.set_sensitive(True)
        self.newmusicdir.set_sensitive(True)
        self.dirp.set_sensitive(True)
        self.clean.set_sensitive(True)
        self.start.set_sensitive(True)
        
    def quit(self,widget):
        gtk.main_quit()
        sys.exit()
        
if __name__ == '__main__':
    aud=audorg()
    gtk.main()