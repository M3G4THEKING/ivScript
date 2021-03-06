#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configparser import ConfigParser

####Hier wird die Config aus dem Configfile geladen und den einzelen
####Werten zugewiesen

class Config():
  host = ""
  database = ""
  user = ""
  password = ""
  sleepTime = ""
  nuller = ""
  rocketStops = ""
  lureModule = ""
  hours = ""
  min_latitude = ""
  max_latitude = ""
  min_longitude = ""
  max_longitude = ""
  token = ""
  ivchatId = ""
  ivchatUrl = ""
  chatId = ""
  chatUrl = ""
  areaName = ""
  iv100 = ""
  iv0 = ""

  def readConfig(self,cfgFile):  
    parser = ConfigParser()
    parser.read(cfgFile, encoding='utf-8')

    self.host = parser.get('Mysql', 'host')
    self.database = parser.get('Mysql', 'database')
    self.user = parser.get('Mysql', 'user')
    self.password = parser.get('Mysql', 'password')

    self.token = parser.get('Bot Settings', 'token')
    self.ivchatId = parser.get('Bot Settings', 'ivchat_id')
    self.ivchatUrl = parser.get('Bot Settings', 'ivchat_url')
    self.chatId = parser.get('Bot Settings', 'chat_id')
    self.chatUrl = parser.get('Bot Settings', 'chat_url')

    self.nuller = parser.get('Modul','nuller')

    self.sleepTime = parser.get('Message', 'sleep_time')

    #self.newMessageAfter = parser.get('Message', 'newMessageAfter')
    #self.rocketStops = parser.get('Options', 'rocketStops')
    #self.lureModule = parser.get('Options', 'lureModule')
    #self.hours = parser.get('Options', 'defineHours')
    
    self.areaName = parser.get('Geofence', 'areaName')
    self.iv100 = parser.get('IV', '100')
    self.iv0 = parser.get('IV', '0')

    self.min_latitude = parser.get('Geofence', 'minLat')
    self.max_latitude = parser.get('Geofence', 'maxLat')
    self.min_longitude = parser.get('Geofence', 'minLon')
    self.max_longitude = parser.get('Geofence', 'maxLon')