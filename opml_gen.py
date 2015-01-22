#!/usr/bin/env python
# -*- coding:utf-8 -*-

import xml.etree.ElementTree as ET
from xml.dom import minidom

root = ET.Element('opml')
root.set('version', '1.0')
head = ET.SubElement(root, 'head')
title = ET.SubElement(head, 'title', {'text':'RSS feeds of deepurple'})
body = ET.SubElement(root, 'body')

for record_group in record_groups:
    feed_group = ET.SubElement(body, 'outline',
                              {'title':record_group.title,
                               'text':record_group.text})
    for record in records:
        feed = ET.SubElement(feed_group, 'outline',
                            {'text':record.text,
                             'title':record.title,
                             'type':'rss',
                             'xmlUrl':record.xmlUrl,
                             'htmlUrl':record.htmlUrl})

rough_string = ET.tostring(root, 'utf-8')
reparsed = minidom.parseString(rough_string)
with open('feeds.opml', 'w') as opml:
    opml.write(reparsed.toprettyxml(indent='    '))