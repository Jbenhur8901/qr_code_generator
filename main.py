import streamlit as st
from ecard import create_vcard
from tools import *

with st.sidebar : 
    st.title("Options")

with st.form(key="my_form") :
    st.title("Form")
    st.write("This is the form content.")

    col = st.columns(2)
    with col[0] :
        name = st.text_input("Nom de famille")
        title = st.text_input("Fonction")
        tel_cell = st.text_input("Téléphone 1 (Portable)")
        mail = st.text_input("Adresse Mail")
        logo =st.file_uploader("Logo sur le QR", type=["jpg", "jpeg", "png"])
    
    with col[1] :
        first_name = st.text_input("Prénom(s)")
        org = st.text_input("Organisation")
        tel_work = st.text_input("Téléphone 2 (Bureau)")
        url = st.text_input("Site Web")
        filename = st.text_input("Nom du Fichier")
    
    note = st.text_area("Note")

    flag = st.form_submit_button()
    if flag : 
        
        fullname = name + " " + first_name

        vcard_string = create_vcard(
            fn=fullname,
            title=title,
            tel_cell=tel_cell,
            email=mail,
            tel_work=tel_work,
            url=url,
            note=note,
        )
        if logo is not None : 
            path = save_uploaded_image(logo)
            artisticQr(vcard_string, path, filename=filename)

if flag :
    st.image(f"qrs/{filename}.png", caption="QR Code")


