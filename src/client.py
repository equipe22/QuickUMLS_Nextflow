#!/usr/bin/env python3

from quickumls import get_quickumls_client
import argparse
import json

def readJsonConfig(pathToconfig):
    with open(pathToconfig) as f:
        config_json = json.load(f)
        print(config_json)
    return(config_json)

def writeJson(dataObject,pathToOutput):
    with open(pathToOutput, 'w', encoding='utf-8') as f:
        json.dump(dataObject, f, ensure_ascii=False, indent=4)

parser = argparse.ArgumentParser()
parser.add_argument("--inputFile", help="input text file")
parser.add_argument("--serverName", help="get servername")
args = parser.parse_args()
thisFile= open(args.inputFile,'r').read()
fileName=""
if args.inputFile.endswith(".html"):
    fileName=args.inputFile.split("/")[-1].replace(".html","_quickumls.json")
else:
    fileName=args.inputFile.split("/")[-1].replace(".txt","_quickumls.json")

pathToOoutput="/".join(args.inputFile.split("/")[:-1])


quickumls_server = args.serverName
matcher = get_quickumls_client(host=quickumls_server,port=4645)
annotations=matcher.match(thisFile, best_match=True, ignore_syntax=False)

print(" write the json "+fileName)
annotations_dict={"Annotators":{"quickumls-fre-hegp": "quickumls"}, "Entity":[] }
#fileName=pathToInput.split("/")[-1].replace(".html",".json")


for thisEntity in annotations:
    localAnnot={"position":{},"properties":[]}
    for thisAnnot in thisEntity:
        if 'start' not in localAnnot['position'].keys():
            localAnnot["position"]["start"]=thisAnnot['start']
        if 'end' not in localAnnot["position"].keys():
            localAnnot["position"]["end"]=thisAnnot['end']
        if 'texts' not in localAnnot.keys():
            localAnnot["texts"]=thisAnnot['ngram']
        thisProperty={"property":{"type":list(thisAnnot['semtypes']),"value":thisAnnot["term"],"cui":thisAnnot["cui"],"similarity":thisAnnot["similarity"] }}
        localAnnot["properties"].append(thisProperty)
    annotations_dict["Entity"].append(localAnnot)

writeJson(annotations_dict,fileName)
