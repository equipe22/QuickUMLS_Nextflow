# Description 
Docker Image of the QuickUMLS tools (https://github.com/Georgetown-IR-Lab/QuickUMLS)

tested With UMLS2018AA data



Maintainer :  Alice ROGIER <alice.rogier-ext@aphp.fr>

# REQUIREMENTS:
docker https://docs.docker.com/engine/install/

nextflow https://www.nextflow.io/


# Dataset
located on the data folder:
are the result of the  pubmed request from 2000 to 2019

("EHR" or "biomedical NLP" or "clinical NLP" or "clinical natural language processing" or
"natural language processing" OR "NLP" OR "natural language processing") AND
("system" or "framework" or "tool" or "workflow" or "pipeline" or "architecture")
and ("text mining" or "platform")

each result is put on a separated file


# How to use

## 1) Download MRSTY.RRF and MRCONSO.RRF in the UMLS folder.


## 2)  Build the image
To build both the client and the server image run 

    bash bin/build.sh

## 3) start the server

### a) create a docker network named annotations 

    bash bin/createNetwork.sh

###  b) start the server it will be available from port localhost:8080

    bash bin/startServer.sh

NB: if you want to change the server port modify it in bin/startServer.sh
Furthermore we create a docker network to ease the communication with the docker client.

## 4) start the client

### a) start client

    bash bin/client_demo.sh

NB: It will take as input data in folder data

### b) call the script

An example of client, server interaction is located on src/quickumls_main.py


 python3 /home/quickumls/src/client.py --serverName quickumlsserver --inputFile /home/quickumls/tmp/demo/input_1.txt 

