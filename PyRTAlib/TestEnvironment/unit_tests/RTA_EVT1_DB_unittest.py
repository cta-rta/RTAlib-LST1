# ==========================================================================
#
# Copyright (C) 2018 INAF - OAS Bologna
# Author: Leonardo Baroncelli <leonardo.baroncelli26@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ==========================================================================

#!/usr/bin/env python

import unittest
from sys import path
from os.path import dirname, abspath, realpath

rootFolder = dirname(dirname(dirname(dirname(realpath(__file__)))))
path.append(rootFolder+'/PyRTAlib/')

from lst_PyRTAlib.RTAInterface import RTA_EVT1_DB
from PyRTAlib.Utils.UtilsUT import getConfig
from PyRTAlib.Utils.UtilsUT import UtilsMySql
from PyRTAlib.Utils.UtilsUT import UtilsRedis

config_file_path = '../../../../../../RTAlib/Configs/rtalibconfig_lst_evt1'
tableName = ''
DEBUG = False

"""
 (                                              (
 )\ )  *   )   (                   *   )    )   )\ )   (
(()/(` )  /(   )\      (   (   ( ` )  /( ( /(  (()/( ( )\
 /(_))( )(_)|(((_)(    )\  )\  )\ ( )(_)))\())  /(_)))((_)
(_)) (_(_()) )\ _ )\  ((_)((_)((_|_(_())((_)\  (_))_((_)_
| _ \|_   _| (_)_\(_) | __\ \ / /|_   _|__ (_)  |   \| _ )
|   /  | |    / _ \   | _| \ V /   | |  |_ \    | |) | _ \
|_|_\  |_|   /_/ \_\  |___| \_/    |_| |___/    |___/|___/
                                                           """


class RTA_EVT1_DB_interface(unittest.TestCase):

    # test connection
    def test_connection(self):
        getConfig(config_file_path, DEBUG, reload=True).set('General', 'numberofthreads', 0)
        rta_evt1_db_mysql = RTA_EVT1_DB('mysql', config_file_path)
        rta_evt1_db_redis = RTA_EVT1_DB('redis-basic', config_file_path)
        self.assertEqual(True, rta_evt1_db_mysql.dbConnector.testConnection())
        self.assertEqual(True, rta_evt1_db_redis.dbConnector.testConnection())

if __name__ == '__main__':
    unittest.main()
