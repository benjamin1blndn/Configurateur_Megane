#!/usr/bin/env python3
"""Extrait les visuels de la brochure Renault MEGANE (janvier 2021) vers ./assets.
Usage : python extract_assets.py 2021_01.pdf   (nécessite poppler-utils : pdfimages)"""
import subprocess, sys, shutil, pathlib, tempfile
pdf = sys.argv[1]
MAP = {  # page: (dossier, [noms dans l'ordre d'extraction])
 30: ("colors", ["cuivre-solar","bleu-iron","blanc-glacier","rouge-flamme","blanc-nacre","bleu-cosmos"]),
 31: ("colors", ["gris-baltique","gris-titanium","noir-etoile","gris-highland"]),
 36: ("seats",  ["limited","carbone","mixte","alcantara","cuir"]),
 37: ("wheels", ["elliptik-16","hightek-18","magny-cours-18","limited-16","montlhery-17","allium-17","impulse-16"]),
}
for page,(folder,names) in MAP.items():
    tmp = pathlib.Path(tempfile.mkdtemp())
    subprocess.run(["pdfimages","-j","-f",str(page),"-l",str(page),pdf,str(tmp/"i")],check=True)
    files = sorted(tmp.glob("i-*.jpg"))
    out = pathlib.Path("assets")/folder; out.mkdir(parents=True,exist_ok=True)
    for f,n in zip(files,names): shutil.copy(f,out/f"{n}.jpg")
print("OK")
