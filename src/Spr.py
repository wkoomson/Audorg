'''
Created on Aug 7, 2011

@author: Willie Koomson
'''
def tak(d,formats = ['.flac','.mp3','.m4a','.aac','.wav','.ogg']):
    from glob import glob
    if d.endswith('/'):
        d = d[:-1]
    else:
        pass
    files  = []
    for form in formats:
        x = 1
        counter = 1
        while x > 0:
            try:
                musfile = glob(d + '/*' * counter + form)
                if musfile == [] and counter >= 3:
                    raise OSError('Deep level, done')
                else:
                    pass
                files.extend(musfile)
                del musfile
                counter = counter + 1
            except OSError:
                x = 0
            finally:
                pass
    return files
def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text
def ynt(inp):
    if inp.startswith('y'):
        return True
    elif inp.startswith('Y'):
        return True
    elif inp.startswith('n'):
        return False
    elif inp.startswith('N'):
        return False
