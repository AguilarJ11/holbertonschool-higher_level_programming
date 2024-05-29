#!/usr/bin/python3

"""
doc
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    
    """
    doc
    """
    
    root = ET.Element('data')
    
    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = value
        root.append(child)

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    
    cons_dict = {}
    
    tree = ET.parse(filename)
    root = tree.getroot()
    
    for child in root:
        cons_dict[child.tag] = child.text
    
    return cons_dict
