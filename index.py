from os import read, write
import os
from pathlib import Path
import yaml
import json

# imageFile = input("enter path to image file: ")
namespace = ("enter namespace: ")
imageFile = ("test.txt")
input_file = open(imageFile,"r") 
for line in input_file.readlines():
    Path(line).mkdir(parents=True, exist_ok=True)
    Path(line+"/Image repository").touch()
    Path(line+"/Image policy").touch()
    Path(line+"/arg").touch()
    repository = open('image_repository.yaml',"r+")
    read_repository = yaml.safe_load(repository)
    file = open(line+"/Image repository.yaml","w+")
    yaml.dump(read_repository, file,)
    file.close()
    policy = open('image_policy.yaml',"r+")
    read_policy = yaml.safe_load(policy)
    file = open(line+"/Image policy.yaml","w+")
    yaml.dump(read_policy, file)
    file.close()
