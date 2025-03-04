import xml.etree.ElementTree as ET
tree = ET.parse("truc.xml")

print(tree)

root = tree.getroot()
print(root.text)