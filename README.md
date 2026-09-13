# ARGUS
Automated Recon &amp; Gathering Utility Suite

A lightweight Python-based reconnaissance tool that discovers subdomains, resolves their IP addresses, and gathers open ports, operating systems, hardware, services, and associated CVEs — all in one pass.

## Features

- **Subdomain discovery** via [crt.sh](https://crt.sh/) (certificate transparency logs)
- **IP resolution** for each discovered subdomain
- **Host analysis** via [Shodan InternetDB](https://internetdb.shodan.io/) — open ports, OS, hardware, and services
- **CVE enrichment** via [NVD](https://nvd.nist.gov/) with severity and CVSS scores
- **Extensible** — APIs are configured through `config.json`, with placeholders for API-key-based providers

## Requirements

- Python 3.8+
- Dependencies:
  ```bash
  pip install requests nvdlib
  ```

## Installation

```bash
git clone https://github.com/<your-username>/argus.git
cd argus
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

When prompted, enter a target domain:

```
example.com
```

### Example Output

```
========================================
sub1.example.com
sub2.example.com
...

========================================
IP: 93.184.216.34
Open ports: 80 443
OS: ['Linux']
Hardware: []
Services: [['nginx', '1.25.3'], ['OpenSSL', '3.0.0']]
CVE list:
CVE-2023-XXXXX HIGH - 8.1
CVE-2022-YYYYY MEDIUM - 5.3
========================================
```

## Configuration

All data sources are declared in `config.json`:

```json
{
  "SubdomainLookup": [
    { "api_name": "https://crt.sh/?q={domainName}&output=json",
      "use_api": "True", "api_key": "None" }
  ],
  "IPFinder": [],
  "IPAnalyser": [
    { "api_name": "https://internetdb.shodan.io/{ip}",
      "use_api": "True", "api_key": "None" }
  ]
}
```

- `use_api` — set to `"False"` to disable a source.
- `api_key` — set to `"None"` for keyless APIs. Key-based providers are stubbed out and can be implemented in the respective modules.

## Project Structure

| File | Purpose |
|------|---------|
| `main.py` | Entry point and orchestration |
| `subdomainFinder.py` | Enumerates subdomains for a domain |
| `IPFinder.py` | Resolves subdomains to IP addresses |
| `IPAnalyser.py` | Queries host intelligence and CVE data |
| `config.json` | API configuration |

## Disclaimer

This tool is intended for **authorized security testing and educational purposes only**. Only scan domains and hosts you own or have explicit permission to test. The authors are not responsible for any misuse.

## License

Released under the [MIT License](LICENSE).
