# -*- encoding: utf-8 -*-
"""
@File    :   parse_read.py
@Contact :   jeremyhua@foxmail.com

@Modify Time      @Author       @Version     @Description
------------      -------       --------     -----------
2023/3/5 14:20   HuaZhangzhao    1.0          None
"""
import json
import xml.etree.ElementTree as ET


def read_res_parse_edges():
    with open('res/result_edges_parse.json', 'r') as f:
        read_edges = json.load(f)
    return read_edges


def read_res_parse_junctions():
    with open('res/result_junctions_parse.json', 'r') as f:
        read_junctions = json.load(f)
    return read_junctions


def read_res_parse_connections():
    with open('res/result_connections_parse.json', 'r') as f:
        read_connections = json.load(f)
    return read_connections


def read_res_id_map_edge():
    with open('res/result_id_map_edge.json', 'r') as f:
        read_edge_id_map = json.load(f)
    return read_edge_id_map


def read_res_id_map_lane():
    with open('res/result_id_map_lane.json', 'r') as f:
        read_lane_id_map = json.load(f)
    return read_lane_id_map


