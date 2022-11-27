"""
Курс "ТИМ-ориентированная аналитика. Современные инструменты работа с данными"
Блок 2 - Работа с IFC и XML в Python
Официальная справка см. здесь - https://ifcopenshell.github.io/docs/python/html/index.html
Урок: Составление IFC-файла вручную
Оригинальный материал: https://academy.ifcopenshell.org/posts/creating-a-simple-wall-with-property-set-and-quantity-information/
ДЕМОНСТРАЦИОННЫЙ
Construction Solid Geometry (CSG) - трехмерный примитив, строительная трехмерная геометрия
"""

from _general import mguu_cource_tools
import ifcopenshell as _ifc

#элементарная геометрия
point_center = 0.0, 0.0, 0.0
dir_x = 1.0, 0.0, 0.0
dir_y = 0.0, 1.0, 0.0
dir_z = 0.0, 0.0, 1.0

#создание IfcAxis2Placement3D - создание сетки координат
def create_IfcAxis2Placement3D(point = point_center, dir1= dir_z, dir2 = dir_x):
    new_ifc_point = ifc_file.createIfcCattesianPoint(point)
    new_ifc_dir1 = ifc_file.createIfcDirection(dir1)
    new_ifc_dir2 = ifc_file.createIfcDirection(dir2)
    new_ifc_IfcAxis2Placement3D =  ifc_file.createIfcAxis2Placement3D(new_ifc_point, new_ifc_dir1, new_ifc_dir2)
    return new_ifc_IfcAxis2Placement3D

#создание IfcLocalPlacement - расположение объекта в локальной системе координат -> наследование сущностей
def create_IfcLocalPlacmenet(point=point_center, dir1=dir_z, dir2=dir_x,relative_to=None):
    aux_IfcAxis2Placement3D = create_IfcAxis2Placement3D(point, dir1, dir2)
    new_ifc_IfcLocalPlacement = ifc_file.createLocalPlacement(relative_to, aux_IfcAxis2Placement3D)
    return new_ifc_IfcLocalPlacement

#создание цилиндрa IfcRightCircularCylinder - это твердое тело в круглым основанием и врешиной. Позиция определяется наследованием IfcAxisPlacement3D
def create_IfcRightCircularCylinder(object_IfcAxis2Placement3D, height, radius):
    new_ifc_IfcRightCircularCylinder = ifc_file.createIfcRightCircularCylinder(object_IfcAxis2Placement3D, height, radius)
    return new_ifc_IfcRightCircularCylinder

#создание конуса IfcRightCircularCone - это твердое тело в круглым основанием и врешиной. Позиция определяется наследованием IfcAxisPlacement3D
def create_IfcRightCircularCone(object_IfcAxis2Placement3D, height, bottom_radius):
    new_ifc_IfcRightCircularCone = ifc_file.createIfcRightCircularCone(object_IfcAxis2Placement3D, height, bottom_radius)
    return new_ifc_IfcRightCircularCone

ifc_file_path = mguu_cource_tools.create_ifc_by_template()
global ifc_file
ifc_file = _ifc.open(ifc_file_path)

print(ifc_file.by_type("IfcProject")[0])





