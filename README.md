# Description 
Docker Image of the QuickUMLS tools (https://github.com/Georgetown-IR-Lab/QuickUMLS)

tested With UMLS2018AA data



Maintainer :  Alice ROGIER <alice.rogier-ext@aphp.fr>

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

    python3 /home/quickumls/src/quickumls_main.py --inputFile demo.txt --serverName quickumlsserver


