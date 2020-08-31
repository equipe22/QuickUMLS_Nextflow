#!/usr/bin/env python3
import os


nextflowConfig="""
process.$quickumls_1.container = 'quickumls-democlient-hegp'
 docker {
  enabled = true
  runOptions = '--network annotations --user 1000:1000'
 }

"""

nextflowScript='''
params.files = ['FILESPATH']
params.results ="RESULTPATH"
Channel.fromPath( params.files ).into{ annotations_quickumls }

process quickumls_1{
	container 'quickumls-democlient-hegp'
	maxForks 15
	errorStrategy 'ignore'
	time '200m'

	input:
	    file(process_1_val) from annotations_quickumls


	output:
        file '*.json' into process_cui

	script:
	    """
        python /home/quickumls/src/client.py --inputFile $process_1_val --serverName quickumlsserver
	    """
}



'''+"""

process sendInDir1{
	maxForks 10

	input:
	    file(f) from process_cui


	output:
        stdout  process_stdout_cui

	shell:
	    '''
	echo !{f}
        cp !{f} !{params.results}
	    '''
}

process_stdout_cui.println { it }

"""


thisPath= os.getcwd()

resPath=thisPath+"/results"
dataPath=thisPath+"/data/demo/*txt"
scriptPath=thisPath+"/nfscript"
print(resPath)
if not os.path.exists(resPath):
    os.makedirs(resPath)

if not os.path.exists(scriptPath):
    os.makedirs(scriptPath)

nextflowConfig = nextflowConfig.replace("RESULTPATH",resPath)
nextflowScript =nextflowScript.replace("RESULTPATH",resPath).replace("FILESPATH",dataPath)
configFile=open("config/nextflow.config","w")
configFile.write(nextflowConfig)
configFile.close()
print("Nextflow config is written")


scriptFile=open("nfscript/demo_nlp.nf","w")
scriptFile.write(nextflowScript)
scriptFile.close()
print("Nextflow Script is written")
