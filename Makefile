##
# Project Title
#
# @file
# @version 0.1



# end

help: ## Display available commands in Makefile
	@grep -hE '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build: ## Build dinstance
	@bash bin/build.sh

createNetwork: ## createdocker Network
	@bash bin/createNetwork.sh

livedemo: ## live demo of quickumls client
	@bash bin/client_demo.sh

generate: ## generate nextflow conf and script files
	@python3 bin/generateNextflowConf.py

runnf: ## run nexflow script agains demo data
	@nextflow run nfscript/demo_nlp.nf -c config/nextflow.config
