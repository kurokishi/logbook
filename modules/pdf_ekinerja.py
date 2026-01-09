from reportlab.platypus import *
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_pdf(file, pegawai, nip, unit, data):
    doc = SimpleDocTemplate(file, pagesize=A4)
    styles = getSampleStyleSheet()
    el = []

    el.append(Paragraph(
        "<b>RSUD</b><br/>INSTALASI TI<br/><br/>"
        "<b>LAPORAN e-KINERJA IT SUPPORT</b><br/><br/>",
        styles["Title"]
    ))

    el.append(Paragraph(
        f"Nama: {pegawai}<br/>NIP: {nip}<br/>Unit: {unit}<br/><br/>",
        styles["Normal"]
    ))

    table = [["No","Tanggal","Uraian","Angka Kredit"]]
    for i,d in enumerate(data,1):
        table.append([i,d["tanggal"],d["narasi"],d["angka"]])

    t = Table(table,[30,70,280,80])
    t.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.black)
    ]))

    el.append(t)
    doc.build(el)
