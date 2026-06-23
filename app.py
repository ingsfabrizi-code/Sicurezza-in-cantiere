import streamlit as st

# ✉️ Inserisci qui l'email finale (Aziendale o Gmail)
IL_TUO_INDIRIZZO_EMAIL = "ing.s.fabrizi@gmail.com"

# Configurazione della pagina
st.set_page_config(page_title="Consulenza Edile Smart", page_icon="🏗️")

st.title("🏗️ Portale Sicurezza Cantiere")
st.write("Inserisci i dati e allega i file per richiedere il documento.")

tab_pos, tab_pimus = st.tabs(["📋 Sezione POS", "🪜 Sezione PiMUS"])

# ------------------- SCHERMATA POS -------------------
with tab_pos:
    st.header("Richiesta POS")
    cantiere_ref = st.text_input("Cantiere di Riferimento (es. Via Roma 12)", key="pos_cant")
    dati_committente = st.text_area("Dati del Committente / Impresa Affidataria", key="pos_comm")
    oggetto_lavori = st.text_input("Oggetto delle Lavorazioni", key="pos_ogg")
    note_lavorazioni = st.text_area("Descrizione o note aggiuntive", key="pos_note")
    
    st.info("💡 Compila i campi e usa il modulo qui sotto per caricare la foto e inviare tutto al tecnico.")
    
    if cantiere_ref and oggetto_lavori:
        form_url = f"https://formsubmit.co/{IL_TUO_INDIRIZZO_EMAIL}"
        
        # Form HTML puro integrato per gestire testo + file contemporaneamente
        submit_html = f'''
            <form action="{form_url}" method="POST" enctype="multipart/form-data" target="_blank" style="font-family: sans-serif; background-color: #f0f2f6; padding: 15px; border-radius: 5px;">
                <input type="hidden" name="Cantiere" value="{cantiere_ref}">
                <input type="hidden" name="Committente" value="{dati_committente}">
                <input type="hidden" name="Oggetto Lavori" value="{oggetto_lavori}">
                <input type="hidden" name="Note" value="{note_lavorazioni}">
                <input type="hidden" name="_subject" value="🆕 Richiesta POS - {cantiere_ref}">
                
                <label style="font-weight: bold; display: block; margin-bottom: 8px; color: #31333F;">📸 Seleziona Foto Cantiere o Planimetria:</label>
                <input type="file" name="Foto_Cantiere" accept="image/*" style="margin-bottom: 15px; display: block;">
                
                <button type="submit" style="background-color: #FF4B4B; color: white; border: none; padding: 12px 20px; border-radius: 4px; cursor: pointer; font-weight: bold; width: 100%; font-size: 16px;">
                    INVIA RICHIESTA CON ALLEGATO 🚀
                </button>
            </form>
        '''
        st.components.v1.html(submit_html, height=130)
    else:
        st.warning("Inserisci almeno il Cantiere e l'Oggetto delle lavorazioni per sbloccare il modulo di invio.")

# ------------------- SCHERMATA PiMUS -------------------
with tab_pimus:
    st.header("Richiesta PiMUS")
    cantiere_pimus = st.text_input("Cantiere di Riferimento Ponteggio", key="pimus_cant")
    allestimento_per = st.text_input("Allestimento per...", key="pimus_all")
    tipo_ponteggio = st.selectbox("Tipo di Ponteggio", ["Telai Prefabbricati", "Tubi e Giunti", "Multidirezionale"], key="pimus_tipo")
    altezza_max = st.text_input("Altezza massima (metri)", key="pimus_alt")
    note_pimus = st.text_area("Note aggiuntive", key="pimus_note")
    
    st.info("💡 Compila i campi e usa il modulo qui sotto per caricare il disegno e inviare tutto al tecnico.")
    
    if cantiere_pimus and allestimento_per:
        form_url = f"https://formsubmit.co/{IL_TUO_INDIRIZZO_EMAIL}"
        
        submit_html_pimus = f'''
            <form action="{form_url}" method="POST" enctype="multipart/form-data" target="_blank" style="font-family: sans-serif; background-color: #f0f2f6; padding: 15px; border-radius: 5px;">
                <input type="hidden" name="Cantiere Ponteggio" value="{cantiere_pimus}">
                <input type="hidden" name="Allestimento Per" value="{allestimento_per}">
                <input type="hidden" name="Tipo Ponteggio" value="{tipo_ponteggio}">
                <input type="hidden" name="Altezza" value="{altezza_max}">
                <input type="hidden" name="Note" value="{note_pimus}">
                <input type="hidden" name="_subject" value="🆕 Richiesta PiMUS - {cantiere_pimus}">
                
                <label style="font-weight: bold; display: block; margin-bottom: 8px; color: #31333F;">📸 Seleziona Disegno o Foto Ponteggio:</label>
                <input type="file" name="Disegno_Ponteggio" accept="image/*" style="margin-bottom: 15px; display: block;">
                
                <button type="submit" style="background-color: #FF4B4B; color: white; border: none; padding: 12px 20px; border-radius: 4px; cursor: pointer; font-weight: bold; width: 100%; font-size: 16px;">
                    INVIA RICHIESTA CON ALLEGATO 🚀
                </button>
            </form>
        '''
        st.components.v1.html(submit_html_pimus, height=130)
    else:
        st.warning("Inserisci almeno il Cantiere e l'Allestimento per sbloccare il modulo di invio.")
