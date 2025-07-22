# src/csdm_mapper.py

def map_to_csdm(df):
    """
    Mappt CMDB-Einträge auf ServiceNow-Tabellen gemäß CSDM.
    Fügt eine neue Spalte 'target_table' hinzu.
    """

    csdm_mapping = {
        "BusinessApplication": "cmdb_ci_business_app",
        "ApplicationService": "cmdb_ci_appl",
        "Server": "cmdb_ci_server",
        "Database": "cmdb_ci_database",
        "NetworkDevice": "cmdb_ci_network",
        "StorageDevice": "cmdb_ci_storage_device",
        # Weitere Typen hier ergänzen …
    }

    df["target_table"] = df["Type"].map(csdm_mapping).fillna("unknown")
    return df
