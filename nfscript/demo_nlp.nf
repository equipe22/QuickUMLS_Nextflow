
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

