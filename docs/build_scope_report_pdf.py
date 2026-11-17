from html import escape
from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


BASE = Path(__file__).resolve().parent
SOURCE = BASE / "scope_report.md"
OUTPUT = BASE / "scope_report.pdf"

NAVY = colors.HexColor("#173B57")
TEAL = colors.HexColor("#176B78")
INK = colors.HexColor("#243447")
MUTED = colors.HexColor("#596B78")
PALE = colors.HexColor("#EFF4F7")
PALE_GREEN = colors.HexColor("#EAF4F3")
PALE_SAND = colors.HexColor("#F5F1EC")


def inline_markup(text: str) -> str:
    text = escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", text)
    return text


def make_styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle("ReportTitle", parent=base["Title"], fontName="Helvetica-Bold", fontSize=21, leading=24, textColor=NAVY, alignment=TA_LEFT, spaceAfter=2),
        "meta": ParagraphStyle("Meta", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=8.3, leading=10, textColor=MUTED, spaceAfter=2),
        "heading": ParagraphStyle("SectionHeading", parent=base["Heading2"], fontName="Helvetica-Bold", fontSize=10.2, leading=12, textColor=TEAL, spaceBefore=4.5, spaceAfter=1.4, keepWithNext=True),
        "body": ParagraphStyle("Body", parent=base["BodyText"], fontName="Helvetica", fontSize=8.5, leading=10.4, textColor=INK, spaceAfter=2.6, alignment=TA_LEFT),
        "list": ParagraphStyle("List", parent=base["BodyText"], fontName="Helvetica", fontSize=8.2, leading=9.6, textColor=INK, leftIndent=10, firstLineIndent=-7, spaceAfter=1.2),
        "table": ParagraphStyle("TableText", parent=base["BodyText"], fontName="Helvetica", fontSize=7.7, leading=9.0, textColor=INK, spaceAfter=0),
        "table_head": ParagraphStyle("TableHead", parent=base["BodyText"], fontName="Helvetica-Bold", fontSize=7.7, leading=9.0, textColor=colors.white, spaceAfter=0),
    }


def markdown_rows(lines, start):
    rows = []
    index = start
    while index < len(lines) and lines[index].strip().startswith("|"):
        cells = [cell.strip() for cell in lines[index].strip().strip("|").split("|")]
        if not all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells):
            rows.append(cells)
        index += 1
    return rows, index


def on_page(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#D8E2E8"))
    canvas.setLineWidth(0.5)
    canvas.line(doc.leftMargin, 22, A4[0] - doc.rightMargin, 22)
    canvas.setFont("Helvetica", 7.2)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 11, "CSE431 Topic and Problem Scope | Group 05")
    canvas.drawRightString(A4[0] - doc.rightMargin, 11, f"Page {doc.page}")
    canvas.restoreState()


def main():
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    styles = make_styles()
    story = []
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        if not line:
            index += 1
            continue
        if line.startswith("# "):
            story.append(Paragraph(inline_markup(line[2:]), styles["title"]))
            story.append(Spacer(1, 2))
        elif line.startswith("## "):
            story.append(Paragraph(inline_markup(line[3:]), styles["heading"]))
        elif line.startswith("|"):
            rows, index = markdown_rows(lines, index)
            if rows:
                converted = []
                for row_index, row in enumerate(rows):
                    style = styles["table_head"] if row_index == 0 else styles["table"]
                    converted.append([Paragraph(inline_markup(cell), style) for cell in row])
                column_count = len(rows[0])
                widths = [ (A4[0] - 84*mm) / column_count ] * column_count
                table = Table(converted, colWidths=widths, hAlign="LEFT", repeatRows=1)
                table.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                    ("BACKGROUND", (0, 1), (-1, -1), PALE),
                    ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#C7D4DC")),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 5),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                    ("TOPPADDING", (0, 0), (-1, -1), 3),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ]))
                story.append(table)
                story.append(Spacer(1, 2))
            continue
        elif re.match(r"\d+\. ", line):
            item = re.sub(r"^\d+\. ", "", line)
            story.append(Paragraph("&#8226; " + inline_markup(item), styles["list"]))
        elif line.startswith("**Included:**") or line.startswith("**Excluded:**"):
            story.append(Paragraph(inline_markup(line), styles["body"]))
        else:
            story.append(Paragraph(inline_markup(line), styles["meta"] if line.startswith("**Course:**") or line.startswith("**Group:**") or line.startswith("**Industry domain:**") or line.startswith("**Milestone due:**") else styles["body"]))
        index += 1

    document = SimpleDocTemplate(
        str(OUTPUT), pagesize=A4,
        rightMargin=42*mm, leftMargin=42*mm,
        topMargin=13*mm, bottomMargin=16*mm,
        title="BreastWise Project Scope",
        author="Group 05",
        subject="CSE431 Topic and Problem Scope",
    )
    document.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(OUTPUT)


if __name__ == "__main__":
    main()
