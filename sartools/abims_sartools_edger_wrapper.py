#abims_sartools_edger_wrapper.py
#Author: Loraine Gueguen
# imports
import os, argparse



def main():

    print("Start of galaxy wrapper")

    #Check R and Rscript are installed
    check_r_cmd="command -v R >/dev/null 2>&1 || { echo >&2 'This tool requires R but it is not installed.  Aborting.'; exit 1; }"
    check_rscript_cmd="command -v Rscript >/dev/null 2>&1 || { echo >&2 'This tool requires Rscript but it is not installed.  Aborting.'; exit 1; }"
    os.system(check_r_cmd)
    os.system(check_rscript_cmd)

    #Get arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--projectName')
    parser.add_argument('--author')
    parser.add_argument('--targetFile')
    parser.add_argument('--rawDir')
    parser.add_argument('--featuresToRemove')
    parser.add_argument('--varInt')
    parser.add_argument('--condRef')
    parser.add_argument('--batch')
    parser.add_argument('--alpha')
    parser.add_argument('--pAdjustMethod')
    parser.add_argument('--cpmCutoff')
    parser.add_argument('--geneSelection')
    parser.add_argument('--normalizationMethod')
    parser.add_argument('--colors')
    parser.add_argument('--figures_html')
    parser.add_argument('--figures_html_files_path')
    parser.add_argument('--tables_html')
    parser.add_argument('--tables_html_files_path')
    parser.add_argument('--rdata')
    parser.add_argument('--report_html')
    parser.add_argument('--log')
    args = parser.parse_args()
    projectName=args.projectName
    author=args.author
    targetFile=args.targetFile
    rawDir=args.rawDir
    featuresToRemove=args.featuresToRemove
    varInt=args.varInt
    condRef=args.condRef
    batch=args.batch
    alpha=args.alpha
    pAdjustMethod=args.pAdjustMethod
    cpmCutoff=args.cpmCutoff
    geneSelection=args.geneSelection
    normalizationMethod=args.normalizationMethod
    colors=args.colors
    figures_html=args.figures_html
    figures_html_files_path=args.figures_html_files_path
    tables_html=args.tables_html
    tables_html_files_path=args.tables_html_files_path
    rdata=args.rdata
    report_html=args.report_html
    log=args.log
    #Print the parameters selected
    print("Wrapper arguments: %s") %(args)

    #Get the working directory path
    working_directory = os.getcwd()
    #Get the script directory path
    script_directory=os.path.dirname(os.path.realpath(__file__))
 
    #Unzip files from rawDir
    rawDir_unzipped_path=working_directory+"/rawDir_unzipped"
    os.mkdir(rawDir_unzipped_path)
    unzip_cmd="unzip -j %s -d %s" % (rawDir,rawDir_unzipped_path) #-j arg: junk paths
    os.system(unzip_cmd)

    #Create the command
    cmd="Rscript --no-save --no-restore %s/template_script_edgeR.r --projectName %s --author %s " % (script_directory,projectName,author)
    cmd+="--targetFile %s --rawDir %s --featuresToRemove %s --varInt %s --condRef %s " % (targetFile,rawDir_unzipped_path,featuresToRemove,varInt,condRef)
    if batch and batch!="NULL":
        cmd+="--batch %s " % (batch)
    if alpha:
        cmd+="--alpha %s " % (alpha)
    if pAdjustMethod:
        cmd+="--pAdjustMethod %s " % (pAdjustMethod)
    if cpmCutoff:
        cmd+="--cpmCutoff %s " % (cpmCutoff)
    if geneSelection:
        cmd+="--gene.selection %s " % (geneSelection)
    if normalizationMethod:
        cmd+="--normalizationMethod %s " % (normalizationMethod)
    if colors:
        cmd+="--colors %s " % (colors)
    cmd+="> %s 2>&1" % (log)
    print("Rscript command: %s") % (cmd)
    os.system(cmd)

    #Get output files
    os.mkdir(figures_html_files_path)
    os.mkdir(tables_html_files_path)
    rsync_figures_dir_cmd="rsync -r figures/* %s/." % (figures_html_files_path)
    rsync_tables_dir_cmd="rsync -r tables/* %s/." % (tables_html_files_path)
    os.system(rsync_figures_dir_cmd)
    os.system(rsync_tables_dir_cmd)
    figures_html_create_cmd="python %s/make_html.py --tool SARTools_edgeR --output_type Figures --output_dir %s --output_html %s" % (script_directory,figures_html_files_path,figures_html)
    tables_html_create_cmd="python %s/make_html.py --tool SARTools_edgeR --output_type Tables --output_dir %s --output_html %s" % (script_directory,tables_html_files_path,tables_html)
    os.system(figures_html_create_cmd)
    os.system(tables_html_create_cmd)
    rsync_rdata_file_cmd="rsync %s.RData %s" % (projectName,rdata)
    rsync_report_file_cmd="rsync %s_report.html %s" % (projectName,report_html)
    os.system(rsync_rdata_file_cmd)
    os.system(rsync_report_file_cmd)

    print("End of galaxy wrapper")

if __name__ == '__main__':
    main()


