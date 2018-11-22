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

from PyRTAlib.RTAInteface import RTA_DL_DB
from ..DataModels import EVT1


class RTA_EVT1_DB(RTA_DL_DB):

    def __init__(self, database, configFilePath = ''):
        super().__init__(database, configFilePath)

        # Pipeline Database Updater
        """
        if not self.multithreading and self.config.get('MySqlPipelineDatabase', 'active', 'bool'):
            self.mysqlDbConnector = self.getMySqlConnector(configFilePath, 'MySqlPipelineDatabase')
            if self.mysqlDbConnector.connect():
                print('[RTA_EVT1_DB] Pipeline updater activated.')
            else:
                print('[RTA_EVT1_DB] Cannot connect.')
        """

    def insertEvent(self, eventidfits, x, y, r, phi, length, width, psi, skewness, kurtosis, disp, hadroness, src_x, src_y, time_gradient, intercept, gps_time, mc_energy, mc_alt, mc_az, mc_core_x, mc_core_y, mc_h_first_int, mc_type, mc_az_tel, mc_alt_tel, mc_x_max, mc_core_distance, mc_shower_primary_id, hadroness, wl, impact, observationid, datarepositoryid, status):
        evt1 = EVT1(eventidfits, x, y, r, phi, length, width, psi, skewness, kurtosis, disp, hadroness, src_x, src_y, time_gradient, intercept, gps_time, mc_energy, mc_alt, mc_az, mc_core_x, mc_core_y, mc_h_first_int, mc_type, mc_az_tel, mc_alt_tel, mc_x_max, mc_core_distance, mc_shower_primary_id, hadroness, wl, impact, observationid, datarepositoryid, status)
        committed = super()._insertEvent(evt1)


    def getRandomEvent(self):
        return EVT1.getRandomEvent()
