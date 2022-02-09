#!/usr/local/bin/python3

"""Convert a BrickOwl parts CSV to a BrickLink XML that can be imported into
BickLink Studio

BrickOwl CSV format

"Order Id",Name,Type,"Color Name",Boid,"Lot Id",Condition,"Ordered Quantity","Public Note","Base Price"
3351561,"LEGO Medium Stone Gray Axle 7 (44294)",Part,"Medium Stone Gray",29003-64,71762615,New,2,,0.053
3351561,"LEGO Dark Stone Gray Angle Connector #2 (180º) (32034 / 42134)",Part,"Dark Stone Gray",589908-50,33583825,New,4,,0.239


BrickLink XML format (https://www.bricklink.com/help.asp?helpID=207)

<INVENTORY>
  <ITEM>
    <ITEMTYPE>P</ITEMTYPE>
    <ITEMID>3622</ITEMID>
    <COLOR>11</COLOR>
    <QTYFILLED>4</QTYFILLED>
  </ITEM>
  <ITEM>
    <ITEMTYPE>P</ITEMTYPE>
    <ITEMID>3039</ITEMID>
  </ITEM>
  <ITEM>
    <ITEMTYPE>P</ITEMTYPE>
    <ITEMID>3001</ITEMID>
    <COLOR>5</COLOR>
    <MAXPRICE>1.00</MAXPRICE>
    <MINQTY>100</MINQTY>
    <CONDITION>N</CONDITION>
    <REMARKS>for MOC AB154A</REMARKS>
    <NOTIFY>N</NOTIFY>
  </ITEM>
</INVENTORY>
"""

from dataclasses import dataclass
import sys
from pathlib import Path
import csv
import re
import this

part_regexp = re.compile(r"\((.*?)\)")


@dataclass
class Part:
    part_no: str
    qty: int

    def as_brick_link(self):
        return f"<ITEM><ITEMTYPE>P</ITEMTYPE><ITEMID>{self.part_no}</ITEMID><QTYFILLED>{self.qty}</QTYFILLED></ITEM>\n"


def main(infile: Path, outfile: Path):
    brick_link_catalog = load_brick_link_catalog()

    parts = {}
    with open(infile) as brick_owl_csv:
        reader = csv.DictReader(brick_owl_csv)
        for row in reader:
            this_part = parse_part(row, brick_link_catalog)
            if this_part.part_no not in parts:
                parts[this_part.part_no] = this_part
            else:
                parts[this_part.part_no].qty += this_part.qty

    with outfile.open("w") as studio_xml:
        studio_xml.write("<INVENTORY>\n")
        studio_xml.writelines(part.as_brick_link() for part in parts.values())
        studio_xml.write("</INVENTORY>\n")


def load_brick_link_catalog() -> set:
    with open("bricklink-catalog.tsv") as catalog_csv:
        reader = csv.DictReader(catalog_csv, delimiter="\t")
        return set(row["Number"].strip() for row in reader)


def parse_part(row: dict, catalog: set) -> Part:
    part_nos = part_regexp.findall(row["Name"])[-1].split("/")
    part_no = alt_part_no = part_nos[0].strip()
    if len(part_nos) == 2:
        alt_part_no = part_nos[1].strip()
    if part_no not in catalog:
        part_no = alt_part_no

    qty = int(row["Ordered Quantity"])
    return Part(part_no, qty)


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
