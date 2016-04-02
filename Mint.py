#!/usr/bin/env python
import os
import sys
import hashlib
import re
import time
record = ''
ISOTIMEFORMAT='%Y-%m-%d %X'
def SHA1FileWithName(fineName, block_size=64 * 1024):
    with open(fineName, 'rb') as f:
        sha1 = hashlib.md5()
        while True:
            data = f.read(block_size)
            if not data:
                break
            sha1.update(data)
        retsha1 = sha1.hexdigest()
        f.close()
        return retsha1
def GetValue(path):
    global record
    fl = os.listdir(path)
    for f in fl:
        if '$' in os.path.join(path,f):
            continue
        if os.path.isdir(os.path.join(path,f)):
            GetValue(os.path.join(path,f))
        else:
            fb = open(sys.path[0]+"//config//scan_extensions")
            fw = open(sys.path[0]+"//config//whitelist_dir")
            text = os.path.join(path,f)
            flag = False
            for line in fw:
                line=line.strip('\n')
                if re.match(line, text, re.IGNORECASE):
                    fb.close()
                    fw.close()
                    flag = True
                    break
            if flag == True:
                continue
            for linez in fb:
                linez=linez.strip('\n')
                if re.search('.'+linez, text, re.IGNORECASE):
                    record += "%s+%s\n" % (text,str(SHA1FileWithName(text)))
                    break
            fb.close()
            fw.close()
if __name__ == "__main__": 
    record = ''
    if len(sys.argv) == 2:
        if (sys.argv[1] == '-status'):
            file_object = open(sys.path[0]+'//config//scan_dir')
            try:
                all_the_text = file_object.read( )
            finally:
                file_object.close( )
            if (all_the_text == ''):
                all_the_text = 'WAIT TO ADD'
            print 'WEBSITE DIRECTORY TO SCAN:\n'+all_the_text+'\n'
            file_object = open(sys.path[0]+'//config//scan_extensions')
            try:
                all_the_text = file_object.read( )
            finally:
                file_object.close( )
            if (all_the_text == ''):
                all_the_text = 'WAIT TO ADD'
            print 'FILE EXTENSIONS TO SCAN:\n'+all_the_text+'\n'
            file_object = open(sys.path[0]+'//config//whitelist_dir')
            try:
                all_the_text = file_object.read( )
            finally:
                file_object.close( )
            if (all_the_text == ''):
                all_the_text = 'WAIT TO ADD'
            print 'WHITELIST TO SKIP:\n'+all_the_text+'\n'

        elif (sys.argv[1] == '-rec'):
            print 'RECORDING NOW,PLEASE WAIT\n'
            file_object = open(sys.path[0]+'//config//scan_dir')
            try:
                all_the_text = file_object.read( )
            finally:
                file_object.close( )
            all_the_text = all_the_text.strip('\n')
            GetValue(all_the_text)
            file_object = open(sys.path[0]+'//record//record', 'w')
            file_object.write(record)
            file_object.close()
            print record
            print 'RECORD FINISHED'

        elif (sys.argv[1] == '-scan'):
            if os.path.exists(sys.path[0]+'//log//log'):
                filesz = os.path.getsize(sys.path[0]+'//log//log')
                if filesz > 83886080:
                    os.remove(sys.path[0]+'//log//log')
            print 'SCANNING WEBSHELL NOW,PLEASE WAIT\n'
            file_object = open(sys.path[0]+'//config//scan_dir')
            try:
                all_the_text = file_object.read( )
            finally:
                file_object.close( )
            all_the_text = all_the_text.strip('\n')
            GetValue(all_the_text)
            file_object = open(sys.path[0]+'//temp//record', 'w')
            file_object.write(record)
            file_object.close()
            file_now = open(sys.path[0]+'//temp//record')
            for line in file_now:
                flagz = False
                file_past = open(sys.path[0]+'//record//record')
                for linez in file_past:
                    if line == linez:
                        flagz = True
                        break
                if flagz == True:
                    file_past.close()
                    continue
                else:
                    file_past.close()
                    output = open(sys.path[0]+'//log//log', 'a')
                    output.write('POSSIBLE WEBSHELL:'+line.split('+')[0]+'\nSHA1:'+line.split('+')[1]+time.strftime( ISOTIMEFORMAT, time.localtime() )+'--SCANNED\n\n')
                    output.close()
                    print 'POSSIBLE WEBSHELL:'+line.split('+')[0]+'\nSHA1:'+line.split('+')[1]
            print 'SCAN FINISHED'
        elif (sys.argv[1] == '-kill'):
            if os.path.exists(sys.path[0]+'//log//log'):
                filesz = os.path.getsize(sys.path[0]+'//log//log')
                if filesz > 83886080:
                    os.remove(sys.path[0]+'//log//log')
            print 'KILLING WEBSHELL NOW,PLEASE WAIT\n'
            file_object = open(sys.path[0]+'//config//scan_dir')
            try:
                all_the_text = file_object.read( )
            finally:
                file_object.close( )
            all_the_text = all_the_text.strip('\n')
            GetValue(all_the_text)
            file_object = open(sys.path[0]+'//temp//record', 'w')
            file_object.write(record)
            file_object.close()
            file_now = open(sys.path[0]+'//temp//record')
            for line in file_now:
                flagz = False
                file_past = open(sys.path[0]+'//record//record')
                for linez in file_past:
                    if line == linez:
                        flagz = True
                        break
                if flagz == True:
                    file_past.close()
                    continue
                else:
                    file_past.close()
                    output = open(sys.path[0]+'//log//log', 'a')
                    output.write('POSSIBLE WEBSHELL:'+line.split('+')[0]+'\nSHA1:'+line.split('+')[1]+time.strftime( ISOTIMEFORMAT, time.localtime() )+'--KILLED\n\n')
                    output.close()
                    os.remove(line.split('+')[0])
                    print 'POSSIBLE WEBSHELL:'+line.split('+')[0]+'\nSHA1:'+line.split('+')[1]+'KILLED\n'
            print 'KILL FINISHED'
        elif (sys.argv[1] == '-about'):
            print 'WELCOME TO USE MINT WEBSHELL DEFENDER 1.0'
        else:
            print '\nHOW TO USE:\n'
            print '1.Complete the configuration refer to the simple:'
            print '2.Use "-rec" to take notes of the SHA1 of WEBSITE files.If you have modified the WEBSITE files,You have to use "-rec" to take notes of the SHA1 of these files again.'
            print '3.Use "-scan" to scan the webshell files'
            print '4.Use "-kill" to kill the webshell files(Program will kill webshell automatically without notification)'
            print '5.Use "-status" to show the status of configuration'
            print '6.Use "-about" to show the software version\n'
            print 'MINT WEBSHELL DEFENDER DEVELOPED BY jkkj93'
    else:
        print '\nHOW TO USE:\n'
        print '1.Complete the configuration refer to the simple:'
        print '2.Use "-rec" to take notes of the SHA1 of WEBSITE files.If you have modified the WEBSITE files,You have to use "-rec" to take notes of the SHA1 of these files again.'
        print '3.Use "-scan" to scan the webshell files'
        print '4.Use "-kill" to kill the webshell files(Program will kill webshell automatically without notification)'
        print '5.Use "-status" to show the status of configuration'
        print '6.Use "-about" to show the software version\n'
        print 'MINT WEBSHELL DEFENDER DEVELOPED BY jkkj93'
