import streamlit as st
import requests

# ⚠️ INSERISCI QUI LA TUA EMAIL PROFESSIONALE
IL_TUO_INDIRIZZO_EMAIL = "sicurezza@sigismondicostruzioni.com" 

# Configurazione della pagina
st.set_page_config(page_title="Consulenza Edile Smart", page_icon="🏗️")

st.title("🏗️ Portale Sicurezza Cantiere")
st.write("Inserisci i dati per richiedere la redazione del documento.")

tab_pos, tab_pimus = st.tabs(["📋 Sezione POS", "🪜 Sezione PiMUS"])

# Funzione per inviare i dati via email usando FormSubmit
def invia_dati_email(tipo_documento, dati_dizionario):
    # FormSubmit invia i dati alla tua mail in automatico
    url_servizio = f"https://formsubmit.co/{IL_TUO_INDIRIZZO_EMAIL}"
    
    # Prepariamo il testo dell'email
    corpo_mail = {
        "_subject": f"🆕 Nuova richiesta {tipo_documento} da App Cantieri",
        "Tipo Documento": tipo_documento
    }
    corpo_mail.update(dati_dizionario)
    
    # Invio della richiesta
    risposta = requests.post(url_servizio, data=corpo_mail)
    return risposta.status_code == 200

# ------------------- SCHERMATA POS -------------------
with tab_pos:
    st.header("Richiesta POS")
    cantiere_ref = st.text_input("Cantiere di Riferimento (es. Via Roma 12)", key="pos_cant")
    dati_committente = st.text_area("Dati del Committente / Impresa Affidataria", key="pos_comm")
    oggetto_lavori = st.text_input("Oggetto delle Lavorazioni", key="pos_ogg")
    note_lavorazioni = st.text_area("Descrizione o note aggiuntive", key="pos_note")
    
    # Nota sulle foto per questa versione semplificata
    st.info("💡 Per questa versione beta, invia le foto direttamente su WhatsApp indicando il nome del cantiere.")
    
    if st.button("Invia Dati POS al Tecnico"):
        if cantiere_ref and oggetto_lavori:
            dati_da_inviare = {
                "Cantiere": cantiere_ref,
                "Committente": dati_committente,
                "Oggetto Lavori": oggetto_lavori,
                "Note": note_lavorazioni
            }
            with st.spinner("Invio in corso..."):
                if invia_dati_email("POS", dati_da_inviare):
                    st.success(f"✔️ Dati inviati! Controlla la tua email '{IL_TUO_INDIRIZZO_EMAIL}'.")
                else:
                    st.error("❌ Errore nell'invio dei dati. Riprova.")
        else:
            st.warning("Compila i campi obbligatori (Cantiere e Oggetto).")

# ------------------- SCHERMATA PiMUS -------------------
with tab_pimus:
    st.header("Richiesta PiMUS")
    cantiere_pimus = st.text_input("Cantiere di Riferimento Ponteggio", key="pimus_cant")
    allestimento_per = st.text_input("Allestimento per...", key="pimus_all")
    tipo_ponteggio = st.selectbox("Tipo di Ponteggio", ["Telai Prefabbricati", "Tubi e Giunti", "Multidirezionale"], key="pimus_tipo")
    altezza_max = st.text_input("Altezza massima (metri)", key="pimus_alt")
    note_pimus = st.text_area("Note aggiuntive", key="pimus_note")
    
    if st.button("Invia Dati PiMUS al Tecnico"):
        if cantiere_pimus and allestimento_per:
            dati_da_inviare = {
                "Cantiere Ponteggio": cantiere_pimus,
                "Allestimento Per": allestimento_per,
                "Tipo Ponteggio": tipo_ponteggio,
                "Altezza": altezza_max,
                "Note": note_pimus
            }
            with st.spinner("Invio in corso..."):
                if invia_dati_email("PiMUS", dati_da_inviare):
                    st.success(f"✔️ Dati inviati! Controlla la tua email '{IL_TUO_INDIRIZZO_EMAIL}'.")
                else:
                    st.error("❌ Errore nell'invio dei dati. Riprova.")
        else:
            st.warning("Compila i campi obbligatori (Cantiere e Allestimento).")