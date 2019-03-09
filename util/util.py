import os

def Traversal(filedir):
    file_list=[]
    for root,dirs,files in os.walk(filedir): 
        for file in files:
            file_list.append(os.path.join(root,file)) 
        for dir in dirs:
            Traversal(dir)
    return file_list

def is_img(path):
    ext = os.path.splitext(path)[1]
    ext = ext.lower()
    if ext in ['.jpg','.png','.jpeg','.bmp']:
        return True
    else:
        return False

def is_video(path):
    ext = os.path.splitext(path)[1]
    ext = ext.lower()
    if ext in ['.mp4','.flv','.avi','.mov','.mkv','.wmv','.rmvb']:
        return True
    else:
        return False

def  writelog(path,log):
    f = open(path,'a+')
    f.write(log+'\n')

def clean_tempfiles():
    if os.path.isdir('./tmp'):   
        os.system('rm -rf ./tmp')
    os.makedirs('./tmp')
    os.makedirs('./tmp/video2image')
    os.makedirs('./tmp/addmosaic_image')
    os.makedirs('./tmp/mosaic_crop')
    os.makedirs('./tmp/replace_mosaic')