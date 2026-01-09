from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from datetime import datetime

def generate_pdf(filename, pegawai, nip, jabatan, unit, data):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # HEADER
    elements.append(Paragraph(
        "<b>PEMERINTAH DAERAH</b><br/>"
        "<b>RUMAH SAKIT UMUM DAERAH</b><br/>"
        "<b>INSTALASI TEKNOLOGI INFORMASI</b><br/><br/>",
        styles["Title"]
    ))

    elements.append(Paragraph(
        "<b>LAPORAN KEGIATAN HARIAN IT SUPPORT</b><br/>"
        "(Bahan Pengisian e-Kinerja ASN)<br/><br/>",
        styles["Heading2"]
    ))

    # IDENTITAS
    elements.append(Paragraph(
        f"""
        Nama Pegawai : {pegawai}<br/>
        NIP : {nip}<br/>
        Jabatan : {jabatan}<br/>
        Unit Kerja : {unit}<br/>
        Bulan/Tahun : {datetime.now().strftime('%B %Y')}<br/><br/>
        """,
        styles["Normal"]
    ))

    # TABEL KEGIATAN
    table_data = [["No", "Tanggal", "Uraian Kegiatan", "Angka Kredit"]]

    for i, d in enumerate(data, start=1):
        table_data.append([
            i,
            d["tanggal"],
            d["narasi"],
            f"{d['angka']:.2f}"
        ])

    table = Table(table_data, colWidths=[30, 70, 300, 80])
    table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 30))

    # TTD
    elements.append(Paragraph(
        f"""
        <br/>
        Mengetahui,<br/>
        Atasan Langsung<br/><br/><br/><br/>
        _______________________<br/><br/>

        {datetime.now().strftime('%d %B %Y')}<br/>
        Pegawai Yang Bersangkutan<br/><br/><br/><br/>
        <b>{pegawai}</b>
        """,
        styles["Normal"]
    ))

    doc.build(elements)
