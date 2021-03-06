# Copyright 2017-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.confd import confd
from wazo_admin_ui.helpers.service import BaseConfdService


class DeviceService(BaseConfdService):
    resource_confd = 'devices'

    def autoprov(self, device_id):
        confd.devices.autoprov(device_id)

    def synchronize(self, device_id):
        confd.devices.synchronize(device_id)
