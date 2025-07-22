import pandas as pd
import os


def load_cmdb_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"[ERROR] Datei nicht gefunden: {file_path}")

    df = pd.read_csv(file_path)
    if df.empty:
        raise ValueError(f"[ERROR] Datei ist leer: {file_path}")

    print(f"[INFO] {len(df)} Zeilen geladen aus: {file_path}")
    return df
