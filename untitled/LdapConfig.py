#!/usr/bin/env python3
# _*_coding:utf-8 _*_

import configparser
import os

class LdapConfig(object):
    def __init__(self):
        pass

    def getValue(self,key,section='ldap_db'):
        conf = configparser.ConfigParser()
        curPath = os.path.abspath(os.path.dirname(__file__))
        conf.read(os.path.join(curPath,'ldap.cfg'))
        value = conf.get(section, key)
        return value
