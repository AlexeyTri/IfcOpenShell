"""
Курс "ТИМ-ориентированная аналитика. Современные инструменты работа с данными"
Блок 2 - Работа с IFC и XML-язык разметки аналог HTTP в Python
Официальная справка см. здесь - https://ifcopenshell.github.io/docs/python/html/index.html
Урок: Работа с XML (на примере чтения файла LandXML)
Материал по теме:
ДЕМОНСТРАЦИОННЫЙ
"""

from _general import mguu_cource_tools
import xml.etree.ElementTree as xml

xml_file = xml.parse(mguu_cource_tools.get_example_file_path('Landxml_example_surfaces.xml'))
ns_xmlns = "{http://www.landxml.org/schema/LandXML-1.1}"
xml_surface_block = xml_file.find(ns_xmlns + "Surfaces")
xml_surface_list = xml_surface_block.findall(ns_xmlns + "Surface")
surface_data = dict()
for xml_surface in xml_surface_list:
    surface_name = xml_surface.attrib["name"]
    xml_surface_def = xml_surface.find(ns_xmlns + "Definition")
    xml_attrs = xml_surface_def.attrib
    attrs_list = dict()
    for xml_attr_name in xml_attrs:
        attr_value = xml_attrs[xml_attr_name]
        attrs_list[xml_attr_name] = attr_value
    surface_data[surface_name] = attrs_list
print(str(surface_data))