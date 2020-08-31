# Description 
Docker Image of the QuickUMLS tools (https://github.com/Georgetown-IR-Lab/QuickUMLS)

tested With UMLS2018AA data



Maintainer :  Alice ROGIER <alice.rogier-ext@aphp.fr>

# REQUIREMENTS:
docker https://docs.docker.com/engine/install/

nextflow https://www.nextflow.io/


# Dataset
located on the data/demo folder:
are the result of the  pubmed request from 2000 to 2019

("EHR" or "biomedical NLP" or "clinical NLP" or "clinical natural language processing" or
"natural language processing" OR "NLP" OR "natural language processing") AND
("system" or "framework" or "tool" or "workflow" or "pipeline" or "architecture")
and ("text mining" or "platform")

each result is put on a separated file


# How to use

## 1) Add MRSTY.RRF and MRCONSO.RRF in the UMLS folder.


## 2)  Build the image
To build both the client and the server image run 

```bash

    make build

```


## 3) start the server

### a) create a docker network named annotations 

```bash

    make createNetwork

```


###  b) start the server it will be available from port localhost:8080

```bash

    make startServer

```

NB: if you want to change the server port modify it in bin/startServer.sh
Furthermore we create a docker network to ease the communication with the docker client.

## 4) Live demo with the client

### a) start client

```bash

    make liveDemo

```


NB: It will take as input data in folder data

### b) call the script

An example of client, server interaction is located on src/quickumls_main.py


```bash

    #in the container run 
    python3 /home/quickumls/src/client.py --serverName quickumlsserver --inputFile /home/quickumls/tmp/demo/input_1.txt 

```

## 4) RUN nexflow and analyse all the demo data folder
The user need to install nexflow as required

### a) Generate Nexflow script

```bash

    make generate

```
### b) run Nexflow script

```bash

    make runnf 
    #or
    nextflow run nfscript/demo_nlp.nf -c config/nextflow.config                                                                                                                                                                                                                                  
```

results will be output on the result folder


# Customization:

If the user wants to custom the script :

```bash
nfscript/demo_nlp.nf  # for the nextflow script
config/nextflow.config #nexflow config
src/client.py # quickumls client 


```
