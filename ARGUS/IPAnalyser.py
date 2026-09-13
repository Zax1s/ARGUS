import requests
import ast
import json
from pathlib import Path
import nvdlib

def IPAnalyser(ip):
    OSAll = []
    hardwareAll = []
    servicesAll = []
    BASE_DIR = Path(__file__).resolve().parent
    config_path = BASE_DIR / "config.json"
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
        apiList = config["IPAnalyser"]
        for i in range(len(apiList)):
            if apiList[i]["use_api"] == "False":
                continue
            if apiList[i]["api_key"] == "None":
                api_url = apiList[i]["api_name"].format(ip=ip)
                resp = requests.get(url=api_url)
                data = ast.literal_eval(resp.text)
                try:
                    ports = sorted(data["ports"])
                    services = sorted(data["cpes"])
                    CVEs = sorted(data["vulns"], reverse=True)
                except:
                    return(None)

                for j in range(len(services)):
                    service = services[j].split(":")
                    if service[1] == "/o":
                        OSAll.append(service[2:])
                    elif service[1] == "/h":
                        hardwareAll.append(service[2:])
                    else:
                        servicesAll.append(service[2:])
            else:
                pass
                #Дописать работу с api_key

            for j in range(len(CVEs)):
                r = nvdlib.searchCVE(cveId=CVEs[j])[0]
                _, cve_score, cve_severity = r.score
                CVEs[j] = list([CVEs[j], cve_severity, cve_score])

            CVEs.sort(key=lambda x: x[2], reverse=True)

            return(ports, OSAll, hardwareAll, servicesAll, CVEs)