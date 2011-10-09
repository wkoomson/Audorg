#!/usr/bin/env python2
#TODO LIST
#check if musicdir and newmusicdir exist, if not create it (newmusicdir)
#
#
#############
from os import rename, makedirs, listdir, remove
from os.path import isdir,isfile
from shutil import move
from Spr import tak, replace_all
import mutagen

class audorg:
    def main(self):
        musicdir =  raw_input("What directory are the music files located in? : ")#'../tests' 
    
        musfile = tak(musicdir)
        newmusicdir = raw_input("What folder should the music files be put into?: ") #'../tests/test' 
    
        dirp =  str(raw_input("Organizing Pattern:"))#'/artist/album/tracknumber - artist - title' 
    
        filep = dirp.split('/')[-1]
        dirp = dirp.split('/')[:-1]
        dirp = '/'.join(dirp)
        aud.org(musicdir,musfile,newmusicdir,dirp,filep)
    def org(self,musicdir,musfile,newmusicdir,dirp,filep):
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
                #Changing m to it's new location
                m = newmusicdir + dirpattern + '/' + m.split('/')[-1]
                rename(m, newmusicdir + dirpattern + '/' + filepattern + mfor)
                print('*')
                del m, dirdict, artist, album, title, tracknumber, genre, dirpattern
    def clean(self,musicdir,dtup=['.jpg','.png','.m3u','.ini','cue','txt']:
        dirs = tak(musicdir, formats=[''])
        for d in dirs:
            if :
                dirs.remove(d)
            else:
                pass
        for d in dirs and t in dtup:
            dlist = listdir(d)
            for files in dlist:
                if files.endswith(t):
                    remove(files)
                
        
        
        
aud = audorg()

if __name__ == '__main__':
    aud.main()