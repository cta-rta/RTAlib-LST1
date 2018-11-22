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
import time
from random import uniform

from PyRTAlib.DataModels.EVTbase import EVTbase

class EVT1(EVTbase):
    def __init__(self, event_id, x, y, r, phi, length, width, psi, skewness, kurtosis, disp, hadroness, src_x, src_y, time_gradient, intercept, gps_time, mc_energy, mc_alt, mc_az, mc_core_x, mc_core_y, mc_h_first_int, mc_type, mc_az_tel, mc_alt_tel, mc_x_max, mc_core_distance, mc_shower_primary_id, hadroness, wl, impact, obs_id, datarepositoryid, status ):
        super().__init__();

        self.event_id = event_id
        self.x = x
        self.y = y
        self.r = r
        self.phi = phi
        self.length = length
        self.width = width
        self.psi = psi
        self.skewness = skewness
        self.kurtosis = kurtosis
        self.disp = disp
        self.hadroness = hadroness
        self.src_x = src_x
        self.src_y = src_y
        self.time_gradient = time_gradient
        self.intercept = intercept
        self.gps_time = gps_time
        self.mc_energy = mc_energy
        self.mc_alt = mc_alt
        self.mc_az = mc_az
        self.mc_core_x = mc_core_x
        self.mc_core_y = mc_core_y
        self.mc_h_first_int = mc_h_first_int
        self.mc_type = mc_type
        self.mc_az_tel = mc_az_tel
        self.mc_alt_tel = mc_alt_tel
        self.mc_x_max = mc_x_max
        self.mc_core_distance = mc_core_distance
        self.mc_shower_primary_id = mc_shower_primary_id
        self.hadroness = hadroness
        self.wl = wl
        self.impact = impact
        self.observationid = obs_id
        self.datarepositoryid = datarepositoryid
        self.status = status


    def getData(self):
        """Return the 'dictionary' representation of the object.
        """
        return vars(self)

    @staticmethod
    def getRandomEvent():
        rndEvent = []

        #rndEvent.append(uniform(0, 9999999))

        return rndEvent
