import os
import segno
import uuid

def simpleQr(content: str, filename: str = "myQr", scale: int = 10):
    """
    Génère un QR code simple et l'enregistre dans 'qrs/'.
    """
    output_dir = "qrs"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    qr = segno.make_qr(content)
    qr.save(os.path.join(output_dir, f"{filename}.png"), scale=scale)


def artisticQr(content: str, source: str, filename: str = "myQr", scale: int = 8):
    """
    Génère un QR code artistique en superposant le code sur une image de fond.
    """
    output_dir = "qrs"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    qr = segno.make_qr(content)
    target_path = os.path.join(output_dir, f"{filename}.png")

    qr.to_artistic(
        background=source,
        target=target_path,
        scale=scale,
    )


def save_uploaded_image(uploaded_file, upload_dir="uploads"):
    """
    Sauvegarde une image uploadée dans un répertoire local.
    
    Paramètres :
        uploaded_file (UploadedFile) : Le fichier image uploadé
        upload_dir (str) : Répertoire de destination

    Retour :
        str : Chemin absolu du fichier sauvegardé
    """
    # S'assurer que le répertoire existe
    os.makedirs(upload_dir, exist_ok=True)

    # Générer un nom de fichier unique pour éviter les collisions
    ext = os.path.splitext(uploaded_file.name)[1]  # e.g. ".jpg"
    unique_name = f"{uuid.uuid4()}{ext}"

    save_path = os.path.join(upload_dir, unique_name)

    # Sauvegarder le fichier
    with open(save_path, "wb") as f:
        for chunk in uploaded_file.chunks() if hasattr(uploaded_file, "chunks") else [uploaded_file.read()]:
            f.write(chunk)

    return save_path




