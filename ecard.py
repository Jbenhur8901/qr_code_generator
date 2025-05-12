import vobject 
import base64
import mimetypes
import os


def create_vcard(**kwargs):
    """
    Génère une vCard à partir des champs fournis.

    Gère automatiquement les types de téléphone : 
    - 'tel_cell' → CELL
    - 'tel_work' → WORK
    - 'tel_home' → HOME

    Tous les autres champs sont ajoutés tels quels (ex. : 'fn', 'email', 'org').

    Paramètres :
        **kwargs : dict — Paires clé-valeur des attributs de la vCard.

    Retour :
        str — vCard au format texte.
    """

    vcard = vobject.vCard()
    tel_fields = {
        "tel_cell": "CELL",
        "tel_work": "WORK",
        "tel_home": "HOME"
    }

    for key, value in kwargs.items():

        if not value :
            continue

        if key in tel_fields:
            tel = vcard.add("tel")
            tel.value = value
            tel.type_param = tel_fields[key]
        
        else : 
            vcard.add(key).value = kwargs.get(key)
        
    vcard_string = vcard.serialize()
    return vcard_string





# def create_vcard_2(**kwargs):
#     """
#     Génère une vCard à partir des champs fournis, y compris la prise en charge du champ PHOTO.

#     Paramètres :
#         kwargs : dictionnaire de champs. 
#             Exemples : fn, email, org, tel_cell, photo_url, photo_file

#     Retour :
#         str — vCard au format texte.
#     """

#     vcard = vobject.vCard()
#     tel_fields = {
#         "tel_cell": "CELL",
#         "tel_work": "WORK",
#         "tel_home": "HOME"
#     }

#     for key, value in kwargs.items():
#         if not value:
#             continue

#         if key in tel_fields:
#             tel = vcard.add("tel")
#             tel.value = value
#             tel.type_param = tel_fields[key]

#         elif key == "photo_url":
#             photo = vcard.add("photo")
#             photo.value = value
#             photo.type_param = "JPEG"
#             photo.encoding_param = "URI"

#         elif key == "photo_file":
#             # Lire les données depuis un fichier téléchargé (UploadedFile)
#             encoded_data = base64.b64encode(value.read()).decode("utf-8")
    
#             photo = vcard.add("photo")
#             photo.value = encoded_data
#             photo.encoding_param = "b"

#             mime_type = value.
#             ext = mimetypes.guess_extension(mime_type).replace('.', '').upper()
#             photo.type_param = ext

#         else:
#             vcard.add(key).value = value

#     return vcard.serialize()


