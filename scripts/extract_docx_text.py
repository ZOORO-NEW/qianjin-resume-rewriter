"""Extract plain text from a .docx file (paragraphs + tables), no external deps.

Usage:
    python extract_docx_text.py <path-to-docx>

Prints each paragraph/table-row text on its own line, in document order.
Works offline; useful when the live editor SDK cannot read the file.
"""
import sys
import zipfile
import re
from xml.etree import ElementTree as ET

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def para_text(p):
    parts = []
    for t in p.iter(f"{{{NS['w']}}}t"):
        parts.append(t.text or "")
    return "".join(parts).strip()


def main(path):
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml")
    root = ET.fromstring(xml)
    body = root.find("w:body", NS)
    for el in body:
        tag = el.tag.split("}")[-1]
        if tag == "p":
            text = para_text(el)
            if text:
                print(text)
        elif tag == "tbl":
            for row in el.findall("w:tr", NS):
                cells = []
                for tc in row.findall("w:tc", NS):
                    cell = " ".join(
                        filter(None, (para_text(p) for p in tc.findall("w:p", NS)))
                    )
                    cells.append(cell)
                line = " | ".join(cells).strip(" |")
                if line:
                    print(line)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    main(sys.argv[1])
