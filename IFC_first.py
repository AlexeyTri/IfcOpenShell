"""
Курс "ТИМ-ориентированная аналитика. Современные инструменты работа с данными"
Блок 2 - Работа с IFC и XML в Python
Официальная справка см. здесь - https://ifcopenshell.github.io/docs/python/html/index.html
Урок: Общие команды для работы с IFC
ДЕМОНСТРАЦИОННЫЙ
"""
import _general
from _general import mguu_cource_tools
import uuid #генерит униакльный id номер,в зависисмости от вызываемой функции id может быть безопасным uuid4(), так и не безопасный uuid1()
import ifcopenshell as _ifc
import os

#by type
# ifc_file = _ifc.open(mguu_cource_tools.get_example_file_path("Renga_House.ifc"))
# ifc_project = ifc_file.by_type("IfcProject")[0]
# print(str(ifc_project.get_info()))

file_dir = os.path.dirname(__file__)
ifc_file_path = os.path.join(file_dir + '\DataExamples\\' + "Renga_House.ifc")
ifc_file_path_2 = os.path.abspath(os.path.realpath(ifc_file_path))
file = _ifc.open(ifc_file_path_2)
print(file)
print(file_dir)
print(ifc_file_path)
print(ifc_file_path_2)
