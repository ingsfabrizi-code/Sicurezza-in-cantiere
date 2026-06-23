import streamlit as st
from datetime import datetime

# Configurazione della pagina per smartphone
st.set_page_config(page_title="Consulenza Edile Smart", page_icon="🏗️", layout="centered")

st.title("🏗️ Portale Sicurezza Cantiere")
st.write("Benvenuto! Seleziona il documento che desideri compilare oggi.")

# Creazione dei due macro-pulsanti (Tab)
tab_pos, tab_pimus = st.tabs(["📋 Sezione POS", "🪜 Sezione PiMUS"])

# ------------------- SCHERMATA POS -------------------
with tab_pos:
    st.header("Compilazione Dati per POS")
    st.subheader("(Piano Operativo di Sicurezza)")
    
    with st.form("form_pos", clear_on_submit=True):
        cantiere_ref = st.text_input("Cantiere di Riferimento (es. Via Roma 12)")
        dati_committente = st.text_area("Dati del Committente / Impresa Affidataria")
        oggetto_lavori = st.text_input("Oggetto delle Lavorazioni (es. Rifacimento tetto)")
        
        st.divider()
        st.subheader("📸 Foto e Dettagli delle Lavorazioni")
        foto_lavorazioni = st.file_uploader("Carica le foto del cantiere/lavorazioni", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
        note_lavorazioni = st.text_area("Descrizione dettagliata delle lavorazioni da eseguire")
        
        # Pulsante di invio
        submit_pos = st.form_submit_button("Invia Dati POS al Tecnico")
        
        if submit_pos:
            if cantiere_ref and oggetto_lavori:
                st.success(f"✔️ Dati per il cantiere '{cantiere_ref}' inviati con successo! Il tecnico si metterà al lavoro.")
                # Qui in futuro collegheremo il salvataggio su database o l'invio via email
            else:
                st.error("❌ Per favore, compila almeno i campi obbligatori (Cantiere e Oggetto).")

# ------------------- SCHERMATA PiMUS -------------------
with tab_pimus:
    st.header("Compilazione Dati per PiMUS")
    st.subheader("(Piano di Montaggio, Uso e Smontaggio Ponteggi)")
    
    with st.form("form_pimus", clear_on_submit=True):
        cantiere_pimus = st.text_input("Cantiere di Riferimento Ponteggio")
        allestimento_per = st.text_input("Allestimento per (es. Intonacatura facciata, Isolamento a cappotto)")
        
        st.divider()
        st.subheader("📐 Dimensioni e Caratteristiche del Ponteggio")
        tipo_ponteggio = st.selectbox("Tipo di Ponteggio", ["Telai Prefabbricati", "Tubi e Giunti", "Montanti Prefabbricati (Multidirezionale)"])
        altezza_max = st.number_input("Altezza massima del ponteggio (in metri)", min_value=0.0, step=0.5)
        lunghezza_max = st.number_input("Sviluppo lineare/Lunghezza (in metri)", min_value=0.0, step=0.5)
        
        st.divider()
        st.subheader("📸 Foto Area di Installazione")
        foto_pimus = st.file_uploader("Carica foto della base d'appoggio o dello stato dei luoghi", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
        note_pimus = st.text_area("Note aggiuntive (es. presenza di linee elettriche aeree, vincoli di spazio)")
        
        # Pulsante di invio
        submit_pimus = st.form_submit_button("Invia Dati PiMUS al Tecnico")
        
        if submit_pimus:
            if cantiere_pimus and allestimento_per:
                st.success(f"✔️ Dati PiMUS per il cantiere '{cantiere_pimus}' ricevuti correttamente!")
                # Qui in futuro collegheremo l'automazione
            else:
                st.error("❌ Per favore, inserisci il cantiere e il motivo dell'allestimento.")