# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from wazo_admin_ui.helpers.classful import BaseDestinationView


class DeviceDestinationView(BaseDestinationView):

    def list_json(self):
        params = self._extract_params()
        devices = self.service.list(**params)
        results = [{'id': device['id'], 'text': device['mac']} for device in devices['items']]
        return self._select2_response(results, devices['total'], params)
