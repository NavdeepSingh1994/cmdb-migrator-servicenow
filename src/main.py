from cmdb_loader import load_cmdb_data
from csdm_mapper import map_to_csdm
from validator import validate_data
from servicenow_api import push_to_servicenow

def main():
    # 1. CSV laden
    df = load_cmdb_data("../data/cmdb_sample.csv")

    # 2. Mapping (CSDM Type → SNOW Table)
    df = map_to_csdm(df)

    # 3. Anzeige
    print("\n📋 Gemappte CMDB-Daten:")
    print(df.to_markdown(index=False))

    # 4. Validierung
    print("\n🔎 Validierungsbericht:")
    errors = validate_data(df)
    if errors:
        for e in errors:
            print(e)
        print("❌ Daten fehlerhaft. Kein API-Push erfolgt.")
        return
    else:
        print("✅ Alle Daten sind vollständig und gültig.")

    # 5. Push zu ServiceNow
    print("\n📡 Übertrage Daten an ServiceNow:")
    push_to_servicenow(df)

if __name__ == "__main__":
    main()
