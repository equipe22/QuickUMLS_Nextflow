#!/usr/bin/env python3
import os


nextflowConfig="""
process.$quickumls_1.container = 'quickumls-client-hegp'
 docker {
  enabled = true
  temp = 'RESULTPATH'
  runOptions = '--network annotations --user 1000:1000'
 }


"""
thisPath= os.getcwd()

resPath=thisPath+"/results"
print(resPath)
if not os.path.exists(resPath):
    os.makedirs(resPath)

nextflowConfig = nextflowConfig.replace("RESULTPATH",resPath)

configFile=open("config/nextflow.config","w")
configFile.write(nextflowConfig)
configFile.close()

print("Nextflow config is written")
