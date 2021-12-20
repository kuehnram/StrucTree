from lxml import etree

from model import Entry


def build_model(file_name: str) -> Entry:
    entry = Entry(file_name)
    with open(file_name, "r", encoding="utf-8") as f:
        xml_tree = etree.parse(f)
    entry.children.append(convert_xml(xml_tree.getroot()))

    return entry


def convert_xml(node) -> Entry:
    entry = Entry(node.tag)
    for child in node:
        entry.children.append(convert_xml(child))
    return entry


