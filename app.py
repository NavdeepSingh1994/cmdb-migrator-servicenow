import streamlit as st
import pandas as pd
from src.cmdb_loader import load_cmdb_data
from src.csdm_mapper import map_to_csdm
from src.validator import validate_data
from src.servicenow_api import push_to_servicenow
from src.pdf_generator import create_pdf_report
from src.mailer import send_email_with_pdf
from pathlib import Path

st.set_page_config(page_title="CMDB Migrator", layout="wide")
st.title("🛠️ CMDB Migrations-Tool")

uploaded_file = st.file_uploader("📤 Lade deine CMDB-Datei hoch (.csv)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df = map_to_csdm(df)
    errors = validate_data(df)

    st.subheader("📋 Vorschau der CMDB-Daten:")
    st.dataframe(df)

    if errors:
        st.warning("❗ Validierungsfehler:")
        for e in errors:
            st.text(e)
    else:
        st.success("✅ Daten sind vollständig und valide.")

        if st.button("🚀 Daten an ServiceNow senden"):
            push_to_servicenow(df)
            st.success("✅ Alle Einträge wurden erfolgreich übertragen.")

        pdf_path = create_pdf_report(df)
        st.download_button("📄 PDF herunterladen", open(pdf_path, "rb"), file_name="cmdb_report.pdf")

        email = st.text_input("✉️ E-Mail für Versand", key="email_input")
        if st.button("📬 PDF per E-Mail versenden"):
            if email:
                success = send_email_with_pdf(email, pdf_path)
                if success:
                    st.success(f"✅ E-Mail an {email} wurde erfolgreich versendet.")
                else:
                    st.error("❌ Fehler beim Senden der E-Mail. Bitte überprüfe die Konsole oder .env-Datei.")
            else:
                st.warning("⚠️ Bitte gib eine gültige E-Mail-Adresse ein.")
