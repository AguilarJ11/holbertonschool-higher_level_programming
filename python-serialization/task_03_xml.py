#!/usr/bin/python3

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    
    root = ET.Element('data')
    
    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = value
        root.append(child)

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    