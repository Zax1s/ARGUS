import requests
import ast
import json
from pathlib import Path

def subdomainFinder(domainName):
        subdomainList = []
        BASE_DIR = Path(__file__).resolve().parent
        config_path = BASE_DIR / "config.json"
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            apiList = config["SubdomainLookup"]
            for i in range(len(apiList)):
                if apiList[i]["use_api"] == "False":
                    continue
                if apiList[i]["api_key"] == "None":
                    api_url = apiList[i]["api_name"].format(domainName=domainName)
                    resp = requests.get(url=api_url)
                    if resp.status_code != 200:
                        continue
                    data = ast.literal_eval(resp.text)
                    for i in range(len(data)):
                        nameValue = data[i]["name_value"].split("\n")
                        for j in range(len(nameValue)):
                            if nameValue[j] not in subdomainList:
                                subdomainList.append(nameValue[j])
                else:
                    pass
                    #Дописать api_key

                subdomainList.sort()
                return(subdomainList)

#print(subdomainFinder("absatz.media"))