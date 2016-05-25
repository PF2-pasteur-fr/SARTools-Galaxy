#Author: Loraine Gueguen

import sys
import os
import time
import argparse

def getfSize(fpath,outpath):
    """
    format a nice file size string
    """
    size = ''
    fp = os.path.join(outpath,fpath)
    if os.path.isfile(fp):
        size = '0 B'
        n = float(os.path.getsize(fp))
        if n > 2**20:
            size = '%1.1f MB' % (n/2**20)
        elif n > 2**10:
            size = '%1.1f KB' % (n/2**10)
        elif n > 0:
            size = '%d B' % (int(n))
    return size

# Define option
parser = argparse.ArgumentParser(description='Create an html page for downloading files from a directory') 
parser.add_argument('--tool', help='Galaxy tool', required=True)
parser.add_argument('--output_type', help='figures or tables', required=True)
parser.add_argument('--output_dir', help='Output directory', required=True)
parser.add_argument('--output_html', help='Output HTML file name', default='', required=True)

#Parse the command line
args = parser.parse_args() 
tool=args.tool
output_type=args.output_type
output_dir=args.output_dir
output_html=args.output_html


debut_html="""<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title></title>
    </head>
    <body>
    <h1>Galaxy Tool %s</h1>
""" %(tool)

fin_html="</body></html>"

html=debut_html
run_date=time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(time.time()))
html+='<div>Run at %s</div><br/>\n'%run_date
html+='<div><strong>%s</strong> available for downloading</div><br/>\n'%output_type

 
flist = os.listdir(output_dir)
flist.sort()


html+='<div><table cellpadding="3" cellspacing="3"><tr><th>Output File Name (click to view)</th><th>Size</th></tr>\n'

for f in flist :
	size=getfSize(f,output_dir)
	html+='<tr><td><a href="%s">%s</a></td><td>%s</td></tr>\n'%(f,f,size)
html+='</table></div><br/>\n'

html+=fin_html

htmlf = file(output_html,'w')
htmlf.write(html)
htmlf.close()
