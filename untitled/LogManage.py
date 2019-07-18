#!/usr/bin/env python3
# _*_coding:utf-8 _*_
'''
  日志管理
   日志开关，在config/config.cfg下
   True：开启
   False：关闭
'''
import  logging

from config.ConfigManage import ConfigManage


class LogManage(object):

    @classmethod
    def getLogger(self,fileName):
        self._logger=logging.getLogger(fileName)
        logManage=LogManage()
        return logManage

    def info(self,message):
        on  = ConfigManage().getValue('onInfo','log')
        if on=='True':
            self._logger.info(message)

    def error(self,message):
        on = ConfigManage().getValue('onError', 'log')
        if on=='True':
            self._logger.error(message)

    def debug(self,message):
        self._logger.debug(message)
