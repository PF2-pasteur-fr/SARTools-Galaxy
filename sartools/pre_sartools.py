#!/usr/bin/env python
#Author: Coline Billerey

from os.path import  basename, join
from os import getcwd, system
import argparse
from shutil import copyfile
import tempfile
import csv

def __main__():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--batch')
    parser.add_argument('--inputs', action='append' ,nargs='*')
    parser.add_argument('--outfile')
    parser.add_argument('--outarch')
    args = parser.parse_args()

    batch=args.batch
    outfile=args.outfile
    outarch=args.outarch
    inputs=args.inputs
    counts_files = open( outfile, 'w' )

    working_directory = getcwd()
    file_zip=working_directory+"/counts.zip"


    zip_cmd='zip -j %s' % (file_zip)
    if batch and batch!="NULL":
        counts_files.write("label\tfiles\tgroup\tbatch\n")
        for (level, filename, label, batch_name ) in inputs:
            filename_base = basename(filename)
            # For RSEM files we process files as HTSeq count output
            tmpdir = tempfile.mkdtemp()
            with open(filename, 'rb') as csvfile:
                with open(join(tmpdir, basename(filename)), 'wb') as out:
                    spamwriter = csv.writer(out, delimiter='\t')
                    reader = csv.DictReader(csvfile, delimiter='\t', skipinitialspace=True)
                    if len(reader.fieldnames) > 2:
                        for row in reader:
                            spamwriter.writerow((row['gene_id'], int(float(row['expected_count']))))
                        zip_cmd += ' %s ' % (join(tmpdir, basename(filename)))
                    else :
                        zip_cmd += ' %s ' % (filename)
            counts_files.write( label + "\t" + filename_base + "\t" + level + "\t" + batch_name + "\n" )
    else :
        counts_files.write("label\tfiles\tgroup\n")
        for (level, filename, label) in inputs:
            filename_base = basename(filename)
            # For RSEM files we process files as HTSeq count output
            tmpdir = tempfile.mkdtemp()
            with open(filename, 'rt') as csvfile:
                with open(join(tmpdir, basename(filename)), 'wt') as out:
                    spamwriter = csv.writer(out, delimiter='\t')
                    reader = csv.DictReader(csvfile, delimiter='\t', skipinitialspace=True)
                    if len(reader.fieldnames) > 2:
                        for row in reader:
                            spamwriter.writerow((row['gene_id'], int(float(row['expected_count']))))
                        zip_cmd += ' %s ' % (join(tmpdir, basename(filename)))
                    else:
                        zip_cmd += ' %s ' % (filename)

            counts_files.write( label + "\t" + filename_base + "\t" + level + "\n" )

    counts_files.close()
    system(zip_cmd)
    copyfile(file_zip,outarch)



if __name__=="__main__": 
    __main__()
