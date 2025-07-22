import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv
from pathlib import Path

# 🔄 Lade Umgebungsvariablen aus .env
load_dotenv(dotenv_path=Path(__file__).parent.parent / '.env')

# 📥 ServiceNow-Zugangsdaten
SN_INSTANCE = os.getenv("SN_INSTANCE")
SN_USER = os.getenv("SN_USER")
SN_PASS = os.getenv("SN_PASS")

# 🔍 Debug: Prüfe ob ENV-Daten geladen wurden
if not SN_INSTANCE or not SN_USER or not SN_PASS:
    raise ValueError("❌ .env Datei nicht korrekt geladen oder unvollständig!")

print(f"[DEBUG] Verbinde mit: https://{SN_INSTANCE} als {SN_USER}")

def push_to_servicenow(df):
    """
    Sendet CMDB-Daten über REST API an ServiceNow.
    """
    for _, row in df.iterrows():
        url = f"https://{SN_INSTANCE}/api/now/table/{row['target_table']}"
        payload = {
            "name": row["Name"],
            "environment": row["Environment"]
        }

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        try:
            response = requests.post(
                url,
                auth=HTTPBasicAuth(SN_USER, SN_PASS),
                headers=headers,
                json=payload
            )

            if response.status_code in [200, 201]:
                sys_id = response.json()['result']['sys_id']
                print(f"[OK] {row['Name']} erstellt (sys_id: {sys_id})")
            elif response.status_code == 401:
                print(f"[AUTH FAIL] 401 Unauthorized – Bitte prüfe Benutzername/Passwort.")
                break
            else:
                print(f"[FAIL] {row['Name']} → {response.status_code}: {response.text}")

        except Exception as e:
            print(f"[EXCEPTION] Fehler bei {row['Name']}: {e}")
