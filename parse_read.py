# -*- encoding: utf-8 -*-
"""
@File    :   parse_read.py
@Contact :   jeremyhua@foxmail.com

@Modify Time      @Author       @Version     @Description
------------      -------       --------     -----------
2023/3/5 14:20   HuaZhangzhao    1.0          None
"""
import json
import os
import xml.etree.ElementTree as ET


def read_res_parse_edges():
    with open('res/result_edges_parse.json', 'r') as f:
        read_edges = json.load(f)
    # print("{:=^50s}".format("Parse_edges"))
    # for x in read_edges:
    #     print(x)
    return  read_edges

def read_res_parse_junctions():
    with open('res/result_junctions_parse.json', 'r') as f:
        read_junctions = json.load(f)
    # print("{:=^50s}".format("Parse_junctions"))
    # for x in read_junctions:
    #     print(x)
    return read_junctions

def read_res_parse_connections():
    with open('res/result_connections_parse.json', 'r') as f:
        read_connections= json.load(f)
    # print("{:=^50s}".format("Parse_junctions"))
    # for x in read_connections:
    #     print(x)
    return read_connections

def read_res_id_map_edge():
    with open('res/result_id_map_edge.json', 'r') as f:
        read_edge_id_map = json.load(f)
    # print("{:=^50s}".format("id_map_edge"))
    # for x in read_edge_id_map:
    #     print(x, "\t", read_edge_id_map[x])
    read_edge_id_map

def read_res_id_map_lane():
    with open('res/result_id_map_lane.json', 'r') as f:
        read_lane_id_map = json.load(f)
    # print("{:=^50s}".format("id_map_lane"))
    # for x in read_lane_id_map:
    #     print(x, "\t", read_lane_id_map[x])
    read_lane_id_map

def  trans_xml_edges(edges):
    xml_str_edges = ""
    for edge in edges:
        if 'function' in edge:
            xml_str_edges += f'<edge id="{edge["id"]}" function="{edge["function"]}">\n'
        else:
            xml_str_edges += f'<edge id="{edge["id"]}" from="{edge["from"]}" to="{edge["to"]}" priority="{edge["priority"]}">\n'
        for lane in edge["lanes"]:
            xml_str_edges += f'    <lane id="{lane["id"]}" index="{lane["index"]}" speed="{lane["speed"]}" length="{lane["length"]}" shape="{lane["shape"]}" />\n'
        xml_str_edges += '</edge>\n'
    return xml_str_edges

def trans_xml_junctions(junctions):
    xml_str_junctions = ""
    for junction in junctions:
        xml_str_junctions += f'<junction id="{junction["id"]}" type="{junction["type"]}" x="{junction["x"]}" y="{junction["y"]}" incLanes="{junction["incLanes"]}" intLanes="{junction["intLanes"]}"'
        if 'shape' in junction:
            xml_str_junctions += f'\nshape="{junction["shape"]}">\n'
            for request in junction["requests"]:
                xml_str_junctions += f'    <request index="{request["index"]}" response="{request["response"]}" foes="{request["foes"]}" cont="{request["cont"]}" />\n'
            xml_str_junctions += '</junction>\n'
        else:
            xml_str_junctions += "/>"


    return xml_str_junctions

def trans_xml_connections(connections):
    xml_str_connections = ""
    for connection in connections:
        if 'via' in connection:
            xml_str_connections += '<connection from="{}" to="{}" fromLane="{}" toLane="{}" via="{}" dir="{}" state="{}" />\n'.format(
                connection["from"], connection["to"], connection["fromLane"], connection["toLane"], connection["via"],
                connection["dir"], connection["state"])
        else:
            xml_str_connections += '<connection from="{}" to="{}" fromLane="{}" toLane="{}" dir="{}" state="{}" />\n'.format(
                connection["from"], connection["to"], connection["fromLane"], connection["toLane"], connection["dir"],
                connection["state"])
    return xml_str_connections


def parse_read_main(new_net_xml_file):
    read_res_id_map_edge()
    read_res_id_map_lane()

    edges=read_res_parse_edges()
    junctions=read_res_parse_junctions()
    connections=read_res_parse_connections()

    xml_core=trans_xml_edges(edges=edges)+"\n"+trans_xml_junctions(junctions=junctions)+"\n"+trans_xml_connections(connections=connections)
    f=open('new_xml_core.xml','w')
    print(xml_core,file=f)
    f.close()

    # 解析原始XML文件
    tree = ET.parse(new_net_xml_file)
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

    # 保存修改后的XML文件
    tree.write('new_'+new_net_xml_file)




















