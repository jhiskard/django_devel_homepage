from xml.etree.ElementTree import parse

tree = parse("siesta.xml")
note = tree.getroot()
parameterList = note.find("metadataList")

for child in parameterList:
    print child.attrib
