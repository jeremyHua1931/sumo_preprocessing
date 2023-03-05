# -*- encoding: utf-8 -*-
"""
@File    :   parse_generate.py   
@Contact :   jeremyhua@foxmail.com
 
@Modify Time      @Author       @Version     @Description
------------      -------       --------     -----------
2023/3/5 21:10   HuaZhangzhao    1.0         None
"""
from src import parse_read
import xml.etree.ElementTree as ET


def generate_edge(edges):
    root = ET.Element("root")
    for item in edges:
        element = ET.SubElement(root, "edge", item)
        for lane in item['lanes']:
            ET.SubElement(element, "lane", lane)
    xml_data = ET.tostring(root).decode()
    return xml_data


def generate_junction(junctions):
    root = ET.Element('root')
    for item in junctions:
        if 'shape' in item:
            junction = ET.SubElement(root, 'junction', id=item['id'], type=item['type'], x=item['x'], y=item['y'],
                                     incLanes=item['incLanes'], intLanes=item['intLanes'], shape=item['shape'])
            for req in item['requests']:
                ET.SubElement(junction, 'request', index=req['index'], response=req['response'], foes=req['foes'],
                              cont=req['cont'])
        else:

            ET.SubElement(root, 'junction', id=item['id'], type=item['type'], x=item['x'], y=item['y'],
                          incLanes=item['incLanes'], intLanes=item['intLanes'])
    xml_data = ET.tostring(root).decode()
    return xml_data


def generate_connection(connections):
    root = ET.Element('root')
    for item in connections:
        connection = ET.SubElement(root, 'connection')
        connection.attrib = item
    xml_data = ET.tostring(root).decode()
    return xml_data


def get_origin_info(origin_file, generate_file):
    # 解析原始XML文件
    tree = ET.parse(origin_file)
    root = tree.getroot()

    # 删除所有的edge标签
    for edge in root.findall('edge'):
        root.remove(edge)

    # 删除所有的junction标签
    for junction in root.findall('junction'):
        root.remove(junction)

    # 删除所有的connection标签
    for connection in root.findall('connection'):
        root.remove(connection)

    info = ET.tostring(root).decode()
    with open(generate_file, 'w') as f:
        print(info, file=f)


def generate_complete_new_xml(generate_file):
    edges = parse_read.read_res_parse_edges()
    junctions = parse_read.read_res_parse_junctions()
    connections = parse_read.read_res_parse_connections()

    # 解析XML文件
    tree = ET.parse(generate_file)
    root = tree.getroot()

    xml_edges = generate_edge(edges=edges)
    xml_edges_root = ET.fromstring(xml_edges)
    for edge in xml_edges_root.findall('edge'):
        root.append(edge)

    xml_junction = generate_junction(junctions=junctions)
    xml_junction_root = ET.fromstring(xml_junction)
    for junction in xml_junction_root.findall('junction'):
        root.append(junction)

    xml_connection = generate_connection(connections=connections)
    xml_connection_root = ET.fromstring(xml_connection)
    for connection in xml_connection_root.findall('connection'):
        root.append(connection)

    result = ET.tostring(root).decode()

    with open(generate_file, 'w') as f:
        print(result, file=f)
