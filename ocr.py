import os
from cnocr import CnOcr
import re
import sys

def is_image_file(filename):
    return any(filename.endswith(ext) for ext in ['.png','.jpg','jpeg','PNG','JPG','JPEG'])

dir=sys.argv[1]+'/'
print(dir)
tem = os.listdir(dir)


jpg = [dir+x for x in tem if is_image_file(x)]

pattern = re.compile(r".(png|jpg|jpeg|PNG|JPG|JPEG)")
log = [pattern.sub('.log',j) for j in jpg]
n=len(jpg)

for i in range(n):
    ocr = CnOcr()
    res = ocr.ocr(jpg[i])
    print("Extracting from: ",jpg[i],"(",i,"/",n,") ...")
    with open(log[i],'w') as o:
        for j in range(len(res)):
            tmp = ''.join(res[j][0]) + '\n'
            o.write(tmp)
print('Done!')
