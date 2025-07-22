# src/validator.py

def validate_data(df, required_fields=None):
    """
    Prüft, ob alle erforderlichen Felder vorhanden und ausgefüllt sind.
    Gibt eine Liste von Fehlern zurück.
    """
    if required_fields is None:
        required_fields = ["Name", "Type", "Owner", "Environment", "target_table"]

    errors = []

    for field in required_fields:
        if field not in df.columns:
            errors.append(f"[ERROR] Spalte fehlt: {field}")
        else:
            missing = df[df[field].isnull() | (df[field].astype(str).str.strip() == "")]
            if not missing.empty:
                for i in missing.index:
                    errors.append(f"[ERROR] Leeres Feld '{field}' in Zeile {i + 1}: {missing.loc[i].to_dict()}")

    if "target_table" in df.columns:
        unknown = df[df["target_table"] == "unknown"]
        for i in unknown.index:
            errors.append(f"[WARNING] Unbekannter Type → target_table='unknown' in Zeile {i + 1}: {df.loc[i].to_dict()}")

    return errors
