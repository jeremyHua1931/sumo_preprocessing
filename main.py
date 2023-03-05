# -*- encoding: utf-8 -*-
"""
@File    :   main.py
@Contact :   jeremyhua@foxmail.com

@Modify Time      @Author       @Version     @Description
------------      -------       --------     -----------
2023/3/5 17:21   HuaZhangzhao    1.0          None
"""
from src import parse_xml, parse_read

if __name__ == '__main__':
    orgin_net_xml_file = 'origin_net_xml/demo3.net.xml'
    parse_xml.parse_xml_main(orgin_net_xml_file)
    parse_read.parse_read_main(orgin_net_xml_file)
