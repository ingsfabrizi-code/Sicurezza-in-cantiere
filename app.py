import streamlit as st

# Inserisci la tua Gmail per il test
IL_TUO_INDIRIZZO_EMAIL = "ing.s.fabrizi@gmail.com"

# Configurazione della pagina
st.set_page_config(page_title="Consulenza Edile Smart", page_icon="🏗️")

st.title("🏗️ Portale Sicurezza Cantiere")
st.write("Inserisci i dati per richiedere la redazione del documento.")

tab_pos, tab_pimus = st.tabs(["📋 Sezione POS", "🪜 Sezione PiMUS"])

# ------------------- SCHERMATA POS -------------------
with tab_pos:
    st.header("Richiesta POS")
    cantiere_ref = st.text_input("Cantiere di Riferimento (es. Via Roma 12)", key="pos_cant")
    dati_committente = st.text_area("Dati del Committente / Impresa Affidataria", key="pos_comm")
    oggetto_lavori = st.text_input("Oggetto delle Lavorazioni", key="pos_ogg")
    note_lavorazioni = st.text_area("Descrizione o note aggiuntive", key="pos_note")
    
    st.info("💡 Compila i dati e premi il pulsante sotto per inviare la richiesta.")
    
    if cantiere_ref and oggetto_lavori:
        # Questo crea un modulo web sicuro che si apre al clic
        form_url = f"https://formsubmit.co/{IL_TUO_INDIRIZZO_EMAIL}"
        
        with st.form("form_pos", clear_on_submit=True):
            st.write("### Conferma i dati prima di inviare:")
            st.write(f"**Cantiere:** {cantiere_ref}")
            st.write(f"**Oggetto:** {oggetto_lavori}")
            
            # Campi nascosti che FormSubmit leggerà in automatico
            st.markdown(f'<input type="hidden" name="Cantiere" value="{cantiere_ref}">', unsafe_allow_html=True)
            st.markdown(f'<input type="hidden" name="Committente" value="{dati_committente}">', unsafe_allow_html=True)
            st.markdown(f'<input type="hidden" name="Oggetto Lavori" value="{oggetto_lavori}">', unsafe_allow_html=True)
            st.markdown(f'<input type="hidden" name="Note" value="{note_lavorazioni}">', unsafe_allow_html=True)
            
            # Pulsante nativo HTML che forza l'invio bypassando i blocchi del server
            submit_html = f'''
                <form action="{form_url}" method="POST" target="_blank">
                    <input type="hidden" name="Cantiere" value="{cantiere_ref}">
                    <input type="hidden" name="Committente" value="{dati_committente}">
                    <input type="hidden" name="Oggetto Lavori" value="{oggetto_lavori}">
                    <input type="hidden" name="Note" value="{note_lavorazioni}">
                    <input type="hidden" name="_subject" value="🆕 Nuova richiesta POS">
                    <button type="submit" style="background-color: #FF4B4B; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-weight: bold; width: 100%;">
                        INVIA RICHIESTA POS ORA
                    </button>
                </form>
            '''
            st.components.v1.html(submit_html, height=50)
    else:
        st.warning("Inserisci almeno il Cantiere e l'Oggetto delle lavorazioni per sbloccare il pulsante di invio.")

# ------------------- SCHERMATA PiMUS -------------------
with tab_pimus:
    st.header("Richiesta PiMUS")
    cantiere_pimus = st.text_input("Cantiere di Riferimento Ponteggio", key="pimus_cant")
    allestimento_per = st.text_input("Allestimento per...", key="pimus_all")
    tipo_ponteggio = st.selectbox("Tipo di Ponteggio", ["Telai Prefabbricati", "Tubi e Giunti", "Multidirezionale"], key="pimus_tipo")
    altezza_max = st.text_input("Altezza massima (metri)", key="pimus_alt")
    note_pimus = st.text_area("Note aggiuntive", key="pimus_note")
    
    if cantiere_pimus and allestimento_per:
        form_url = f"https://formsubmit.co/{IL_TUO_INDIRIZZO_EMAIL}"
        
        with st.form("form_pimus", clear_on_submit=True):
            st.write("### Conferma i dati prima di inviare:")
            st.write(f"**Cantiere Ponteggio:** {cantiere_pimus}")
            
            submit_html_pimus = f'''
                <form action="{form_url}" method="POST" target="_blank">
                    <input type="hidden" name="Cantiere Ponteggio" value="{cantiere_pimus}">
                    <input type="hidden" name="Allestimento Per" value="{allestimento_per}">
                    <input type="hidden" name="Tipo Ponteggio" value="{tipo_ponteggio}">
                    <input type="hidden" name="Altezza" value="{altezza_max}">
                    <input type="hidden" name="Note" value="{note_pimus}">
                    <input type="hidden" name="_subject" value="🆕 Nuova richiesta PiMUS">
                    <button type="submit" style="background-color: #FF4B4B; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-weight: bold; width: 100%;">
                        INVIA RICHIESTA PiMUS ORA
                    </button>
                </form>
            '''
            st.components.v1.html(submit_html_pimus, height=50)
    else:
        st.warning("Inserisci almeno il Cantiere e l'Allestimento per sbloccare il pulsante di invio.")
