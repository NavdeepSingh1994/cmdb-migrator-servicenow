# CMDB Migrator for ServiceNow (CSDM-ready)

Ein Python-Tool zur Migration, Validierung und Integration von CMDB-Daten nach ServiceNow unter Einhaltung des CSDM-Modells.

## Features
- CSV-Import aus i-doit oder anderen CMDBs
- Mapping nach CSDM (Business Applications, Services, Hosts etc.)
- REST API Push zu ServiceNow
- Datenvalidierung & Bericht
- Konfigurierbar per YAML

## Setup
```bash
git clone https://github.com/NavdeepSingh1994/cmdb-migrator-servicenow
cd cmdb-migrator-servicenow
pip install -r requirements.txt
