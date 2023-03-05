# -*- encoding: utf-8 -*-
"""
@File    :   main.py
@Contact :   jeremyhua@foxmail.com

@Modify Time      @Author       @Version     @Description
------------      -------       --------     -----------
2023/3/5 17:21   HuaZhangzhao    1.0          None
"""
import os
import time

import src.parse_generate
from src import parse_xml, parse_read, parse_generate

if __name__ == '__main__':
    origin_net_xml_file = 'origin_net_xml/osm.net.xml'
    parse_xml.parse_xml_main(origin_net_xml_file)
    generate_net_file = str("new_" + origin_net_xml_file.split("/")[1])
    print("Generate new net.xml :", generate_net_file, " Modify-time:", time.ctime(os.path.getmtime(generate_net_file)))
    src.parse_generate.get_origin_info(origin_net_xml_file, generate_net_file)
    parse_generate.generate_complete_new_xml(generate_net_file)
